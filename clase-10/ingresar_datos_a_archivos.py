# Tomar el código base del Gestor de cursos y agregar las funciones CRUD faltantes.
# El funcionamiento del programa debe intentar leer desde el archivo CSV
# en caso de que no exista la base de datos binaria pero si existe el archivo
# binario se debe precargar la informacion desde el mismo.
# Cada vez que se agreguen, se modifiquen, o se eliminen cursos esto se debe
# sincronizar con la base de datos binaria.

from pickle import dumps, load


class Curso:
    def __init__(self, cod, name, des, cate, hrs):
        self.codigo = int(cod)
        self.nombre = name
        self.descripcion = des
        self.categoria = cate
        self.horas_duracion = float(hrs)

        # def __repr__(self):
        #    return (
        #        f"══════════════════════════════════════════\n"
        #        f"         Curso: {self.nombre} ({self.codigo})\n"
        #        f"══════════════════════════════════════════\n"
        #        f"  Descripción:  {self.descripcion}\n"
        #        f"  Categoría:    {self.categoria}\n"
        #        f"  Duración:     {self.horas_duracion} horas\n"
        #        f"══════════════════════════════════════════\n"
        #    )

    def __str__(self) -> str:
        return f"{self.codigo},{self.nombre},{self.descripcion},{self.categoria},{self.horas_duracion}"

    def mostrarCursoResumido(self):
        return f"Codigo: {self.codigo} - Nombre: {self.nombre}"


class gestorDeCursos:
    def __init__(self):
        self.max_cursos = 10
        self.cursos: list[Curso] = []

    def __str__(self):
        if len(self.cursos) > 0:
            return str(self.cursos)
        else:
            return "La lista de Cursos esta vacia"

    def agregarCurso(self, nuevo_curso):
        if len(self.cursos) < self.max_cursos:
            print("El curso ha sido agregado exitosamente!")
            self.cursos.append(nuevo_curso)
        else:
            print("La lista esta completa!")

    def obtenerCodigo(self):
        return len(self.cursos) + 1

    def buscarPorCodigo(self):
        codigo_a_buscar = input("Ingrese el codigo del curso: ")
        for curso in self.cursos:
            if codigo_a_buscar == curso.codigo:
                print(f"El curso ha sido encontrado y es {curso.nombre}")
                return curso
        return None

    def mostrarSimplificado(self):
        for cursos in self.cursos:
            print(cursos.mostrarCursoResumido())

    def mostrarTodo(self):
        if len(self.cursos) > 0:
            for cursos in self.cursos:
                print(cursos)


gestor_de_cursos = gestorDeCursos()


def crearArchivoTxt():
    global gestor_de_cursos
    with open("texto-de-prueba.txt", "wt", encoding="utf-8") as txt_file:
        for cursos in gestor_de_cursos.cursos:
            cursos = str(cursos)
            rows = cursos.split(",")
            nueva_cosa = Curso(rows[0], rows[1], rows[2], rows[3], rows[4])
            txt_file.write(str(nueva_cosa))


def crearCurso():
    while True:
        global gestor_de_cursos
        cod = gestor_de_cursos.obtenerCodigo()
        nombre = input("Ingrese el nombre del curso: ")
        des = input("Ingrese la descripcion del curso: ")
        cate = input("Ingrese la categoria del curso: ")
        duracion = input("Ingrese la duracion del curso: ")

        new_curse = Curso(cod, nombre, des, cate, duracion)
        gestor_de_cursos.agregarCurso(new_curse)
        continuar = input("Desea continuar agregando cursos ? Si/no\n")
        crearArchivoTxt()
        continuar = continuar.lower()
        if continuar in ("n", "no"):
            break


