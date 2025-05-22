"""
Realizar la suma de los primeros n valores positivos de forma recursiva
"""

def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num - 1)

# Para que solo se ejecute si el archivo se llama igual que este archivo, y no cuando se importe a otros archivos:
if __name__ == "__main__":
    print(suma_recursiva(3))