board_games = ['Settlers of Catan', 'Carcassonne', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
for i in sport_games:
    print(i)



promise = "I will not chew gum in class"
for i in range(5):
    print(promise)




students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
    students_period_B.append(student)
    print(student)
print(students_period_B)


#с ошибкой
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
c = 0
for student in students_period_A:
    students_period_A.append(student)
    c += 1
    if c >= 100:
        break


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
c = 0
for student in students_period_A:
    students_period_B.append(student)
    c += 1
    if c >= 100:
        break





dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for i in dog_breeds_available_for_adoption:
    if i == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break




sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for i in sales_data:
    for j in i:
        scoops_sold += j
print(scoops_sold)




#---
single_digits = list(range(10))
squares = []

for i in single_digits:
    print(i)
    squares.append(i ** 2)
print(squares)


cubes = [i ** 3 for i in single_digits]
print(cubes)




