#Ejercicio1
contador=0
for i in range (0, 101):
    contador=contador +1  
    print(i)

#Ejercicio2
num= int(input("Ingrese un número entero: "))
cantidad_digitod= len(str(num))
print(f"El número {num} tiene {cantidad_digitod} digitos.")

#Ejercicio3
num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese otro número: "))

inicio=min(num1, num2) +1
fin=max(num1, num2)
suma=0
for i in range(inicio, fin):
    suma +=1
print(f" La suma entre los números {num1} y {num2} es :{suma}")

#Ejercicio4
suma= 0
while True:
 numero=int (int(input("Ingresa números enteros (Presiona 0 para terminar): ")))
 if numero== 0:
    break
 suma +=numero
print(f"El total acumulado es : {suma}")

#Ejercicio5
import random
num_aleatorio= random.randint (0,9)
intentos= 0
while True:
 intentos =int(input("Adivina el número (entre 0 y 9): "))
 intentos +=1
 if intentos==num_aleatorio :
  print(f"Correcto, adivinaste el número!")
  print(f"Lo hiciste en {intentos} intentos")
  break
 else:
  print("Incorrecto, intenta de nuevo")

#Ejercicio6

for i in range(100,1, -2):
 print(i)

#Ejercico7
num= int (input("Ingrese un número entero: "))
suma = 0
for i in range(num +1):
 suma += i
 print(f"La suma de los números comprendidos entre {num} y 0 es: {suma}")

#Ejercico8
pares=0
impares=0
positivos=0
negativos=0
for i in range(10):
  num= int(input(f"Ingrese el número {i+1}:  "))
  if num % 2==0:
    pares+=1
  else:
    impares +=1
  if num >= 0:
    positivos +=1
  else:
    negativos +=1
print(f"Hay {pares} números pares, {impares} números impares, {positivos} número positivos y {negativos} negativos.")

#Ejercicio9
suma=0
for i in range (10):
  num= int(input(f"Ingrese el número {i+1}:"))
  suma+=num
  media = suma/10
print(f"La media es de: {media}")

#Ejercicio10
num= int(input("Ingrese un número: "))
invertidor=0
while num > 0:
  digito= num % 10
  invertidor =invertidor * 10 + digito
  num //=10
  print(invertidor)