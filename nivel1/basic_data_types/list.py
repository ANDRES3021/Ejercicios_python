if __name__ == '__main__':
    N = int(input())
    list = []
    for datos in range(N):
        comando = input().split()
        if comando[0] == 'insert':
            list.insert(int(comando[1]), int(comando[2]))
        elif comando[0] == 'print':
            print(list)
        elif comando[0] == 'remove':
            list.remove(int(comando[1]))
        elif comando[0] == 'append':
            list.append(int(comando[1]))
        elif comando[0] == 'sort':
            list.sort()
        elif comando[0] == 'pop':
            list.pop()
        elif comando[0] == 'reverse':
            list.reverse()

