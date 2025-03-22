# Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con mayor altura.
nombres = []

for x in range(2):
    nombre = input("Ingrese un nombre")
    nombres.append(nombre)

orden_avanzando = nombres.sort()

print("El orden de los nombres ingresados es: ", orden_avanzando)

# Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente o si son iguales.

"""
Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados.
"""
# Mas optima.
opcion="si"
suma=0
while opcion=="si":
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    opcion=input("Desea cargar otro numero (si/no):")
print("La suma de valores ingresados es")
print(suma)


"""
Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados en forma alfabética.
"""
nombres = []

for x in range(2):
    nombre = input("Ingrese un nombre")
    nombres.append(nombre)

orden_avanzando = nombres.sort()

print("El orden de los nombres ingresados es: ", orden_avanzando)