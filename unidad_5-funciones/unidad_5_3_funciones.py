# Definición de funciones
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))

    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def obtener_resto(num1, num2):
    return num1 - num2 * (num1 // num2);

def es_multiplo(x,y):
    return obtener_resto(x,y) == 0;

def sumatoria_divisores_propios(num):
    sumatoria = 0
    for i in range(1, num // 2 + 1):
        if es_multiplo(num, i):
            sumatoria += i
    return sumatoria

def es_perfecto(num):
    return sumatoria_divisores_propios(num) == num

def informar_si_numero_es_perfecto(num):
    if es_perfecto(num):
        print(f"El número {num} es perfecto.")
    else:
        print(f"El número {num} no es perfecto.")




# Programa principal
num = leer_entero_validado("Ingresa un número natural", 1)
informar_si_numero_es_perfecto(num)