"""En este ejercicio se trabaja con tres parametros y se usa list comprenhentions 
para imprimir listas anidadas de las posibles comobinaciones entre x, y, z 
cuya suma sea diferente a n """


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    resultado = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(resultado)
