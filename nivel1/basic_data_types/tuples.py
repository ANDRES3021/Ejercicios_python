if __name__ == '__main__':
    n = int(input())
    tuplax = tuple(map(int, input().split()))
    tuplax = hash(tuplax)
    print(tuplax)
