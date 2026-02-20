from datetime import datetime
from pathlib import Path

import pandas as pd
from prettytable import PrettyTable

FINAL_EXAMS_URL = "https://gestiondocente.info.unlp.edu.ar/examenes-finales/"
COURSES_URL = "https://gestiondocente.info.unlp.edu.ar/cursadas/"


def convert_24h_datetime_to_ampm(datetime_str_24h: str) -> str:
    """
    Converts a 24-hour datetime string (DD/MM/YYYY HH:MM) to a 12-hour AM/PM string
    (DD/MM/YYYY HH:MM AM/PM).
    """
    return datetime.strptime(datetime_str_24h.strip(), "%d/%m/%Y %H:%M").strftime(  # noqa: DTZ007
        "%d/%m/%Y %I:%M %p",
    )


def convert_24h_time_to_ampm(time_str_24h: str) -> str:
    """
    Converts a 24-hour time string (HH:MM) to a 12-hour AM/PM string (HH:MM AM/PM).
    """
    return datetime.strptime(time_str_24h.strip(), "%H:%M").strftime("%I:%M %p")  # noqa: DTZ007


def read_subjects_txt(file_path: str) -> list[str]:
    """
    Reads a text file containing subject names and returns it as
    a list of strings, where each string is a subject name. The text file
    should have one subject name per line.
    """
    with Path(file_path).open(mode="r", encoding="utf-8") as f:
        return [line.strip() for line in f]


def make_pretty_table(df: pd.DataFrame) -> PrettyTable:
    """
    Receives a pandas DataFrame and converts it to a PrettyTable
    object that can be printed for easier visualization.
    """
    pt_table = PrettyTable(df.columns.tolist())
    for _, row in df.iterrows():
        pt_table.add_row(row.tolist())
    pt_table.align = "l"
    return pt_table


def get_courses_data(subjects: list[str]) -> pd.DataFrame:
    """
    Receives a list of subject names and retrieves the courses data from the
    specified URL, which contains an HTML table. Then it filters the table
    to include only the rows corresponding to the provided subject names and
    returns the filtered df.
    """
    table_df = pd.read_html(COURSES_URL)[0]
    table_df = table_df.drop(columns=["Carreras"])
    table_df = table_df[table_df.iloc[:, 0].isin(subjects)]

    table_df["Última modificación"] = table_df["Última modificación"].apply(
        convert_24h_datetime_to_ampm,
    )

    return table_df


def get_final_exams_data(subjects: list[str]) -> pd.DataFrame:
    table_df = pd.read_html(FINAL_EXAMS_URL)[0]
    table_df = table_df.drop(columns=["Carreras"])
    table_df = table_df[table_df.iloc[:, 0].isin(subjects)]

    second_rows_content = table_df.groupby("Materia")["Hora"].nth(1)

    table_df = table_df[table_df.groupby("Materia").cumcount() != 1].reset_index(
        drop=True,
    )
    table_df["Última modificación"] = second_rows_content.reset_index(drop=True)

    table_df["Hora"] = table_df["Hora"].str.replace("Hs.", "")
    table_df["Hora"] = table_df["Hora"].apply(convert_24h_time_to_ampm)

    table_df["Última modificación"] = table_df["Última modificación"].str.replace(
        "Modificado por última vez el ",
        "",
    )

    table_df["Día"] = table_df["Día"].str.capitalize()

    table_df["Última modificación"] = table_df["Última modificación"].apply(
        convert_24h_datetime_to_ampm,
    )

    return table_df


def main() -> None:
    course_subjects = read_subjects_txt("course_subjects.txt")
    final_exam_subjects = read_subjects_txt("final_exam_subjects.txt")

    courses_data = get_courses_data(course_subjects)
    final_exams_data = get_final_exams_data(final_exam_subjects)

    courses_table = make_pretty_table(courses_data)
    final_exams_table = make_pretty_table(final_exams_data)

    print("Courses information:")
    print(courses_table)

    print("\nFinal exams information:")
    print(final_exams_table)


if __name__ == "__main__":
    main()
