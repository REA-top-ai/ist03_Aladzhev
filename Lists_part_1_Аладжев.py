products = ["торт", 1]

household_chemicals = [["стиральный порошок", 1],["средство для мытья посуды", 1],]


Names = ["Ben", "Holly", "Ann"]
dogs_names = ["Sharik", "Gab", "Beethoven"]
names_and_dogs_names = zip(Names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)


orders = ["маргаритки", "васильки"]
print(orders)
orders.append("тюльпаны")
orders.append("розы")
print(orders)


orders = ["маргаритка", "лютик", "львиный зев", "гардения", "лилия"]
new_orders = orders + ["сирень", "ирис"]
#broken_prices = [5, 3, 4, 5, 4] + [4] - правильно будет, если 4 тоже будет списком


list1 = [1,8]
list1 = range(0, 9)
list2 = range(0, 8)


list1 = range(5, 15, 3)
list2 = range(0, 41, 5)




first_names = ["Эйнсли", "Бен", "Чани", "Депак"]
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = list(zip(first_names, all_ages))
ids = range(0, 4)

