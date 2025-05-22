"""
Realizar una función recursiva que reciva un número y una frase y la repita el numero de veces ingresado
"""

def repetir_frase(num, frase):
    if num >=1:
        print(frase)
        repetir_frase(num - 1, frase)


# Para que solo se ejecute si el archivo se llama igual que este archivo, y no cuando se importe a otros archivos:
if __name__ == "__main__":
    repetir_frase(3, "Hola Mundo")