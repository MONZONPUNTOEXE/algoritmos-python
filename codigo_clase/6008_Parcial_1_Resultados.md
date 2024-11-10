# Ejercicio 1

```python
"""  
Ejercicio con Matrices  
Dada la siguiente matriz de 4X4 deberá escribir en el  
código de programa que implemente las funciones necesarias para :  
  
Cargar la Matriz con números aleatorios del 10 al 100.  
Mostrar la matriz  
Contar los números pares de la parte inferior de la matriz (Área Gris)  
Promedio de los números que forman parte de la diagonal principal (Área verde)  
"""  
  
#1 que exista en memoria una matriz de 4X4  
#2 cargar datos aleatorios entre 10 y 100 en la matriz  
#3 mostrar la matriz  
#4 identificar los números que forman la parte inferior  
#5 calcular cuantos numeros pares hay en la parte inferior de la matriz  
#6 Identificar los numeros que forman parte de la diag princ  
#7 Sumar los numeros de la diag princ  
#8 Contar los numeros de la diag princ  
#9 divir la sumatoria entre la cantidad de nums que lograron esa sumatoria  
  
#paso 1  
import numpy as np  
  
CANT_FILAS=4  
CANT_COL=4  
  
matriz=np.ones([CANT_FILAS,CANT_COL], dtype=int)  
#Prueba paso 1  
#print(matriz)  
  
#paso 2  
  
LIM_INF=10  
LIM_SUP=100  
  
def cargar_matriz_automaticamente1():  
    from numpy import random  
    global matriz  
    matriz=random.randint(LIM_INF,LIM_SUP+1, size=(CANT_FILAS, CANT_COL))  
  
def cargar_matriz_automaticamente2():  
    import random  
    global matriz  
    for i in range(CANT_FILAS):  
        for j in range(CANT_COL):  
            matriz[i][j]=random.randint(LIM_INF,LIM_SUP)  
  
cargar_matriz_automaticamente2()  
#Paso 2 prueba  
#mostrar_matriz()  
  
#Paso 3  
def mostrar_matriz():  
    for i in range(CANT_FILAS):  
        for j in range(CANT_COL):  
            print(matriz[i][j], end='\t')  
        print()  
  
#Paso 3 prueba  
#mostrar_matriz()  
  
#Paso 4  
def mostrar_tring_inf_matriz():  
    for i in range(CANT_FILAS):  
        for j in range(CANT_COL):  
            if j<i:  
                print(matriz[i][j], end='\t')  
            else:  
                print("",end='\t')  
        print()  
  
#Paso 4 prueba  
#mostrar_matriz()  
#print()  
#mostrar_tring_inf_matriz()  
  
#Paso 5  
def contar_pares_tring_inf_matriz():  
    contador_pares=0  
    for i in range(CANT_FILAS):  
        for j in range(CANT_COL):  
            if j<i: #chequeo si la posicion es parte del triang inferior  
                if matriz[i][j]%2==0: #chequeo si el num es par  
                    contador_pares+=1  
    return contador_pares  
#Paso 5 prueba  
#cant_pares=contar_pares_tring_inf_matriz()  
#print("La cantidad de pares es ", cant_pares)  
  
#Paso 6  
def mostrar_diag_princ_matriz():  
    for i in range(CANT_FILAS):  
        for j in range(CANT_COL):  
            if j==i:  
                print(matriz[i][j], end='\t')  
            else:  
                print("",end='\t')  
        print()  
  
#Paso 6 prueba  
#mostrar_matriz()  
#print()  
#mostrar_diag_princ_matriz()  
  
#Paso 7  
def sumatoria_diag_princ_matriz():  
    sumatoria=0  
    for i in range(CANT_FILAS):  
        for j in range(CANT_COL):  
            if j==i:  
                sumatoria+=matriz[i][j]  
    return sumatoria  
  
#Prueba paso 7  
#mostrar_diag_princ_matriz()  
#sumatoria=sumatoria_diag_princ_matriz()  
#print("La sumatoria es ", sumatoria)  
  
#Paso 8  
def contar_diag_princ_matriz():  
    contador=0  
    for i in range(CANT_FILAS):  
        for j in range(CANT_COL):  
            if j==i:  
                contador+=1  
    return contador  
  
#Prueba paso 8  
#mostrar_diag_princ_matriz()  
#cantidad=contar_diag_princ_matriz()  
#print("La cantidad es ", cantidad)  
  
#Paso 9  
def calcular_promedio_diag_princ():  
    sumatoria=sumatoria_diag_princ_matriz()  
    cant_elementos=contar_diag_princ_matriz()  
    if cant_elementos>0:  
        return sumatoria/cant_elementos  
  
#Prueba paso 9  
mostrar_diag_princ_matriz()  
promedio=calcular_promedio_diag_princ()  
if promedio:  
    print("El promedio de la diag principal es ", promedio)
```
# Ejercicio 2

