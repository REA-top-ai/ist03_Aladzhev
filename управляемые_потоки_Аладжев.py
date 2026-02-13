#true, true, false




bool_variable = "true"
print(type(bool_variable))

#bool_variable - теперь имеет тип string

bool_variable2 = True
print(type(bool_variable2))
#bool_variable2 - логическая



user_name = input()
dmitriy_check = "Дмитрий, твоё рабочее место находится в другой комнате."
if user_name == "Дмитрий":
    print(dmitriy_check)
if user_name == "Ангелина":
    print("Добро пожаловать")



enter_number = 0
if enter_number < 3:
    print("У вас осталось", 3-enter_number, "попыток")
if enter_number >=3:
    print("Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")
