import random


def generate_password():
    for i in range(10000):
        password = create_password()
        f = open('passwords.txt', 'a')
        f.write(f"{password}\n")
        yield password


def create_password():
    password = ''
    while len(password) < 4:
        elements = '1234567890'
        password += random.choice(elements)
    return password


# passwords = generate_password()
# for el in passwords:
#     print(el)
f = open("passwords.txt", "r")
info = []
for i in f.readlines():
    info.append(i[:-1])
print("пароль знайдено" if "1919" in info else "не знайдено")
