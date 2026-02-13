ans = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1)
ans2 = []
for i in range(20):
    a = int(input())
    ans2.append(a)

if list(ans) == ans2:
    print("Экзамен  сдан")
else:
    print("Экзамен провален")
