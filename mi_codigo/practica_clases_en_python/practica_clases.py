# Una plataforma web utiliza la siguiente estructura de datos para almacenar su catalogo de cursos online:
#
# - Código de curso (número entero)
# - Nombre del curso (string)
# - Descripción del curso (string)
# - Horas de duración (número decimal)
# - Categoría del curso (string)
#
# Se pide hacer un programa, donde utilizando un menú permita resolver lo siguiente
#
# 1. Cargar cursos (Carga máxima 10 elementos, pero puede cargar menos). No se permiten registros duplicados con el mismo código de curso (**es requisito validar esto**).
# 2. Mostrar todos los cursos cargados
# 3. Informar el curso de mayor duración.
# 4. Dado un código de curso informar la categoría a la que pertenece. En caso de que no exista informarlo tambien. Utilizar búsqueda secuencial
# 5. Salir


class Cursos:
    def __init__(self, cod: int, name, des, hrs, cate):
        self.codigo = cod
        self.nombre = name
        self.descripcion = des
        self.horas_duracion = hrs
        self.categoria = cate

    def __str__(self) -> str:
        return f'Codigo: {self.codigo}\nNombre: {self.nombre}\nDescripcion: {self.descripcion}\nHoras de duración {self.horas_duracion}\n Categoria: {self.categoria}'

# prueba

# new_curse = Cursos(12, 'Hamburguesas de 0 a experto' 'Descripción de prueba', 12.34, 'Gastronomia')
# print(new_curse.categoria)


class gestorDeCursos:
    def __init__(self):
        self.max_cursos = 4
        self.cursos: list[Cursos] = []

    def __str__(self) -> str:
        return f'Cursos: {self.cursos}'

    def agregarCurso(self, nuevo_curso: Cursos):
        if len(self.cursos) < self.max_cursos:
            self.cursos.append(nuevo_curso)
        else:
            message = 'la lista esta llena'
            graph = '-' * len(message)

            print(graph)
            print(message)

    def obtenerCodigo(self, cod):
        for cursos in self.cursos:
            if cod == cursos.codigo:
                return cod


gestor_de_cursos = gestorDeCursos()

# new_curse = Cursos(11, 'Hamburguesas de 0 a experto',
#                    'prueba de cursos', 23.9, 'Programacion')
# new_curse_2 = Cursos(1, 'Hamburguesas2 de 0 a experto',
#                      'prueba de cursos', 23.9, 'de perlos')
# gestor_de_cursos.agregarCurso(new_curse_2)
# gestor_de_cursos.agregarCurso(new_curse)
# print(gestor_de_cursos)
# gestor_de_cursos.obtenerCodigo()


def cargarCurso():
    while True:
        cod = verificarCod()
        name = input('Ingrese el nombre del curso: ')
        des = input('Ingrese la descripcion del curso: ')
        hrs = float(input('Ingrese la duracion del curso: '))
        cate = input('Ingrese la categoria del curso: ')

        new_course = Cursos(cod, name, des, hrs, cate)
        gestor_de_cursos.agregarCurso(new_course)
        text = 'Desea agregar un curso nuevo s/n ? '
        graph = '-' * len(text)
        print(graph)
        opcion = input(text)
        if opcion == 'n':
            break


def verificarCod():
    global gestor_de_cursos
    cod = int(input('Ingrese el codigo del curso: '))
    verificar = gestor_de_cursos.obtenerCodigo(cod)
    if verificar == cod:
        text = 'Ese codigo esta duplicado, ingrese uno nuevo'
        graph = '-' * len(text)
        print(graph)
        print(text)
        verificarCod()
    else:
        return cod


cargarCurso()
print(gestor_de_cursos.cursos)
