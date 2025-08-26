#Ejercicio1
edad= int(input("ingrese su edad ")) 
if edad >= 18  :
 print("Eres mayor de edad")

#Ejercicio2
nota= int(input("Ingrese su nota "))
if nota >=6 :
 print("Aprobado")
else :
 print ("Desaprobado")
 
#Ejercicio3
numero= int(input("Ingrese un numero "))
if numero % 2 == 0:
 print("El numero ingresado es par")
else:
 print("El numero ingresa es impar")

#Ejercicio4
edad= int(input("Ingrese su edad "))
if edad < 12 :
 print("Niña/o")
elif edad >= 12 and edad < 18:
 print("Adolescente")
elif edad >= 18 and edad < 30 :
 print ("Adulto a joven")
elif edad >= 30:
 print("Adulto")

# Ejercicio5
Contraseña= input("Ingrese una contraseña de entre 8 y 14 caracteres ")
if 8<= len(Contraseña) <=14:
 print("Ha ingresado la contraseña correcta")
else:
 print("Por favor, ingrese una contraseña de 8 y 14 caracteres") 


#ejercicio6
import random
from statistics import mode, median, mean
import statistics 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo o a la derecha"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo o a la izquierda"
else:
    sesgo = "Sin sesgo"

print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")
print(f"El sesgo de la distribución es: {sesgo}")

#Ejercicio7
lista= input("Ingrese una frase o palabra")
vocal="aeiouAEIOU"
if lista and lista[-1] in vocal:
  lista_modificada = lista +"!"
  print (lista_modificada)
else :
  print(lista)

#Ejercicio8
nombre= input("ingrese su nombre ")
print("\nSelecciona una opción para tu nombre:")
print("1. Todo el nombre en mayuscula ")
print("2. Todo el nombre en minuscula ")
print("3. Solo la primera letra en mayúscula")
opcion = input("Ingresa el número de la opción (1, 2 o 3): ")
if opcion == '1':
    nombre_transformado = nombre.upper() 
    print("\nNombre en mayúsculas:", nombre_transformado)
elif opcion == '2':
    nombre_transformado = nombre.lower()  
    print("\nNombre en minúsculas:", nombre_transformado)
elif opcion == '3':
    nombre_transformado = nombre.title() 
    print("\nNombre con la primera letra mayúscula:", nombre_transformado)
else:
    print("\nOpción no válida. Por favor, ingresa 1, 2 o 3.")

#Ejercicio9
magnitud= int(input("Ingrese la magnitud de su terreno "))
if magnitud < 3 :
  print ("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4 :
  print("Leve, (ligeramente perceptible)")
elif magnitud >=4 and magnitud < 5 :
 print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud < 6:
  print("Fuerte (puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
 print("Muy fuerte (puede causar daños significativos)")
elif magnitud >= 7:
  print ("Extremo (puede causar graves daños a gran escala)")

#Ejercicio10
def estacion_anio(hemisferio, mes, dia):
   
    hemisferio = hemisferio.upper()
    mes = mes.lower()

    meses = {
        "enero": 1, "febrero": 2, "marzo": 3,
        "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9,
        "octubre": 10, "noviembre": 11, "diciembre": 12
    }

    m = meses[mes]

    if (m == 12 and dia >= 21) or (m in [1, 2]) or (m == 3 and dia <= 20):
        estacion_norte = "Invierno"
    elif (m == 3 and dia >= 21) or (m in [4, 5]) or (m == 6 and dia <= 20):
        estacion_norte = "Primavera"
    elif (m == 6 and dia >= 21) or (m in [7, 8]) or (m == 9 and dia <= 20):
        estacion_norte = "Verano"
    else:
        estacion_norte = "Otoño"


    if estacion_norte == "Invierno":
        estacion_sur = "Verano"
    elif estacion_norte == "Verano":
        estacion_sur = "Invierno"
    elif estacion_norte == "Primavera":
        estacion_sur = "Otoño"
    else:
        estacion_sur = "Primavera"


    if hemisferio == "N":
        return estacion_norte
    elif hemisferio == "S":
        return estacion_sur
    else:
        return "Hemisferio inválido."



hemisferio = input("¿En qué hemisferio estás? (N/S): ")
mes = input("¿En qué mes estamos? : ")
dia = int(input("¿Qué día del mes es?: "))

print("La estación es:", estacion_anio(hemisferio, mes, dia))
