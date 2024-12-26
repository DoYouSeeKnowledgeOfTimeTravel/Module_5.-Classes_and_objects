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
    while True:
        user_register = User(input('Введите логин: '), password_register := input('Введите пароль: '), password2_register := input('Повторите пароль: '))
        database.add_user(user_register.username, user_register.password)