square = [[], [], []]
for i in range(3):
    for j in range(3):
        square[i].append(int(input("Введите числа")))
def square_check(square):
    proverka_chisel = [square[i][j] for i in range(3) for j in range(3)]
    if sorted(proverka_chisel) != list(range(1, 10)):
        return False
    need_sum = sum(square[0])
    if not(need_sum == sum(square[1]) == sum(square[2])):
        return False
    if not(need_sum == sum([square[i][0] for i in range(3)]) == sum([square[i][1] for i in range(3)]) == sum([square[i] [2]for i in range(3)])):
        return False
    if not(need_sum == square[0][0] + square[1][1] + square[2][2] == square[0][2] + square[1][1] + square[2][0]):
        return False
    return True
print(square_check(square))
