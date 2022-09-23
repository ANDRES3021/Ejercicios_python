# def imprimir_mensaje():
#     print('mensaje especial')
#     print('estoy aprendiendo a usar funciones')


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print('hola')
    print('como estas?')
    print(mensaje)
    print('adios')

opcion = int(input("elije un opcion (1, 2, 3): "))
if opcion == 1:
    conversacion('elegiste a opcion 1')
elif opcion == 2:
    conversacion('elegiste a opcion 2')
elif opcion == 3:
    conversacion('elegiste a opcion 3')
else:
    print('escribe la opcion correcta')
