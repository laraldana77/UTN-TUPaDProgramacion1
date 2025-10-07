#Ejercicio1
def imprimir_hola_mundo():
    print(f"Hola mundo!")
imprimir_hola_mundo()

#Ejercicio2
def saludar_usuario(nombre):
    return f"Hola,{nombre}!"
nombre=input("Ingrese su nombre:")
saludo= saludar_usuario(nombre)
print(saludo )

#Ejercicio3
def informacion_personal(nombre, apellido,edad, residencia):
    return f"Hola soy {nombre} {apellido}, tengo {edad}, y vivo en {residencia}"
nombre= input("Ingrese su nombre:")
apellido= input("Ingrese su apellido:")
edad=int(input("Ingrese su edad: "))
residencia=input("ingrese el lugar donde vive:")
datos=informacion_personal(nombre,apellido,edad,residencia)
print(datos)

#Ejercicio4
import math
def calcular_area(radio):
    return math.pi*(radio**2)
def calcular_perimetro(radio):
    return 2*math.pi*radio
radio=float(input("Ingrese el radio del circulo: "))
resultado_area=calcular_area(radio)
resultado_perimetro=calcular_perimetro(radio)
print (f"El area del circulo es :{resultado_area}")
print(f"El perimetro del circulo es: {resultado_perimetro}")

#Ejercicio5
def segundos_a_horas(segundos):
    horas= segundos/3600
    return horas
seg=int(input("Ingrese  cantidad de segundos:"))
horas=segundos_a_horas(seg)
print(f"{seg} segundos son equivalentes a {horas:.2f} horas")


#Ejercicio6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print (f"{numero} * {i}= {numero * i}")
num=int(input(f"Ingrese un número: "))
tabla_multiplicar(num)

#Ejercicio7

def operacion_basica(a, b):   
 return(suma, resta, multiplicacion, division)
a= int(input(f"Ingrese el primer número: "))
b=int(input(f"Ingrese el segundo número:"))
suma = a+b
resta = a-b
multiplicacion =a*b
division =a/b
resultados= operacion_basica(a,b)
print(f"Suma: {suma}")
print(f"Resta :{resta}")
print(f"Multiplicación:{multiplicacion}")
print(f"División:{division}")

#Ejercicio8
def calcular_imc(peso, altura):
    imc= peso/ (altura**2)
    return round(imc, 2)
peso=float(input(f"Ingrese su peso: "))
altura=float(input(f"Ingreese su altura: "))
imc=calcular_imc(peso, altura)
print(f"Su indice de masa corporal es de: {imc}")

#Ejercicio9
def celsius_a_fahrenheit(celsius) :
    return (celsius * 9/5)+32
celsius=float(input("Ingrese la temperatura en grados celsius:"))
fahrenheit=celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit} °F")

#Ejercicio10
def calcular_promedio(a,b,c):
    return a + b + c /3
a = float(input("Ingrese el primer valor: "))
b= float(input("Ingrese el segundo valor: "))
c=float(input("Ingrese el primer valor: "))
promedio=calcular_promedio(a,b,c)
print(f"El promedio es de {promedio:.2f}")