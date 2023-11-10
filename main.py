class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}
        self.asistencia = 0

    def agregar_evaluacion(self, num_evaluacion, nota):
        self.notas[num_evaluacion] = nota

    def calcular_nota_final(self, ponderacion_exam, tiene_examen):
        promedio_evaluaciones = sum(self.notas.values()) / len(self.notas)
        nota_final = promedio_evaluaciones
        if tiene_examen:
            nota_examen = float(input("Ingrese la nota del examen final: "))
            nota_final = (promedio_evaluaciones * (100 - ponderacion_exam) / 100) + (nota_examen * ponderacion_exam / 100)
        return nota_final

    def agregar_asistencia(self, porcentaje):
        self.asistencia = porcentaje

    def obtener_condicion_final(self, es_practica):
        if es_practica and self.asistencia >= 80:
            return "APROBADO"
        elif not es_practica and self.asistencia >= 60:
            return "APROBADO"
        else:
            return "REPROBADO"


def main():
    nombre_curso = input("Nombre del Curso: ")
    cantidad_alumnos = int(input("Cantidad de Alumnos inscritos: "))
    alumnos = []

    for _ in range(cantidad_alumnos):
        nombre_alumno = input("Nombre del Alumno: ")
        alumnos.append(Alumno(nombre_alumno))

    cantidad_evaluaciones = int(input("Cantidad de evaluaciones: "))
    ponderacion_evaluacion = float(input("Ponderación de cada evaluación (%): "))
    tiene_examen = input("Tiene examen (S/N): ").upper() == "S"
    ponderacion_examen = 0

    if tiene_examen:
        ponderacion_examen = float(input("Ponderación del examen (%): "))

    es_practica = input("Asignatura Teórico o Práctica (T/P): ").upper() == "P"

    while True:
        print("\nMENU:")
        print("1. Ingreso de Evaluación")
        print("2. Ingreso Asistencia")
        print("3. Condición Final Alumno")
        print("4. Promedio General")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            num_evaluacion = int(input("Ingrese el número de evaluación: "))
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            for alumno in alumnos:
                if nombre_alumno == alumno.nombre:
                    nota = float(input(f"Ingrese la nota de {alumno.nombre} en la evaluación {num_evaluacion}: "))
                    alumno.agregar_evaluacion(num_evaluacion, nota)
                    break
            else:
                print(f"No se encontró al alumno con el nombre {nombre_alumno}.")

        elif opcion == "2":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            for alumno in alumnos:
                if nombre_alumno == alumno.nombre:
                    porcentaje_asistencia = float(input(f"Ingrese el porcentaje de asistencia de {alumno.nombre}: "))
                    alumno.agregar_asistencia(porcentaje_asistencia)
                    break
            else:
                print(f"No se encontró al alumno con el nombre {nombre_alumno}.")

        elif opcion == "3":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            for alumno in alumnos:
                if nombre_alumno == alumno.nombre:
                    condicion_final = alumno.obtener_condicion_final(es_practica)
                    nota_final = alumno.calcular_nota_final(ponderacion_examen, tiene_examen)
                    print(f"Condición final: {condicion_final}")
                    print(f"Nota final: {nota_final}")
                    print(f"Porcentaje de asistencia: {alumno.asistencia}%")
                    break
            else:
                print(f"No se encontró al alumno con el nombre {nombre_alumno}.")

        elif opcion == "4":
            if all(len(alumno.notas) == cantidad_evaluaciones for alumno in alumnos):
                promedio_curso = sum(alumno.calcular_nota_final(ponderacion_examen, tiene_examen) for alumno in alumnos) / len(alumnos)
                print(f"Promedio general del curso: {promedio_curso}")
            else:
                print("Falta información para calcular el promedio general.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    main()
