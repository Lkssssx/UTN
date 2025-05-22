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


def es_primo(num):
    cont = 2;
    mitad = num // 2
    while cont <= mitad and not es_multiplo(num, cont):
        cont += 1;
    return cont > mitad

def informar_si_numero_es_primo(num):
    if es_primo(num):
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")


# Programa Principal
num = leer_entero_validado("Ingresa un número natural", 1)
informar_si_numero_es_primo(num)