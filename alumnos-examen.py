# Ejercicio de clases de alumnos

class Alumno:
    def __init__(self, matricula, nombre, edad, nota):
        self.matricula = matricula
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def obtenerNombre(self):
        return self.nombre

    def obtenerNota(self):
        return self.nota

    def atributos(self):
        print("-----------------")
        print(f"- Matricula: {self.matricula}\n- Nombre: {self.nombre}\n- Edad: {self.edad}\n- Nota de Examen: {self.nota}")


cont = 1

alumnos_ls = []
max_alumnos = 3
suma = 0
promedio = None

while cont <= max_alumnos:
    matricula = cont
    nombre = input(f'nombre del Alumno {cont}: ')
    edad = input(f'nombre del edad {cont}: ')
    nota = float(input(f'nombre del nota {cont}: '))

    new_alumno = Alumno(matricula, nombre, edad, nota)
    alumnos_ls.append(new_alumno)

    cont += 1

tam = len(alumnos_ls)

# nota_baja = 999
for alumno in alumnos_ls:
    alumno.atributos()
    suma += alumno.nota
    promedio = suma / tam

    if alumno.nota < promedio:
        nota_baja = alumno.obtenerNota()
        alumno_nota_baja = alumno.obtenerNombre()

#    if alumno.nota < nota_baja:
#        nota_baja = alumno.obtenerNota()
#        alumno_nota_baja = alumno.obtenerNombre()
#
#if nota_baja == 10:
#    print("No hay nota baja, todos sacaron 10")
else:
    print(f"El Alumno {alumno_nota_baja} saco la nota mas baja y es: {nota_baja}")
print(f"El promedio de los alumnos es {promedio}")
