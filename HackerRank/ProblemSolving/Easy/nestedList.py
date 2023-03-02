"""
Given the names and grades for each student in a class of  students,
 store them in a nested list and print the name(s) of any student(s) 
 having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    students = [] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])
    students = sorted(students)
    selected = []
    second_grade = 0
    for n in students:
        if n[0] == students[0][0]:
            pass
        else: 
            second_grade = n[0]
            break
    for n in students:
        if n[0] == second_grade:
            selected.append(n[1])
    for n in sorted(selected):
        print(n)
