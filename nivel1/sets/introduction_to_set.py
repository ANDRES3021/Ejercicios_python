def average(array):
    conjunto = set(array)
    denominador = len(conjunto)
    numerador = sum(conjunto)
    promedio = numerador/denominador
    return(promedio)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)