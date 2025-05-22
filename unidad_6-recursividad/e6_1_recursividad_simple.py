import sys
sys.setrecursionlimit(20000)
# Definición de funciones
def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

def fact(x):
    return 1 if x == 0 else x * fact(x - 1)


# Programa principal

print(factorial(1500))
print(fact(1500))