def run():
    mi_dicccionario = {'llave1' : 1, 'llave2': 2, 'llave3' : 3}
    print(mi_dicccionario['llave1'])

    for llaves in mi_dicccionario.keys():
        print(llaves)
    
    for numero in mi_dicccionario.values():
        print(numero)

    for llaves, numero in mi_dicccionario.items():
        print(llaves + ' tiene ' + str(numero))
if __name__ == '__main__':
    run()