```python
"""  
Una plataforma web utiliza la siguiente estructura de datos para almacenar  
su catalogo de cursos online:  
  
Código de curso (número entero)  
Nombre del curso (string)  
Descripción del curso (string)  
Horas de duración (número decimal)  
Categoría del curso (string)  
  
Se pide hacer un programa, donde utilizando un menú permita  
resolver lo siguiente  
  
Cargar cursos (Carga máxima 10 elementos, pero puede cargar menos).  
No se permiten registros duplicados con el mismo código de curso  
(es requisito validar esto).  
Mostrar todos los cursos cargados  
Informar el curso de mayor duración.  
Dado un código de curso informar la categoría a la que pertenece.  
En caso de que no exista informarlo tambien. Utilizar búsqueda secuencial  
Salir  
"""  
  
#1 definir la estrutura de datos del curso  
#2 que exista una lista para almacenar los cursos  
#3 tener disponible un menu de opciones  
#4 Generar una funcion que liste las opciones y le permita al usuario  
# seleccionar una de ellas y en base a la opcion seleccionada ejecute la  
# funcion que corresponda  
# (cargar, mostrar todos, informar el de mayor duracion, buscar por cod  
# y mostrar su categoria)  
#5 Desarrollar las funciones del menu para las opciones disponibles  
#5.1 Armar funcion para cargar cursos (Carga máxima 10 elementos, pero puede cargar menos)  
#5.2 Armar funcion para mostrar todos los cursos  
#5.3 Armar funcion para buscar curso de mayor duracion  
#5.4 Armar funcion para buscar curso por código (Utilizar búsqueda secuencial)  
  
#Paso 1  
class Curso:  
    def __init__(self, cod, nombre, desc, horas, categoria):  
        self.codigo=cod  
        self.nombre=nombre  
        self.descripcion=desc  
        self.horas_duracion=horas  
        self.categoria=categoria  
  
    def __str__(self):  
        return f"Curso {self.codigo} ({self.categoria}): {self.nombre}\nDescripcion: {self.descripcion}\nHoras de duracion: {self.horas_duracion}"  
  
#Prueba paso 1  
#mi_curso=Curso(1,"Mi cursito", "Un curso de prueba", 2,"probando")  
#print(mi_curso.horas_duracion)  
  
  
#Paso 2  
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
  
#Prueba paso 2  
#gestor_de_cursos=GestorDeCursos()  
#mi_curso=Curso(1,"Mi cursito", "Un curso de prueba", 2,"probando")  
#gestor_de_cursos.cursos.append(mi_curso)  
#print(gestor_de_cursos)  
  
#Paso 3  
def mostrar_menu():  
    print("1- Cargar cursos")  
    print("2- Mostrar todos los cursos")  
    print("3- Informar curso de mayor duración")  
    print("4- Buscar curso por codigo")  
    print("5- Salir")  
  
#Prueba paso 3  
#mostrar_menu()  
  
#Paso 5.1  
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
  
#Paso 5.2  
def mostrar_todos_los_cursos():  
    global gestor_de_cursos  
    print("Listando cursos disponibles")  
    for curso in gestor_de_cursos.cursos:  
        print(curso)  
  
#Paso 5.3  
def mostrar_curso_de_mayor_duracion():  
    mayor_horas=0  
    curso_mayor_horas=None  
    global gestor_de_cursos  
    for curso in gestor_de_cursos.cursos:  
        if curso.horas_duracion>mayor_horas:  
            mayor_horas=curso.horas_duracion  
            curso_mayor_horas=curso  
    print("El curso de mayor duración es ", curso_mayor_horas)  
  
#Paso 5.4  
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
  
  
#Paso 4  
def pedir_opcion_y_ejecutar():  
    opcion=input("ingrese la opcion seleccionada: ")  
    if opcion=="1":  
        cargar_cursos()  
    elif opcion=="2":  
        mostrar_todos_los_cursos()  
    elif opcion=="3":  
        mostrar_curso_de_mayor_duracion()  
    elif opcion=="4":  
        buscar_curso_por_codigo_y_mostrar_categoria()  
    elif opcion=="5":  
        print("Muchas gracias por usar el programa.")  
    else:  
        print("La opción ingresada no es válida")
```

