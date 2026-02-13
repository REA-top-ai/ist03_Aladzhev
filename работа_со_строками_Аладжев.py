favour_word ="Яблоко"
print(favour_word)





first_name ="Виталий"
last_name = "Красилов"
new_account = last_name[:5]
temp_password = last_name[2:6]

def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)


def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]
temp_password = password_generator(first_name, last_name)




company_motto = "Мечты сбываются"
second_to_last = company_motto[:-2]
final_word = company_motto[-4:]
