# Una empresa comercializa 10 artículos en 3 sucursales.
# Se debe realizar un programa que permita gestionar el inventario y el stock por sucursal para dicha empresa.
# Para ello se solicita que el programa posea un menú con las siguientes opciones:
#
# A) Gestión de sucursales. CRUD considerando que toda sucursal tiene un código único (entero), un nombre y una dirección.
# B) Gestión de artículos. CRUD considerando que todo artículo tiene un código único (entero),
# un nombre, una categoría y una descripción.
# C) Carga de stock: se registrará el ingreso en depósito de la cantidad de un determinado artículo en una sucursal.
# D) Venta de artículos:
# se registran las ventas realizadas informando sucursal, artículo y cantidad vendida. 
# Se debe verificar que la cantidad vendida no exceda el stock de ese producto en esa sucursal,
# informando si la venta no se puede realizar por este motivo
# E) Existencia de mercaderías: listar por pantalla cantidad existentes de mercaderías por sucursal
# F) Salir del programa

# Var
MAX_SUCURSAL = 3
MAX_PRODUCTO = 3

# Lists
ls_sucursal = []
ls_producto = []


class Sucursal:
    def __init__(self, suc_ref, suc_name, suc_address):
        self.suc_ref = suc_ref
        self.suc_name = suc_name
        self.suc_address = suc_address

    def sucursalStock():

    def atributos(self):
        print(f'Codigo de sucursal: {self.suc_ref}')
        print(f'Nombre de sucursal: {self.suc_name}')
        print(f'Direccion de sucursal: {self.suc_address}')


class Producto:
    def __init__(self, pro_ref, pro_name, pro_precio: int, pro_des, pro_stock: int):
        self.pro_ref = pro_ref
        self.pro_name = pro_name
        self.pro_precio = pro_precio
        self.pro_des = pro_des

    def stockSucursal(self, name_sucursal, stock_sucursal):
        self.name_sucursal = name_sucursal = []
        self.stock_sucursal = stock_sucursal = []

    def atributosProduct(self):
        print(f'Codigo de producto: {self.pro_ref}')
        print(f'Nombre de producto: {self.pro_name}')
        print(f'Precio del Producto: {self.pro_precio}')
        print(f'Descripcion del Producto: {self.pro_des}')
        print(f'Stock del Producto: {self.pro_stock}')


print("Crear sucursal")


def createSucursal():
    for i in range(MAX_SUCURSAL):
        ref_s = i + 1
        name_s = input(f'Ingrese nombre de la sucursal {i + 1}:\n')
        suc_address = input(f'Ingrese direccion de la sucursal {i + 1}:\n')
        new_sucursal = Sucursal(ref_s, name_s, suc_address)
        ls_sucursal.append(new_sucursal)


def imprimirObjetos():
    for sucursal in ls_sucursal:
        Sucursal.atributos(sucursal)


def buscarSucursal():
    user = input('Introduzca el nombre de la sucursal')
    for sucursal in ls_sucursal:
        print(sucursal)
        if user == sucursal.suc_name:
            print('Su sucursal es:')
            Sucursal.atributos(sucursal)
            return sucursal
    print('Su sucursal no ha sido encontrada, intente nuevamente...')


def editarSucursal():
    edit_s = buscarSucursal()
    print(edit_s)
    print('Que desea modificar ?')
    print('1. Nombre de Sucursal')
    print('2. Direccion de la Sucursal')
    number_e = int(input('Ingrese el la Opcion por numero: '))
    if number_e == 1:
        new_s_name = input('Ingrese el nuevo nombre de la sucursal: ')
        edit_s.suc_name = new_s_name

    elif number_e == 2:
        new_s_name = input('Ingrese la nueva direccion de la sucursal: ')
        edit_s.suc_address = new_s_name
    else:
        print('Hubo un problema con su opcion, intentelo nuevamente')


def eliminarSucursal():
    eliminar_s = buscarSucursal()
    ls_sucursal.remove(eliminar_s)


print('------------')


print('Crear Producto')


def createProduct():
    for i in range(MAX_PRODUCTO):
        ref = i + 1
        name = input(f'Ingrese el nombre del Producto {ref}: ')
        precio = int(input(f'Ingrese el precio del Producto {ref}: '))
        des = input(f'Ingrese la descripción del Producto {ref}: ')
        stock = int(input(f'Ingrese el stock del Producto {ref}: '))
        new_product = Producto(ref, name, precio, des, stock)
        ls_producto.append(new_product)
        for i in ls_sucursal:
            new_product.stockSucursal(i.suc_name, 0)

        print(f'Se ingresaron {len(ls_producto)} productos')


def buscarProducto():
    print('Busqueda de producto')
    user_search = input('Ingresa el producto nombre del producto: ')
    user_search.lower()
    for producto in ls_producto:
        if user_search == producto.pro_name.lower():
            print('SU PRODUCTO FUE ENCONTRADO Y ES: ')
            Producto.atributosProduct(producto)
            return producto
    print('Su producto no fue encontrado, intente nuevamente')


def cargarStock():
    sucursal = buscarSucursal()
    producto = buscarProducto()
    carga_stock = int(input('Ingrese la cantidad que desea cargar: '))
    producto.stockSucursal(sucursal, cargarStock)





#def editProduc():










