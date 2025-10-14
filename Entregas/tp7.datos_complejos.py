# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
precio_actualizado = precios_frutas
print(f"Los precios actualizados son: {precio_actualizado}")

# Ejercicio 3
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2330
}
frutas = list(precios_frutas.keys())
print(frutas)

# Ejercicio 4
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

buscar_contacto = input("Ingrese el nombre del contacto que desea buscar: ")
if buscar_contacto in contactos:
    print(f"El número de {buscar_contacto} es: {contactos[buscar_contacto]}")
else:
    print("El nombre ingresado no pertenece a sus contactos")

# Ejercicio 5
frase = input("Ingresa una frase: ")
palabras = frase.lower().split()

palabras_unicas = set(palabras)

recuento_palabras = {}
for palabra in palabras:
    if palabra in recuento_palabras:
        recuento_palabras[palabra] += 1
    else:
        recuento_palabras[palabra] = 1

print(f"\nPalabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento_palabras}")

# Ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es de {promedio:.2f}")

# Ejercicio 7
parcial1 = {'Ana', 'Melina', 'Xiomara', 'Gustavo'}
parcial2 = {'Lara', 'Ana', 'Aldana', 'Gustavo'}

ambos = parcial1 & parcial2
print(f"Aprobaron ambos parciales: {ambos}")

solo_uno = parcial1 ^ parcial2
print(f"Aprobaron solo un parcial: {solo_uno}")

uno_de_dos = parcial1 | parcial2
print(f"Aprobaron al menos un parcial: {uno_de_dos}")

# Ejercicio 8
stock = {
    'manzana': 50,
    'banana': 30,
    'pera': 20
}

producto = input("Ingrese el nombre del producto: ").lower()

if producto in stock:
    print(f"El stock actual de {producto} es {stock[producto]}")
    agregar = int(input("¿Cuántas unidades desea agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingrese el stock inicial: "))
    stock[producto] = nuevo_stock

print("\nStock actualizado:")
for prod, cant in stock.items():
    print(f"{prod}: {cant}")

# Ejercicio 9
agenda = {
    ('Lunes', '10:00'): 'Turno con el médico',
    ('Martes', '9:00'): 'Gym',
    ('Miércoles', '14:00'): 'Clase de programación',
    ('Jueves', '16:00'): 'Merienda con Ana',
    ('Viernes', '21:00'): 'Cumpleaños de Vale'
}

dia = input("¿Qué día de la agenda desea consultar? ").capitalize()

eventos_en_dia = [evento for (d, hora), evento in agenda.items() if d == dia]

if eventos_en_dia:
    print(f"Eventos programados para {dia}:")
    for evento in eventos_en_dia:
        print(f"- {evento}")
else:
    print(f"No tenés eventos programados para el día {dia}.")

# Ejercicio 10
original = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia'}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print(invertido)
