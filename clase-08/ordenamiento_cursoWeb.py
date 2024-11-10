"""
Una platasforma web utiliza la siguiente estructura de datos para almacenar
su catalosgo de cursos online:
Código des curso (número entero)
Nombre desl curso (string)
Descripcisón del curso (string)
Horas de duración (número decimal)
Categoría del curso (string)

Se pide hacer un programa, donde utilizando un menú permita
resolver lo siguiente

CARGAR CURSOS (CARGA MÁXIMA 10 ELEMENTOS, PERO PUEDE CARGAR MENOS).
No se permiten registros duplicados con el mismo código de curso
(es requisito validar esto).
Mostrar todos los cursos cargados
Informar el curso de mayor duración.
Dado un código de curso informar la categoría a la que pertenece.
En caso de que no exista informarlo tambien. Utilizar búsqueda secuencial
Salir
"""


# clase platasforma web
class webPlataform:
    def __init__(self, cod: int, name: str, desc, horas: float, categoria):
        self.codigo = cod
        self.nombre = name
        self.descripcion = desc
        self.horas_duracion = horas
        self.categoria = categoria

    def __str__(self):
        return f"Curso {self.codigo} ({self.categoria}): {self.nombre}\nDescripcion: {self.descripcion}\nDuracion: {self.horas_duracion}"


# probando objeto
# micurso = webPlataform(
#     1, "mi cursito", "descripcion probando", 7.5, "de asado")
# print(micurso)

# clase gestor de cursos


class gestorDeCursos:
    def __init__(self):
        self.max_cursos = 10
        self.cursos = []

    def __str__(self):
        if len(self.cursos) > 0:
            return str(self.cursos)
        else:
            return "Aun no hay cursos cargados"

    def agregarCurso(self, nuevo_curso):
        if len(self.cursos) < self.max_cursos:
            self.cursos.append(nuevo_curso)
            print("Se ha ingresado un nuevo curso!")
        else:
            print("La lista de cursoso esta llena")

    def obtenerNuevoCodigo(self):
        return len(self.cursos) + 1


# gestor_de_cursos = gestorDeCursos()
# print(gestor_de_cursos)
# micurso = webPlataform(
#     gestor_de_cursos.obtenerNuevoCodigo(),
#     "mi cursito",
#     "descripcion probando",
#     7.5,
#     "de asado",
# )
# gestor_de_cursos.agregarCurso(micurso)
# print(micurso)

# menu


def mostrarMenu():
    print("1 - Cargar curso")
    print("2 - Mostrar Cursos")
    print("3 - Informar curso de mayor duracion")
    print("4 - Buscar categoria de curso")
    print("5 - Salir")


gestor_de_cursos = gestorDeCursos()


def cargarCursos():
    global gestor_de_cursos
    while True:
        codigo = validarCodigo()
        nombre = input("Ingrese nombre de curso: ")
        descripcion = input("Ingrese descripcion del curso: ")
        horas_de_duracion = float(input("Ingrese las horas de duracion: "))
        categoria = input("Ingrese la categoria del curso: ")
        new_course = webPlataform(
            codigo, nombre, descripcion, horas_de_duracion, categoria
        )
        gestor_de_cursos.agregarCurso(new_course)
        x = input("Desea agregar un curso nuevo s/n ")
        x = x.lower()
        print(x)
        if x == "n":
            break


def validarCodigo():
    validar_codigo = int(input("Ingrese el codigo del curso: "))
    print(validar_codigo)
    for curso in gestor_de_cursos.cursos:
        print(curso.codigo, "codigo iterado de cursos")
        print(validar_codigo, "user dentro del for")
        print("dentro del for", validar_codigo)
        if curso.codigo == validar_codigo:
            print("Codigo Existente, Ingrese un codigo diferente")
            return validarCodigo()
    print("fuera del for", validar_codigo)

    return validar_codigo


def mostrarCursos():
    for cursos in gestor_de_cursos.cursos:
        print(cursos)


cargarCursos()

for curso in gestor_de_cursos.cursos:
    print(curso.codigo)
