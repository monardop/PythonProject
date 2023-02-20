def nearestMult(num: int) -> int:
    while True:
        if num % 5 != 0:
            num += 1
        else: 
            return num

def gradingStudents(grades):
    # Write your code here
    final_grades = []
    for n in grades:
        if n < 38:
            final_grades.append(n)
        else:
            nearest = nearestMult(n)
            if nearest - n < 3:
                final_grades.append(nearest)
            else:
                final_grades.append(n)
    return final_grades

print(gradingStudents([73,67,38,33]))
  
