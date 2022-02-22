from day24.classlib.student import Student

# 객체 리스트
student = [
    Student("지민", 3),
    Student("Elsa", 2),
    Student("슈가", 1)
]

print(student[-1])
print(student[-1].learn())

print("***** 학생 명단 *****")
for s in student:
    print(s)
    #print(s.learn())