'''
numero = int(input("Ingrese un numero: "))
numero1 = int(input("Ingrese otro numero: "))
numero2 = int(input("Ingrese otro numero: "))

if numero > numero1 and numero > numero2:
    print('El numero mayor es:', numero)
else:
    if numero1 > numero2:
        print('El numero mayor es:', numero1)
    else:
        print('El numero mayor es:', numero2)


dia = input("Ingrese un dia de la semana: ")
mes = input("Ingrese un mes del año: ")
ano = int(input("Ingrese un año: "))

if mes == 1 or mes == 2 or mes == 3:
    print('Corresponde al primer trimestre')

dia = input("Ingrese un dia del mes: ")
mes = input("Ingrese un mes del año: ")

if dia == '25' and mes == 'Diciembre':
    print('Es Navidad')
else:
    print('No es Navidad :(')


numero = int(input("Ingrese un numero: "))
numero_1 = int(input("Ingrese otro numero: "))
numero_2 = int(input("Ingrese otro numero: "))

if numero < 9 or numero_1 < 9 or numero_2 < 9:
    print('Alguno de los numeros es menor a 9')



numero = int(input("Ingrese un numero: "))
numero_1 = int(input("Ingrese otro numero: "))
numero_2 = int(input("Ingrese otro numero: "))

if numero == numero_1 and numero == numero_2:
    resultado = numero + numero_1 * numero_2
    print('El resultado es:', resultado)


coordenada_x = int(input("Ingrese una coordenada de un plano el x:  "))
coordenada_y = int(input("Ingrese una coordenada de un plano el y:  "))

if coordenada_x > coordenada_y and coordenada_x > 0:
    print('El punto se encuentra en el primer cuadrante')
else:
    if coordenada_x < 0 and coordenada_y > 0:
        print('El punto se encuentra en el segundo cuadrante')
    else:
        if coordenada_x < 0 and coordenada_y < 0:
            print('El punto se encuentra en el tercer cuadrante')
        else:
            if coordenada_x > 0 and coordenada_y < 0:
                print('El punto se encuentra en el cuarto cuadrante')
            else:
                print('El punto se encuentra en el origen')

sueldo = int(input("Ingrese su sueldo: "))
anos_de_antiguedad = int(input("Ingrese sus años de antiguedad: "))

if sueldo > 500 and anos_de_antiguedad >= 10:
    sueldo = sueldo + (sueldo * 0.20)
    print('Su nuevo sueldo es:', sueldo)

elif sueldo > 500 and anos_de_antiguedad < 10:
        sueldo = sueldo + (sueldo * 0.05)
        print('Su nuevo sueldo es:', sueldo)
        
elif sueldo < 500 and anos_de_antiguedad >= 10:
            sueldo = sueldo + (sueldo * 0.10)
            print('Su nuevo sueldo es:', sueldo)
else:
    if sueldo >= 500:
        print('Su nuevo sueldo es:', sueldo)
        print('No tiene aumento de sueldo')


'''

numero = int(input("Ingrese un numero: "))
numero_1 = int(input("Ingrese segundo numero: "))
numero_2 = int(input("Ingrese tercer numero: "))

maximo = numero
minimo = numero

# Con eso se evita el comparar el uno con todos en si xD
# Determinar el número máximo
if numero_1 > maximo:
    maximo = numero_1
elif numero_2 > maximo:
    maximo = numero_2

# Determinar el número mínimo
if numero_1 < minimo:
    minimo = numero_1
elif numero_2 < minimo:
    minimo = numero_2

# Calcular el rango
rango = maximo - minimo

# Mostrar los resultados
print("El número mayor es:", maximo)
print("El número menor es:", minimo)
print("El rango es:", rango)