#Ejercicio 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def mostrar_factoriales(hasta):
    for i in range (1, hasta + 1):
        print(f"{i}= {factorial(i)}")

numero= int(input("Ingrese un número positivo entero: "))
mostrar_factoriales(numero)


#Ejercicio 2
def fibonacci(n):
   if n == 0 or n == 1:
    return n
   else:
    return fibonacci(n - 1) + fibonacci(n - 2)
   
def mostrar_fibonacci(hasta):
   for i in range( hasta +1):
      print(f"F({i})= {fibonacci(i)}")
pos= int(input("Ingrese la posición de Fibonacci: "))
mostrar_factoriales(pos)


#Ejercicio 3
def potencia(n, m):
   if m == 0 :
      return 1
   return n*potencia(n,m-1)
base= int(input("Base: "))
exp=int(input("Exponente: "))
print(f"{base}^{exp}={potencia(base,exp)}")

#Ejercicio 4
def decimal_a_binario(n):
   if n<2:
      return str(n)
   return decimal_a_binario(n//2) +str(n % 2)
num=int(input("Número decimal: "))
print("Binario:", decimal_a_binario(num))

#Ejercicio 5
def palindromo(palabra):
   if len(palabra) <=1:
      return True
   if palabra[0] !=palabra[-1]:
      return False
texto=input("Ingrese una palabra: ")
print( palindromo(texto))


#Ejercicio 6
def suma_digito(n):
   if n<10:
      return n
   return (n % 10)+ suma_digito(n//10)
print(suma_digito(1234))
print(suma_digito(305))
print(suma_digito(9))


#Ejercicio 7
def contar_bloques(n):
   if n==0:
      return 1
   return n + contar_bloques(n-1)
print(contar_bloques(5))

#Ejercicio 8
def contar_digito(numero, digito):
   if numero < 10:
      return 1 if numero == digito else 0
   ultimo = numero % 10 
   resto = numero // 10

   if ultimo== digito:
      return 1+ contar_digito(resto, digito)
   else:
      return contar_digito(resto, digito)
print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))

"""Para poder resolver los ejercicos de recursividad comence siempre definiendo una funcion, luego se presente el caso base que es la condicion que define la recursion, 
para luego seguir  con el paso recursivo que es donde la funcion se llama a si misma. Estos pasos se emplearon en todos los ejercicios, ya que es la manera correcta de trabajar con la tecnica de recursividad"""