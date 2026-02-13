from dataclasses import dataclass
from datetime import datetime, date
import random
import string
from typing import Dict, List, Iterable, Tuple, Optional



import datetime as dt
current_time = dt.datetime.now()
print(current_time)


import random
random_list = []
random_list = [random.randint(1, 100) for i in range(101)]
randomer_number = random.choice(random_list)




from matplotlib import pyplot as plt
import random
number_a = list(range(1, 13))
number_b = random.sample(range(1000), 12)
plt.plot(number_a, number_b)
plt.show()




#-------

employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]

def calculate_programmer_bonus(employees_list):
    for employee in employees_list:
        if "программист" in employee[1].lower():
            bonus = employee[3] * 0.03
            print(bonus)
    print()


def calculate_holiday_bonus(employees_list):
    for employee in employees_list:
        full_name = employee[0]
        patronymic = full_name.split()[-1]
        if patronymic.endswith(('а', 'я')):
            print("Премия к 8 марта: 2000 руб.")
        else:
            print("Премия к 23 февраля: 2000 руб.")
    print()


def calculate_experience_years(hire_date):
    day, month, year = map(int, hire_date.split('.'))
    current_year = 2026
    current_month = 2
    current_day = 13
    years = current_year - year
    if (month > current_month) or (month == current_month and day > current_day):
        years -= 1
    return years


def calculate_indexation(employees_list):
    for employee in employees_list:
        old_salary = employee[3]
        years = calculate_experience_years(employee[2])
        if years > 10:
            percent = 7
        else:
            percent = 5
        new_salary = old_salary * (1 + percent / 100)
        print(new_salary)



def get_vacation_list(employees_list): 
    vacation_list = []
    for employee in employees_list:
        years = calculate_experience_years(employee[2])
        if years > 0.5:
            vacation_list.append(employee[0])
            print(years)
    return vacation_list


if __name__ == "__main__":
    calculate_programmer_bonus(employees)
    

    calculate_holiday_bonus(employees)
    

    calculate_indexation(employees)
    

    vacation_employees = get_vacation_list(employees)
    
    print("Итоговый список сотрудников для отпуска:")
    for i, employee in enumerate(vacation_employees, 1):
        print(i, employee)
