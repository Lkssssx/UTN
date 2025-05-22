"""
Calcula el valor de Fibonacci en la posicion dada de forma recursiva.

:param pos: posicion en la secuencia de Fibonacci (debe ser >= 0).
:return: Valor de Fibonnaci en la posicion indicada.
"""

# 0 1 1 2 3 5 8 11
def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion-2)
    
if __name__ == "__main__":
    print(fibonacci_recursivo(4))