def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

#---

def get_force(mass, acceleration):
    return mass * acceleration
train_mass=22680
train_acceleration=10
print("Поезд GE поставляет", get_force(train_mass, train_acceleration), "ньютонов силы")


def get_energy(mass, c=3 * 10**8):
    return mass * (c**2)
bomb_mass=1
bomb_energy = get_energy(bomb_mass)
print("1 кг бомбы составляет", bomb_energy, "джоулей")

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance
train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)
print("Поезд выполняет", train_work, "Джоулей за", train_distance, "метров")


#--

def wardrobe_preferences(clothes):
    print("У меня большой гардероб")
    for time in ["утром", "днем", "вечером", "ночью"]:
        print(time, "лучше всего подходит", clothes)
def meal_preferences(meal):
    print("Мои предпочтения в еде")
    for time in ["завтрак", "обед", "ужин"]:
        print(time, "лучше всего подходит", meal)


#----
user_name = input()
arm = input()
def check(user_name, arm):
    dmitriy_check = "Дмитрий, твоё рабочее место находится в другой комнате."
    if user_name == "Дмитрий" and arm != '1':
        print(dmitriy_check)
    else:
        if (arm=="1" and user_name=="Дмитрий") or (arm == '2' and user_name == "Ангелина") or (arm == '3' and user_name == "Василий") or (arm == '4' and user_name == "Екатерина"):
            print("Добро пожаловать!")
        else:
            print("Логин или пароль неверный попробуйте еще раз.")
check(user_name, arm)
        
#----
grade = int(input())
def test_grade(grade):
    if grade >= 4:
        return "A"
    elif grade >= 3:
        return "B"
    elif grade >= 2:
        return "C"
    elif grade >= 1:
        return "D"
    elif grade >= 0:
        return "F"
print(test_grade(grade))
