import os
def mostrar_producto():
    if not os.path.exists("Productos.txt"):
        print("No existe 'Productos.txt'")
        return
    
    with open("Productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}")


def agregar_productos():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input(f"Ingrese el precio de {nombre}: ")
    cantidad = input(f"Ingrese la cantidad de {nombre}: ")

    with open("Productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print("Producto agregado con éxito\n")


def cargar_producto_en_lista():
    productos = []

    if not os.path.exists("Productos.txt"):
        print("No existe 'Productos.txt'")
        return []

    with open("Productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos.append(producto)
    
    print("Productos cargados con éxito")
    return productos


def buscar_producto(productos):
    if len(productos) == 0:
        print("No hay productos en la lista. Debe cargar el primer producto.")
        return

    nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ").lower()
    encontrado = False

    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


def reescribir_archivo(productos):
    if len(productos) == 0:
        print("No hay productos encontrados. Debe cargarlos primero.")
        return

    with open("Productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    
    print("Archivo reescrito con éxito.")
