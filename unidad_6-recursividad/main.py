from e6_4_suma_n_valores import suma_recursiva as sum_n
from e6_5_fibonacci import fibonacci_recursivo as fibonacci
from e6_7_funcion_laberinto import resolver_laberinto
"""

num = int(input("Ingrese un número positivo: "))


print(sum_n(num))


for i in range(num + 1):
    print(f"En la posicion {i} obtenemos el valor de fibonacci: {fibonacci(i)}")

"""

laberinto = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],  # Meta en (8, 7)
]


camino = []

resolver_laberinto(laberinto, 0, 0, camino)

print(camino)
