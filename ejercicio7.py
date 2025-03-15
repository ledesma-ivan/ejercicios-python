'''
x = 1

while x<=100:
    print(x)
    x += 1
else:
    print('Fin del ciclo')


n = int(input('Ingrese un numero: '))

x = 1

while x <= n:
    print(x)
    x += 1
else:
    print('Fin del ciclo')



x = 1

suma = 0

while x <= 10:
    valor = int(input('Ingrese un numero: '))
    suma = suma + valor
    x += 1
promedio = suma / 10
print('La suma es:', suma)
print('El promedio es:', promedio)



x = 1

cantidad = 0

n = int(input('Ingrese un numero: '))

while x<=n:
    largo=float(input("Ingrese la medida de la pieza:"))
    if largo>=1.2 and largo<=1.3:
        cantidad=cantidad+1
    x=x+1
print("La cantidad de piezas aptas son")
print(cantidad)

''' 


'''
x = 0
n = int(input("Cuantas personas son del conjunto: "))
grupo_aprobado = 0
grupo_desaprobado = 0


while x<n:
    notas = int(input('Ingrese cada nota de cada alumno: '))
    if notas >= 7:
        grupo_aprobado += 1
    elif notas < 7:
        grupo_desaprobado += 1
    x += 1
    print('El grupo de aprobados es:', grupo_aprobado)
    print('El grupo de desaprobados es:', grupo_desaprobado)
    
 '''
'''  
n = int(input("Ingrese la cantidad de persona que hay: "))
total = 0
x = 0 
while x < n:
    altura = float(input("Ingrese la altura: "))
    total +=altura
    x +=1 
    print(total)
    if x == n:
        promedio = total / n
        print("El promedio de altura es: ", promedio)'


n = int(input("Ingrese la cantidad de empleados que hay: "))
x = 0
total = 0
sueldo_pro = 0
sueldo_promedio = 0
total = 0 
while x < n:
    sueldo = int(input("Ingrese el sueldo del empleado: "))
    if sueldo < 100:
        print("El sueldo debe ser mayor a 100")
    elif sueldo >= 100:
        if sueldo >= 100 and sueldo <=300:
            sueldo_promedio+=1
            total += sueldo
        elif sueldo >300:
            sueldo_pro+=1
            total += sueldo
    x += 1
print(f'La cantidad de empleados que cobra entre 100 y 300 es: {sueldo_promedio} y la cantidad de empleados que cobran sueldo mas de 300 es: {sueldo_pro}')
print("La cantidad de sueldo gastado en el personal es:", total)

'''
"""
Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)

"""
"""
for i in range(11, 500, 11):
    print(i, end= " ")
""" 
"""
Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
"""

for i in range(8, 501, 8):
    print(i, end= " ")

"""
Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""

lista = []

lista_1 = []



for valor in range(0, 15): 
    valor = int(input("Ingrese un numero: "))
    lista.append(valor)

if len(lista) == 15:
    for valor_1 in range(0, 15):
        valor = int(input("Ingrese un numero: "))
        lista_1.append(valor)

suma_de_lista = sum(lista)
print("La suma de la lista es: ", suma_de_lista)

suma_de_lista_1 = sum(lista_1)
print("La suma de la lista_1 es: ", suma_de_lista_1)


if suma_de_lista > suma_de_lista_1:
    print("Lista 1 mayor", sum(lista))
elif suma_de_lista_1 > suma_de_lista:
    print("Lista 2 mayor", sum(lista_1))
else:
    print("La listas son iguales")



"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
"""

# El == se usa como condicional para ver si es da un numero par sera verdadero
n = int(input('Ingrese la cantidad de numeros que desea carga: '))

x = 0

par = 0

impar = 0

while x < n:
    numero = int(input("Ingrese un numero entero: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar+= 1
    print(f"La cantidad de numeros pares son {par} y la cantidad de numeros impar son {impar}")
    x+=1
