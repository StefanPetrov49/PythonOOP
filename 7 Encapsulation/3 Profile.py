class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_enough_char(value) and self.has_digit(value) and self.has_upper(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def is_enough_char(self, password):
        return len(password) >= 8

    def has_digit(self, password):
        result = [el for el in password if el.isdigit()]
        if result:
            return True
        return False

    def has_upper(self, password):
        result = [el for el in password if el.isupper()]
        if result:
            return True
        return False
    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*"* len(self.__password)}'
