#ejercicio1
print("Hola mundo")

#ejercicio2
nombre =input("Ingrese su nombre ")
print(f"Hola {nombre}")

#ejercicio3
nombre = input("ingrese su nombre")
apellido= input("ingrese su apellido")
edad= input("ingrese su edad")
lugar= input("ingrese su lugar de residencia")
print (f"Hola me llamo {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

#ejercicio4

radio= float(input("ingrese el radio de la circunferencia "))
perimetro= 2 * 3.1416 * radio
area = 3.1416 * (radio ** 2)
print (f"el perimetro de la circunferencia es {perimetro} y el area es {area}")

#ejercicio5
segundos = float(input("Ingrese la cantidad de segundos"))
horas = segundos / 3600
print (f"La cantidad de segundos equivale a  {horas} horas")

#ejercicio6
numero = int(input("Ingrese un número "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

#ejercicio7
numero1= int(input("ingrese el primer número "))    
numero2= int(input("ingrese el segundo número "))
suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print ( f"la suma es {suma} , la resta es {resta} , la multiplicacion es {multiplicacion}, la division es {division}")

#ejercio8
peso= float(input("ingrese su peso"))
altura= float(input("ingrese su altura"))
imc = peso / (altura ** 2)
print (f"su indice de masa corporal es {imc}")

#ejercicio9
Celsius = float(input("ingrese la temperatura en grados Celsius"))
Fahrenheit = (Celsius * 9/5) + 32
print (f"la temperatura en grados Fahrenheit es {Fahrenheit}")

#ejercicio10

numero1= int(input("ingrese el primer número "))
numero2= int(input("ingrese el segundo número "))
numero3= int(input("ingrese el tercer número "))
promedio = (numero1 + numero2 + numero3) / 3
print (f"el promedio de los tres números es {promedio}")
