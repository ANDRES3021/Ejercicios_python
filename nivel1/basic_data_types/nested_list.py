"""Ejercicio para guardar el nombre y calificacion 
de estudiantes y luego elegir la segunda mas baja"""
if __name__ == '__main__':
    nombre_calificacion = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        anidada = [name, score]
        nombre_calificacion.append(anidada)
        sorted_records = sorted(set([x[1] for x in nombre_calificacion]))
    segunda_nota = sorted_records[1]
    segundo = []
    for students in nombre_calificacion:
        if segunda_nota == students[1]:
            segundo.append(students[0])
    segundo.sort()
    for names in segundo:
        print(names) 

    
 
    