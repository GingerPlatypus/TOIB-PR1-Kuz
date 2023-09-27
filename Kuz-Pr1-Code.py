import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def random_password():
    length = int(input("Введите длинну пароля или нажмите Enter для генерации 8-символьного пароля по умолчанию: ") or 8)
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print ("Ваш сгенерированный пароль: ", "".join(password))
random_password()