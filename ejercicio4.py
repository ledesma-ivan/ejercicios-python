sueldo = int(input("Cuanto es tu sueldo: ? "))

if sueldo > 3000:
    print('Debe pagar impuestos')

# B
num = int(input("Ingrese un numero: "))

num1 = int(input("Ingrese otro numero: "))

if num > num1:
    print('El numero mayor es:', num)
else:
    print('El numero mayor es:', num1)

# C 
uno_numero = int(input("Ingrese un numero: "))
dos_numero = int(input("Ingrese otro numero: "))

if uno_numero > dos_numero:
    print('La suma de los numeros es:', uno_numero + dos_numero + ' ', + 'Y su diferencia es: ', uno_numero - dos_numero)
else:
    print('El productos de los dos numeros es:', uno_numero * dos_numero + ' ', + 'Y su division de los numeros es: ', dos_numero - uno_numero)


nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print('Promocionado')
else:
    print('No promocionado')


num_1 = int(input("Ingrese un numero: "))

if len(num_1 == 1):
    print('El numero tiene un digito')
elif len(num_1 == 2):
    print('El numero tiene dos digitos')
else:
    print('El numero tiene mas de dos digitos')