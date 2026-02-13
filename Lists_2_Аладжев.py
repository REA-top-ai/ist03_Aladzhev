list1 = range(2, 20, 2)
list1_len = len(list1)
print(list(list1))
print(list1_len)


list1 = range(2, 20, 3)
list1_len_new = len(list1)
print(list(list1))
print(list1_len_new)
print(list1_len, "теперь", list1_len_new)


shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(last_element)
print(element5)



suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase[0:2]
print(len(suitcase))
beginning = suitcase[0:4]
print(beginning)
middle = suitcase[2:4]


suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase[:3]




votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie','Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = 0
for i in votes:
    if i == 'Jake':
        jake_votes += 1
print(jake_votes)



addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place',
'742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
print(addresses)
addresses.sort()
print("После сортировки", addresses)



games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games)
print(games_sorted)




#---
inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье',
'двуспальная кровать', 'двуспальная кровать', 'комод', 'комод', 'стол', 'стол',
'тумбочка', 'тумбочка', 'королевский кровать', 'двуспальная кровать',
'две односпальные кровати', 'две односпальные кровати', 'простыни', 'простыни', 'подушка', 'подушка'
]
inventory_len = len(inventory)
print(inventory_len)
first = inventory[0]
last = inventory[-1]
print(first)
print(last)

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first_3 = inventory[:3]
print(first_3)

twin_beds = 0
for i in inventory:
    if i == 'две односпальные кровати':
        twin_beds += 1
print(twin_beds)

inventory.sort()
print(inventory)


