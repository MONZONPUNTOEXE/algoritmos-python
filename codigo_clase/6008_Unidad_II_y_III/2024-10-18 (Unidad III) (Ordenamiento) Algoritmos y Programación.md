---
Profesor: Lucas Matias Frias
Meet: https://meet.google.com/iwh-byuw-kzu
Cuadernillo:
---


## [[00 - 6008 - Algoritmos y Programación|Ir al Índice]]



![[04_BusquedayOrdenamiento.pptx (1).pdf]]


# Ejemplo de ordenamiento con Marge en cursos

- Codigo profesor

```python
class Curso:
    def __init__(self, cod, nombre, desc, horas, categoria):
        self.codigo=cod
        self.nombre=nombre
        self.descripcion=desc
        self.horas_duracion=horas
        self.categoria=categoria

    def __str__(self):
        return f"Curso {self.codigo} ({self.categoria}): {self.nombre}\nDescripcion: {self.descripcion}\nHoras de duracion: {self.horas_duracion}"

class GestorDeCursos:
    def __init__(self):
        self.limite_de_cursos=10
        self.cursos: list[Curso] = []

    def __str__(self):
        if len(self.cursos)>0:
            return str(self.cursos)
        else:
            return "No hay cursos cargados actualmente"

    def agregar_curso(self, nuevo_curso: Curso):
        if len(self.cursos)<self.limite_de_cursos:
            self.cursos.append(nuevo_curso)
        else:
            print("La lista de cursos ya se encuentra llena")

    def obtener_nuevo_codigo(self):
        return len(self.cursos)+1

gestor_de_cursos=GestorDeCursos()
def cargar_cursos():
    global gestor_de_cursos
    while True:
        nuevo_codigo = gestor_de_cursos.obtener_nuevo_codigo()
        nuevo_nombre = input("Ingrese el nombre del curso: ")
        nueva_desc = input("Ingrese la descripcion: ")
        nueva_horas = float(input("Ingrese las horas de duración: "))
        nueva_categoria = input("Ingrese la categoria")
        nuevo_curso = Curso(nuevo_codigo, nuevo_nombre, nueva_desc, nueva_horas, nueva_categoria)
        gestor_de_cursos.agregar_curso(nuevo_curso)
        desea_continuar=input("Desea continuar cargando cursos?")
        if desea_continuar != 'si':
            break

def mostrar_todos_los_cursos():
    global gestor_de_cursos
    print("Listando cursos disponibles")
    for curso in gestor_de_cursos.cursos:
        print(curso)


def mezclar_por_horas_duracion(lista, inicio, medio, fin):
    # Crea listas temporales para las mitades
    izquierda = lista[inicio:medio + 1]
    derecha = lista[medio + 1:fin + 1]

    i = j = 0  # Índices para las mitades
    k = inicio  # Índice para la lista original

    # Mezcla las dos mitades
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i].horas_duracion <= derecha[j].horas_duracion:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Copia los elementos restantes de la mitad izquierda, si los hay
    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    # Copia los elementos restantes de la mitad derecha, si los hay
    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

def merge_sort_por_horas_duracion(lista, inicio, fin):
    # Caso base: si la lista tiene 0 o 1 elementos
    if inicio < fin:
        medio = (inicio + fin) // 2  # Encuentra el punto medio
        # Ordena la mitad izquierda
        merge_sort_por_horas_duracion(lista, inicio, medio)
        # Ordena la mitad derecha
        merge_sort_por_horas_duracion(lista, medio + 1, fin)

        # Mezcla las dos mitades ordenadas
        mezclar_por_horas_duracion(lista, inicio, medio, fin)
def mezclar_por_codigo(lista, inicio, medio, fin):
    # Crea listas temporales para las mitades
    izquierda = lista[inicio:medio + 1]
    derecha = lista[medio + 1:fin + 1]

    i = j = 0  # Índices para las mitades
    k = inicio  # Índice para la lista original

    # Mezcla las dos mitades
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i].codigo <= derecha[j].codigo:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Copia los elementos restantes de la mitad izquierda, si los hay
    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    # Copia los elementos restantes de la mitad derecha, si los hay
    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

def merge_sort_por_codigo(lista, inicio, fin):
    # Caso base: si la lista tiene 0 o 1 elementos
    if inicio < fin:
        medio = (inicio + fin) // 2  # Encuentra el punto medio
        # Ordena la mitad izquierda
        merge_sort_por_codigo(lista, inicio, medio)
        # Ordena la mitad derecha
        merge_sort_por_codigo(lista, medio + 1, fin)

        # Mezcla las dos mitades ordenadas
        mezclar_por_codigo(lista, inicio, medio, fin)

def ordenar_por_merge_sort_codigo():
    global gestor_de_cursos
    todos_los_cursos = gestor_de_cursos.cursos
    merge_sort_por_codigo(todos_los_cursos, 0, len(todos_los_cursos) - 1)

def ordenar_por_merge_sort_horas_duracion():
    global gestor_de_cursos
    todos_los_cursos = gestor_de_cursos.cursos
    merge_sort_por_horas_duracion(todos_los_cursos, 0, len(todos_los_cursos) - 1)

def buscar_curso_por_codigo_y_mostrar_categoria():
    codigo_a_buscar=int(input("ingrese el código a buscar: "))
    curso_encontrado=None
    for curso in gestor_de_cursos.cursos:
        if curso.codigo==codigo_a_buscar:
            curso_encontrado=curso
    if curso_encontrado:
        print(f"La categoría del curso con código {codigo_a_buscar} es {curso_encontrado.categoria}")
    else:
        print(f"No existe un curso con código {codigo_a_buscar}")


def pedir_opcion_y_ejecutar():
    while True:
        opcion = input("ingrese la opcion seleccionada: ")
        if opcion == "cargar":
            cargar_cursos()
        elif opcion == "mostrar":
            mostrar_todos_los_cursos()
        elif opcion == "ordenar por codigo":
            ordenar_por_merge_sort_codigo()
        elif opcion == "ordenar por duracion":
            ordenar_por_merge_sort_horas_duracion()
        elif opcion == "buscar por codigo":
            buscar_curso_por_codigo_y_mostrar_categoria()
        elif opcion == "salir":
            print("Muchas gracias por usar el programa.")
            break
        else:
            print("La opción ingresada no es válida")

pedir_opcion_y_ejecutar()
```

# Ejercicio:

> En un establecimiento educativo se desea realizar un cálculo estadístico y para ello se ingresan los siguientes datos por alumno: 

- Número de legajo 
- Nombre y Apellido 
- Promedio de calificaciones 

Se desea obtener un listado ordenado por promedio en forma descendente de todos aquellos alumnos cuyo promedio supere o iguale el promedio general. Realicen