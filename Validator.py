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

    def check_passport_number(self, passport_number: str) -> bool:
        pattern = "^\d{6}$"
        if re.match(pattern, str(passport_number)):
            return True
        return False

    def check_occupation(self, occupation: str) -> bool:  # старый паттерн : "^([а-яА-Я]|[a-zA-Z]|-| ){3,}$"
        pattern = "^([а-яА-Я]|-| ){3,}$"
        if re.match(pattern, occupation):
            return True
        return False

    def check_age(self, age: int) -> bool:
        pattern = "^([1-9]|[1-9][0-9]|1[0-1][1-9]|120)$"
        if re.match(pattern, str(age)):
            return True
        return False

    def check_academic_degree(self, academic_degree: str) -> bool:
        pattern = "Кандидат наук|Доктор наук|Специалист|Бакалавр|Магистр"
        if re.match(pattern, academic_degree):
            return True
        return False

    def check_worldview(self, worldview: str) -> bool:
        pattern = "Конфуцианство|Иудаизм|Католицизм|Секулярный гуманизм|Пантеизм|Агностицизм|Деизм|Буддизм|Атеизм"
        if re.match(pattern, worldview):
            return True
        return False

    def check_address(self, address: str) -> bool: # старый "^([а-я]|\s|[А-Я]|\.)+\s[1-9][0-9]*$"
        pattern = "^([а-я-]|\s|[А-Я]|\.|(\d{1,2}-[а-я])|(\d{1,3} \W{2})+(\s[1-9][0-9])*)+\s[1-9][0-9]*$"
        if re.match(pattern, address):
            return True
        return False

    def parse_valid(self) -> list[Users]:
        legal_users: list[Users] = []
        count_invalid = 0
        for i in self.list_users:
            illegal_keys = self.parse_user(i)
            if (len(illegal_keys) == 0):
                legal_users.append(i)
            else:
                count_invalid += 1
        print("Count of invalid writes = ", count_invalid)
        return legal_users

    def parse_invalid(self) -> dict:  # число невалидных записей по типам ошибок
        illegal_writes = {
            "email": 0,
            'height': 0,
            'snils': 0,
            'passport_number': 0,
            'occupation': 0,
            'age': 0,
            'academic_degree': 0,
            'worldview': 0,
            'address': 0
        }

        for i in self.list_users:
            illegal_keys = self.parse_user(i)

            for j in illegal_keys:
                illegal_writes[j] += 1

        return illegal_writes

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
