"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. 
Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el enunciado del problema."
"""
numeros_positivos = 0
while True:
    n = int(input("Ingrese un numero entero e ingrese -1 para finalizar:" ))
    if n < 0:
        print("Hasta aca llegaste, Don comediante")
        break
    numeros_positivos += n

print("La cantidad de los numeros positivos es: ", numeros_positivos)

""" 
Confeccionar un programa que solicite la carga de 10 valores reales por teclado.
Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre del programa, el programador y la fecha de la última modificación.
Utilizar el caracter # para los comentarios.
"""
# Carga de numeros enterenos por teclado.
# Programador: Ivan
# Ultima fecha de modificacion: 20/3/25
suma = 0
for x in range(10):
    n = float(input(f"Ingrese carga de valores reales"))
    suma += n
    
print("La suma de valores reales ingresados es: ", suma)