'''
nota_1 = int(input("Ingrese la primera nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercera nota: "))

promedio = (nota_1 + nota_2 + nota_3) / 3

if promedio >= 7:
    print('Promocionado')
else:   
    if promedio >= 4:
        print('Regular')
    else:
        print('Reprobado')

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


numero = int(input("Ingrese un numero: "))

if numero < 0:
    print('Ingrese un numero positivo')
else:
    if len(numero) == 1:
        print('El numero tiene una cifra')
    elif len(numero) == 2:
        print('El numero tiene dos cifras')
    elif len(numero) == 3:
        print('El numero tiene tres cifras')
    else:
        print('El numero tiene mas de tres cifras')

'''

cantidad_preguntas = int(input("Ingrese la cantidad de preguntas: "))
cantidad_correctas = int(input("Ingrese la cantidad de preguntas correctas: "))

porcentaje = (cantidad_correctas * 100) / cantidad_preguntas

if porcentaje >= 90:
    print('Nivel maximo')
else:
    if porcentaje >= 75:
        print('Nivel medio')
    else:
        if porcentaje >= 50:
            print('Nivel regular')
        else:
            print('Fuera de nivel')


