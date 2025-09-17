#Ejercicio1
notas=[7,8,9,6,10,4,7,8,9,7]
print(notas)
for i in range(10):
    print(notas[i])
    print(i)
suma=0
for nota in notas:
    suma+=nota
promedio= suma/len(notas)
print(f"El promedio de notas es :{promedio}")
minima=notas[0]
maxima=notas[0]
for notas in notas:
   if notas<minima:
      minima=notas
   if notas > maxima:
       maxima=notas
print(f"La nota mas baja es {minima} y la mas alta es:{maxima}")

#Ejercicio2
Productos=[]
for i in range(5):
    Producto=input(f"ingrese el producto{i+1}:")
    Productos.append(Producto)
print(Productos)
lista_ordenada= sorted(Productos)
print(lista_ordenada)
eliminado=input("Que producto desea eliminar?")
if eliminado in Productos:
  Productos.remove(eliminado)
else:
  print("No existe este producto")
print(Productos)

#Ejercicio3
import random
numeros=[]
for i in range (15):
   n=random.randint(1,100)
   numeros.append(n)

pares=[]
impares=[]
for n in numeros:
   if n % 2==0:
      pares.append(n)
else:
    impares.append(n)

print(f"Numeros: {numeros}")
print(f"Los numeros pares son : {pares}")
print(f"los numeros impares son: {impares}")

#Ejercicio4
datos=[1,3,5,3,7,1,9,5,3]
sin_repetir=[]
for n in datos:
   if n not in sin_repetir:
    sin_repetir.append(n)
print(datos)
print(f"sin_repetir,{sin_repetir}")

#Ejercico5
asistencia=["Ana","Dante","Luca","Pedro","Lara","Soledad","Maria","Rosa"]
print("Lista inicial:")
print(asistencia)

while True:
    print("\nAsistencia actual:")
    for a in asistencia:
        print(a)

    opcion = input("\nDesea Agregar (A), Eliminar (E) o Salir (S)? ").upper()
    if opcion == "A":
        nuevo = input("Ingrese el nombre del nuevo estudiante: ")
        asistencia.append(nuevo)
        print(f"{nuevo} fue agregado a la lista.")
    elif opcion == "E":
        eliminado = input("Ingrese el nombre que desea eliminar: ")
        if eliminado in asistencia:
            asistencia.remove(eliminado)
            print(f"{eliminado} fue eliminado de la lista.")
        else:
            print("El estudiante no existe en la lista.")
    elif opcion == "S":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")

#Ejercicio6
num=[1,2,3,4,5,6,7]
ultimo_num= num[-1]
resto=num[:len(num)-1]
print(ultimo_num)
print(resto)

nueva_lista=[ultimo_num]+resto
print(nueva_lista)

#Ejercicio7
dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
semana= [
   [7, 18],
   [9, 22],
   [8, 19],
   [10, 21],
   [6, 20],
   [5, 23],
   [7,21],
]
suma_min=0
suma_max=0
for fila in semana:
    suma_min+= fila[0] 
    suma_max += fila[1]
promedio_min= suma_min/7
promedio_max= suma_max/7

mayor_amplitud=-1
indice_mayor=-1
for i in range(7):
   min_dia=semana[i][0]
   max_dia=semana[i][1]

amplitud=max_dia-min_dia
if amplitud > mayor_amplitud:
   mayor_amplitud = amplitud
   indice_mayor=i
print(f"Matriz semana [min,max]:"(semana))
print(f"promedio minimo, {round(promedio_min,2)}")
print(f"promedio maximo, {round(promedio_max,2)}")
print(f"Mayor amplitud en : {dias[indice_mayor]}, con { mayor_amplitud}")
   

#Ejercicio8
estudiantes=["Ana","Carla","Maria","Bruno","Gabriel"]
materias=["biologia","historia","quimica"]
notas= [
   [8, 9, 7],
   [9,6,7],
   [4,7, 8],
   [9, 10,7],
   [6,9,8],

   ]
print("notas(fila=estudiantes,comlumna=materias)")
for i in range(len( estudiantes)):
 print(" ",estudiantes[i]+ ".",notas[i])


 print("\n promedio por estudianre")

for i in range(len(estudiantes)):
   suma=0
   for j in range(3):
      suma=notas[i][j]
      promedio=suma/3
      print("",estudiantes[i]+".", round(promedio,2))
   print("\n promedio por materia")

for j in range(3):
   suma=0
   for i in range(5):
      suma +=notas[i][j]
      promedio=suma/5
      print (" ", materias[j],+" ",round(promedio,2))

#Ejercicio9
Tablero=[]
for _ in range(3):
   fila=[]
   for _ in range(3):
       fila.append("_")
       Tablero.append(fila)
turno=0
jugador_actual="x"

while turno<9:
   print("\n tablero_actual")
   for f in range(3):
      print(Tablero[f][0], Tablero[f][-1], Tablero[f][2])
      print("\ Juega:", jugador_actual)
      fila_ing=int(input("Ingesa la fila (1-3):"))-1
      col_ing=int(input("Ingesa la columna (1-3):"))-1
      if fila_ing < 0 or fila_ing>2 or col_ing<0 or col_ing>2:
       print("Posicion fuera de rango. Intenta de nuevo")

#Ejercico10
ventas=[
   [1,4,5,6,7,8,7],
   [3,5,7,8,2,6,1],
   [9,5,7,1,2,3,4],
   [5,8,6,2,4,5,9]

]
mayor_ventas=-1
dia_mayor=-1
for j in range(7):
   total_dia=0
   for i in range(4):
      total_dia +=ventas[i][j]
      print(f"Total dia{j+i} : {total_dia}")
      if total_dia >mayor_ventas:
         mayor_ventas=total_dia
         dia_mayor=j
         print(f"El dia con mayor ventas fue: {dia_mayor+1}, con {mayor_ventas} ventas")

   mayor_producto=-1
   indice_producto=-1
   for i  in range(4):
      totatales_productos= suma(ventas[i])
      if totatales_productos > mayor_producto:
       mayor_producto= totatales_productos
      indice_producto=i
      print(f"El producto mas vendido {indice_producto+1} con {mayor_producto} ventas en la semana")
   


    


