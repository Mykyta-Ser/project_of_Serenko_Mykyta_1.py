import random
def generate_password():
    for i in range(10000):
        password = create_password()
        f = open('passwords.txt', 'a')
        f.write(f"{password}\n")
        yield password


def create_password():
    password = ''
    while len(password) < 16:
        elements = '!@$%^&*_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        password += random.choice(elements)
    if password.find('!@$%^&*_') and any(el.isupper() for el in password) and any(el.islower() for el in password) and any(el.isdigit() for el in password):
        return password
    else:
        return f"{password} - недостатньо безпечний"


passwords = generate_password()
for el in passwords:
    print(el)
