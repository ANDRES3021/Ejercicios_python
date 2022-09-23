def run():
    # for count in range(1000):
    #     if count % 2 != 0:
    #         continue
    #     print(count)

    #     for i in range (0, 10000):
    #         print(i)
    #         if i == 5678:
    #             break

    texto = input('Escribe un texto: ')
    for letter in texto:
        if letter == 'o':
            break
        print(letter)


if __name__ == '__main__':
    run()