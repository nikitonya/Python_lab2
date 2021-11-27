import re
from Users import Users


class Validator():
    def __init__(self, list: list[Users]):
        self.list_users = []

        for i in list:
            self.list_users.append(i.copy())

    def get_list(self):
        return self.list_users

    def check_email(self, email: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def check_height(self, height: str) -> bool:
        pattern = "^[1-2]+\.+\d\d$"
        if re.match(pattern, str(height)):
            return True
        return False

    def check_snils(self, snils: str) -> bool:
        pattern = "^\d{11}$"
        if re.match(pattern, snils):
            return True
        return False

    def check_passport_number(self, passport_number: int) -> bool:
        pattern = "^\d{6}$"
        if re.match(pattern, str(passport_number)):
            return True
        return False

    def check_occupation(self, occupation: str) -> bool:
        pattern = "^([а-яА-Я]|[a-zA-Z]|-| ){3,}$"
        if re.match(pattern, occupation):
            return True
        return False

    def check_age(self, age: int) -> bool:
        pattern = "^([1-9]|[1-9][0-9]|1[0-1][1-9]|120)$"
        if re.match(pattern, str(age)):
            return True
        return False


    def check_academic_degree(self, academic_degree: str) -> bool:
        pattern = "Кандидат наук|Доктор наук"
        if re.match(pattern, academic_degree):
            return True
        return False

    def check_worldview(self, worldview: str) -> bool:
        pattern = "Ислам|Буддизм|Христианство|Иудаизм|Конфуциантсво|Древнегреческая мифология" \
                  "|Синтоизм|Скандинавская мифология|Индуизм|Древнеегипетская религия|" \
                  "Джайнизм|Славянская мифология|Римская религия|Кельтская мифология|Ведизм"
        if re.match(pattern, worldview):
            return True
        return False

    def check_address(self, address: str) -> bool:
        pattern = "^([а-я]|\s|[А-Я]|\.)+\s[1-9][0-9]*$"
        if re.match(pattern, address):
            return True
        return False


    def parse_valid(self) -> list[Users]:
        legal_users: list[Users] = []
        for i in self.list_users:
            illegal_keys = self.parse_user(i)
            if (len(illegal_keys) == 0):
                legal_users.append(i)
        return legal_users

    def parse_user(self, user: Users) -> list[str]:
        illegal_keys = []
        if not self.check_email(user['email']):
            illegal_keys.append('email')
        elif not self.check_height(user['height']):
            illegal_keys.append('height')
        elif not self.check_snils(user['snils']):
            illegal_keys.append('snils')
        elif not self.check_passport_number(user['passport_number']):
            illegal_keys.append('passport_number')
        elif not self.check_occupation(user['occupation']):
            illegal_keys.append('occupation')
        elif not self.check_age(user['age']):
            illegal_keys.append('age')
        elif not self.check_academic_degree(user['academic_degree']):
            illegal_keys.append('academic_degree')
        elif not self.check_worldview(user['worldview']):
            illegal_keys.append('worldview')
        elif not self.check_address(user['address']):
            illegal_keys.append('address')


        return illegal_keys
