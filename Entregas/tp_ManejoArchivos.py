import utils
opcion="0"
productos= []
menu = [
    "\n === Gestor de Productos ===",
    "\n1. Mostrar productos",
    "2. Agregar productos",
    "3. Cargar productos en lista de diccionario",
    "4. Buscar producto",
    "5. Reescribir archivo",
    "6. Salir \n",
]
while opcion !="6":
    for item in menu:
        print(item)
    opcion =input("Ingrese una opcion (1-6):").strip()
    continue
match opcion:
    case "1":
        utils.mostrar_producto()
    case"2":
        utils.agregar_productos()
    case "3":
        productos = utils.cargar_producto_en_lista()
    case "4":
        utils.buscar_producto(productos)
    case "5":
        utils.reescribir_archivo(productos)
    case "6":
        print("Saliendo de gestor de productos")
    case _:
        print("Opcion fuera de rango, intente nuevamente")