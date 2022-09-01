if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *nota = input().split()
        scores = list(map(float, nota))
        student_marks[name] = scores
    
    query_name = input()
    divisor = (len(scores))
    suma = float(sum(student_marks[query_name]))
    promedio = suma/divisor
    print("%.2f"%promedio)
