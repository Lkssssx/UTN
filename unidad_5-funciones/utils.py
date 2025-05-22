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

def sucesion_simbolos(simbolo, veces):
    sucesion = ""
    for i in range(veces):
        sucesion += simbolo # sucesion = sucesion + simbolo
    return sucesion

def imprimir_simbolo(simbolo, veces):
    print(sucesion_simbolos(simbolo,veces))

