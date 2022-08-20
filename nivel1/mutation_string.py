#!/usr/bin/python3
"""cambiar la letra de un string por medio 
de una funcion que recibe el string la posicion 
y la letra a cambiar"""
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return(string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    