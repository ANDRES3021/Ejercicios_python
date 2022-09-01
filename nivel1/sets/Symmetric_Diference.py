if __name__ == '__main__':
    M = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    b = set(map(int, input().split()))
    primer = a.symmetric_difference(b)
    primer = sorted(primer)
    for items in primer:
        print(items)
