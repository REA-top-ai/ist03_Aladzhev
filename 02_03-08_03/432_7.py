correct = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
studend = open('student.txt').readline().split(" ")
a = 0
b = 0
wrong_numbers = []
for i in range(20):
    if correct[i] == studend[i]:
        a += 1
    else:
        b += 1
        wrong_numbers.append(i + 1)
if a >= 15:
    print("Экзамен сдан")
else:
    print("Экзамен не сдан")
print("Количество верных", a)
print("Количество неверных", b)
print("Неправильные ответы даны на вопросы", *wrong_numbers)
