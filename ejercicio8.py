# Realizar un programa que imprima en pantalla los números del 0 al 100
for x in range(101):
    print(x)

# Realizar un programa que imprima en pantalla los números del 20 al 30.
for x in range(20,31):
    print(x)


# Imprimir todos los números impares que hay entre 1 y 100.=
for x in range(1,100,2):
    print(x)

# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.
valores = []
for x in range(0, 10):
    n = int(input("Ingrese un valor: "))
    valores.append(n)

suma = sum(valores)
promedio = suma / 10
print(f"La suma de los valores ingresados es: {suma}, y su promedio es {promedio}")

# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
notas = []

mayores_o_igual_7 = []
menores_7 = []

for x in range(0, 10):
    n = int(input("Ingrese la nota del alumno: "))
    if n >= 7:
        mayores_o_igual_7.append(n)
    else:
        menores_7.append(n)

cantidad_pro = len(mayores_o_igual_7)
cantidad_no_pro = len(menores_7)
print(f"La cantidad de alumnos con notas mayores o iguales a 7 es: {cantidad_pro} y la cantidad de alumnos con notas menores a 7 es: {cantidad_no_pro}")


# Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
# Para que sea multiplo el residuo debe ser 0 
multiplo_3 = []
multiplo_de_5 = []
multiplo_3_5 = []

for x in range(0, 10):
    n = int(input("Ingrese un numero: "))
    if n % 3 == 0 and n % 5 == 0:
        multiplo_3_5.append(n)
    elif n % 3 == 0:
        multiplo_3.append(n)
    elif n % 5 == 0:
        multiplo_de_5.append(n)
    else:
        print('El numero no es multiplo ni de 3 ni de 5.')

cantidad_multiplo_3 = len(multiplo_3)
cantidad_multiplo_5 = len(multiplo_de_5)
cantidad_multiplo_3_5 = len(multiplo_3_5)

print(f"Cantidad de multiplo de 3 es: {cantidad_multiplo_3} y la cantidad de multiplo de 5 es: {cantidad_multiplo_5} y la cantidad de valores es multiplos de los dos es {cantidad_multiplo_3_5}")


"""
Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)
Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. Lo primero que se hace es cargar una variable que indique la cantidad de valores a ingresar.
Dicha variable se carga antes de entrar a la estructura repetitiva for.
"""

# En este caso no pide usar listas, si bien es una opcion viable habra que analizar el costo computacional.


cantidad = int(input("Ingrese la cantidad de valores a ingresar: "))

valores_igual_mayor_mil = 0

for cantidad in range(0, cantidad):
    n = int(input("Ingrese un valor: "))
    if n >= 1000:
        cantidad+=1

print('La cantidad total de numeros ingresados que son mayor o igual a mil es', cantidad)


"""
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12.
"""
cantidad = int(input("Ingrese la cantidad de triangulos que tenes"))
superfie_mayor_12 = 0

for x in range(0, cantidad):
    base = int(input("Ingrese la base del triangulo: " ))
    altura = int(input("Ingrese la altura"))
    superficie = base * altura / 2
    print('La base es', base)
    print('La altura es', altura)
    print('La superfie es', superficie)

    if superficie > 12:
        superfie_mayor_12 +=1
print('La la cantidad de triangules cuya superficies es mayor a 12: ', superficie)

# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
ultimos_5 = []

for n in range(0, 10):
    if n > 5:
        numero = int(input("Ingrese un numero: "))
        ultimos_5.append(numero)

suma_ultimos_5 = sum(ultimos_5)
print("La suma de los ultimos 5 valores ingresados es: ", suma_ultimos_5)

# Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)

print("Bienvenido a la tabla de multiplicar")
for x in range(11):
    tabla = 5
    resultado = 5 * x
    print(resultado)

# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

n = int(input("Ingrese el valor de la tabla a multiplicar: "))

for x in range(13):
    resultado = n * x
    print(resultado)


"""
Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
"""

n = int(input("Ingrese cuantos triangulos tenes: "))
equilátero = 0
isosceles = 0 
escaleno = 0

for n in range(0, n+1):
    lado_1 = int(input("Ingrese el lado 1: "))
    lado_2 = int(input("Ingrese el lado 2: "))
    lado_3 = int(input("Ingrese el lado 3: "))

    if lado_1 == lado_2 and lado_1 == lado_3:
        print("Los tres lados son iguales")
        equilátero+=1
    elif lado_1 == lado_2 or lado_1 == lado_3:
        print("El triangulo es isosceles")
        isosceles+=1
    else:
        print("Ningun lado es igual")
        escaleno+=1
 
print(f"La cantidad de triagulos que son equilateros, {equilátero}, y isosceles {isosceles}, y lo que son escaleno {escaleno}")

"""
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
"""


"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
"""
valores_positivos = 0
valores_negativos = 0
multiplos_15 = 0
numeros_pares = []

for x in range(10):
    n = input("Ingrese un valor: ")
    



"""
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
"""

