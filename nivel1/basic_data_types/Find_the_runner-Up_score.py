if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    conjunto = set(arr)
    maximo = max(conjunto)
    conjunto.discard(maximo)
    sub_campeon = max(conjunto)
    print(conjunto)

    