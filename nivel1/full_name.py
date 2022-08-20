#!/usr/bin/python3
"""funcion que recibe como parametro el nombre 
y el apellido y los muestra por pantalla"""

def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    