class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    valid = False
    while True:
        choice = input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n')
        user = User(input('Введите логин: '), password := input('Введите пароль: '), password_confirm := input('Повторите пароль: '))
        if password != password_confirm:
            exit(print('Пароли не совпадают'))
        if valid != True:

        else:

            database.add_user(user.username, user.password)
            print(database.data)
