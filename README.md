# Overview

- Scrapes both the course information and the final exam information from my university's website.
- The info is then filtered based on two .txt files `course_subjects.txt` and `final_exam_subjects.txt` which contain the subjects I'm interested in knowing more about, in regards to how the courses are structured and when the final exams are, respectively.
- The filtered information is then printed to the console as a table.

# Motivation

- The website contains really big tables with every single subject in the university, which makes it annoying and time-consuming to find the information about the subjects I actually care about.
- I wanted to semi-automate the process of finding this information, so I don't really have to go manually to the website anymore. This is important because the site is updated pretty frequently, so I'd have to go check it every now and then to see if there are any changes in the courses or the final exams, which I don't want to do anymore.

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
| Materia                                              | Inicio Cursada                        | Horarios Cursada                                                       | Última modificación |
+------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------+---------------------+
| Diseño de Experiencia de Usuario                     | Martes 18 de marzo 18 horas. Aula 1.4 | Teorías: miércoles 8.30 hs. Aula 1.4 Prácticas: martes 18 hs. Aula 1.4 | 12/03/2025 09:18    |
| Teoría de la Computación y Verificación de Programas | Martes 10 de marzo de 2026            | Clases teóricas martes de 19 a 21 Clases prácticas jueves de 19 a 21   | 10/02/2026 14:27    |
+------------------------------------------------------+---------------------------------------+------------------------------------------------------------------------+---------------------+

Final exams information:
+------------------------------------------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Materia                                              | Día       | Hora      | Observaciones                                                                                           | Última modificación                           |
+------------------------------------------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Computabilidad y Complejidad                         | viernes   | 08:30 Hs. | Contactar por Ideas en la semana, previo al día del examen, por Ideas, en la asignatura que corresponde | Modificado por última vez el 02/10/2025 12:10 |
| Desarrollo Seguro de Aplicaciones                    | viernes   | 09:00 Hs. | LINTI                                                                                                   | Modificado por última vez el 05/11/2018 18:29 |
| Diseño de Experiencia de Usuario                     | viernes   | 08:30 Hs. | LINTI  Enviar mail a la docente confirmando su concurrencia. El mail es iharari@info.unlp.edu.ar        | Modificado por última vez el 28/02/2020 15:02 |
| Matemática 4                                         | jueves    | 15:00 Hs. | Mesa de Septiembre:  aula 1-4                                                                           | Modificado por última vez el 26/08/2024 21:55 |
| Minería de Datos usando Sistemas Inteligentes        | miércoles | 09:00 Hs. | Mesa de Septiembre:  Modalidad a distancia  Enviar mail a laural@lidi.info.unlp.edu.ar para coordinar.  | Modificado por última vez el 01/09/2021 10:45 |
| Programación Distribuida y Tiempo Real               | viernes   | 08:30 Hs. | Contactar por Ideas en la semana, previo al día del examen, por Ideas, en la asignatura que corresponde | Modificado por última vez el 02/10/2025 12:10 |
| Teoría de la Computación y Verificación de Programas | martes    | 19:00 Hs. | Aula 1-4                                                                                                | Modificado por última vez el 05/11/2018 18:29 |
+------------------------------------------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------+-----------------------------------------------+
```
