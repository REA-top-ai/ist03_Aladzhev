days = int(input("Введите количество дней:"))
summ = 0
a = 0.5
ans = []
if days > 0:
    for i in range(1, days+1):
        a = a * 2
        summ += a
        ans.append(int(a))
print(summ / 100)
print(ans)