def modificarCurso():
    global gestor_de_cursos
    gestor_de_cursos.mostrarSimplificado()
    print("Para poder modificar")
    curso_encontrado = gestor_de_cursos.buscarPorCodigo()
    if curso_encontrado:
        nuevo_nombre = input("Ingrese el nuevo nombre - (Enter para dejar el actual): ")
        nuevo_descripcion = input(
            "Ingrese la nueva descripcion - (Enter para dejar el actual): "
        )
        nuevo_categoria = input(
            "Ingrese la nueva categoria - (Enter para dejar el actual): "
        )
        nuevo_duracion = input(
            "Ingrese la nueva duracion del curso - (Enter para dejar el actual): "
        )

        # cambios anteriores
        nombre_sin_cambio = curso_encontrado.nombre
        desc_sin_cambio = curso_encontrado.descripcion
        cate_sin_cambio = curso_encontrado.categoria
        duracion_sin_cambio = curso_encontrado.horas_duracion

        text_sin_cambios = "Sin aplicar Cambios"
        graph = "=" * len(text_sin_cambios)
        print(graph)
        print(text_sin_cambios)
        print(curso_encontrado)

        if nuevo_nombre:
            curso_encontrado.nombre = nuevo_nombre
        if nuevo_descripcion:
            curso_encontrado.descripcion = nuevo_descripcion
        if nuevo_categoria:
            curso_encontrado.categoria = nuevo_categoria
        if nuevo_duracion:
            curso_encontrado.horas_duracion = float(nuevo_duracion)

        text_con_cambios = "Aplicando los cambios... "
        graph2 = "=" * len(text_con_cambios)
        print(graph2)
        print(text_con_cambios)
        print(curso_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        decidir_cambios = decidir_cambios.lower()
        if decidir_cambios in ("no", "n"):
            curso_encontrado.nombre = nombre_sin_cambio
            curso_encontrado.descripcion = desc_sin_cambio
            curso_encontrado.categoria = cate_sin_cambio
            curso_encontrado.horas_duracion = float(duracion_sin_cambio)
            print("El Curso no se ha actualizado")
            crearArchivoTxt()
        else:
            print("El Curso se ha actualizado correctamente")
            crearArchivoTxt()
            print(curso_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def mostrarUnCurso():
    global gestor_de_cursos
    print("Para porder mostrar un solo curso.")
    codigo_encontrado = gestor_de_cursos.buscarPorCodigo()
    if codigo_encontrado:
        print(codigo_encontrado)
    else:
        print("El codigo no ha sido encontrado o la lista esta vacia")


def eliminarUnCurso():
    global gestor_de_cursos
    print("Para eliminar un curso.")
    curso_encontrado = gestor_de_cursos.buscarPorCodigo()
    if curso_encontrado:
        opcion = input(f"Desea eliminar {curso_encontrado} ? S/n: ")
        opcion = opcion.lower()
        if opcion in ("si", "s", "y", "yes" "ye"):
            gestor_de_cursos.cursos.remove(curso_encontrado)
            crearArchivoTxt()
            print(f"Se ha eliminado {curso_encontrado} de la lista")
        else:
            print("El curso no ha sido eliminado...")


def mostrarCSV():
    pass


menu_text = """
------------------- Menu ---------------------------

crear curso - Para crear un curso nuevo
modificar curso - Para modificar un curso
mostrar los cursos - Para listar todos los cursos cargados en memoria
mostrar un curso - Para listar un solo curso en especifico por codigo
eliminar curso - Para eliminar un curso por codigo
mostrar csv - Para mostrar desde archivo CSV

salir - Para Salir del programa
"""


def menu():
    global menu_text
    global gestor_de_cursos
    while True:
        print(menu_text)
        opcion = input("Ingrese la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear curso":
            crearCurso()
        elif opcion == "modificar curso":
            modificarCurso()
        elif opcion == "mostrar los cursos":
            gestor_de_cursos.mostrarTodo()
        elif opcion == "mostrar un curso":
            mostrarUnCurso()
        elif opcion == "eliminar curso":
            eliminarUnCurso()
        elif opcion == "mostrar csv":
            pass
        elif opcion == "salir":
            break


menu()
