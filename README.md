# Overview

- Scrapes both the course information and the final exam information from my university's website.
- The info is then filtered based on two .txt files `course_subjects.txt` and `final_exam_subjects.txt` which contain the subjects I'm interested in knowing more about, in regards to how the courses are structured and when the final exams are, respectively.
- The filtered information is then printed to the console as a table.

# Motivation

- The website contains really big tables with every single subject in the university, which makes it annoying and time-consuming to find the information about the subjects I actually care about.
- I wanted to semi-automate the process of finding this information, so I don't really have to go manually to the website anymore. This is important because the site is updated pretty frequently, so I'd have to go check it every now and then to see if there are any changes in the courses or the final exams, which I don't want to do anymore.

# Requirements

- Python 3.13.
- `uv` for dependency management.

# How to use

1. Clone the repo and `cd` into it.
2. Run `uv sync` so the dependencies are installed and the virtual environment is created.
3. Create the two .txt files `course_subjects.txt` and `final_exam_subjects.txt` in the root directory of the project, and fill them with the subjects you want to know information about, one per line.
4. Run `uv run main.py` to execute the script and see the output on the console. Optionally, you can pass a year as an argument to filter "Last modified" column by that year, for example `uv run main.py --year 2026` to only show the courses and final exams that were last updated in 2026.

# Example

- Assuming `course_subjects.txt` contains the following subjects:

```
Teoría de la Computación y Verificación de Programas
Diseño de Experiencia de Usuario
```

- And `final_exam_subjects.txt` contains the following subjects:

```
Minería de Datos usando Sistemas Inteligentes
Computabilidad y Complejidad
Programación Distribuida y Tiempo Real
Desarrollo Seguro de Aplicaciones
Matemática 4
Teoría de la Computación y Verificación de Programas
Diseño de Experiencia de Usuario
```

- The output on the console would be something like this:

```
Courses information:
+------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------+---------------------+
| Materia                                              | Inicio cursada                        | Horarios cursada                                                       | Última modificación |
+------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------+---------------------+
| Diseño de Experiencia de Usuario                     | Martes 18 de marzo 18 horas. Aula 1.4 | Teorías: miércoles 8.30 hs. Aula 1.4 Prácticas: martes 18 hs. Aula 1.4 | 12/03/2025 09:18 AM |
| Teoría de la Computación y Verificación de Programas | Martes 10 de marzo de 2026            | Clases teóricas martes de 19 a 21 Clases prácticas jueves de 19 a 21   | 10/02/2026 02:27 PM |
+------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------+---------------------+

Final exams information:
+------------------------------------------------------+-----------+----------+---------------------------------------------------------------------------------------------------------+---------------------+
| Materia                                              | Día       | Hora     | Observaciones                                                                                           | Última modificación |
+------------------------------------------------------+-----------+----------+---------------------------------------------------------------------------------------------------------+---------------------+
| Computabilidad y Complejidad                         | Viernes   | 08:30 AM | Contactar por Ideas en la semana, previo al día del examen, por Ideas, en la asignatura que corresponde | 02/10/2025 12:10 PM |
| Desarrollo Seguro de Aplicaciones                    | Viernes   | 09:00 AM | LINTI                                                                                                   | 05/11/2018 06:29 PM |
| Diseño de Experiencia de Usuario                     | Viernes   | 08:30 AM | LINTI  Enviar mail a la docente confirmando su concurrencia. El mail es iharari@info.unlp.edu.ar        | 28/02/2020 03:02 PM |
| Matemática 4                                         | Jueves    | 03:00 PM | Mesa de Septiembre:  aula 1-4                                                                           | 26/08/2024 09:55 PM |
| Minería de Datos usando Sistemas Inteligentes        | Miércoles | 09:00 AM | Mesa de Septiembre:  Modalidad a distancia  Enviar mail a laural@lidi.info.unlp.edu.ar para coordinar.  | 01/09/2021 10:45 AM |
| Programación Distribuida y Tiempo Real               | Viernes   | 08:30 AM | Contactar por Ideas en la semana, previo al día del examen, por Ideas, en la asignatura que corresponde | 02/10/2025 12:10 PM |
| Teoría de la Computación y Verificación de Programas | Martes    | 07:00 PM | Aula 1-4                                                                                                | 05/11/2018 06:29 PM |
+------------------------------------------------------+-----------+----------+---------------------------------------------------------------------------------------------------------+---------------------+
```
