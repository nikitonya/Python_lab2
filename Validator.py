import re
from Users import Users
from tqdm import tqdm


class Validator():
    """Класс для валидации данных"""
    def __init__(self, lst: list[Users]):
        """
                  Конструктор класса
                  Parameters
                  ----------
                  lst: list[Users]
                    Список объектов класса Users
                  """
        self.list_users = []

        for i in lst:
            self.list_users.append(i.copy())

    def check_email(self, email: str) -> bool:
        '''
          Выполняет проверку корректности адреса электронной почты.

          Parameters
          ----------
            email : str
              Строка с проверяемым электронным адресом

          Returns
          -------
            bool:
              Булевый результат проверки на корректность
        '''
        pattern = "^[^\\s@]+@([^\\s@.,]+\\.)+[^\\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def check_height(self, height: str) -> bool:
        '''
            Выполняет проверку корректности роста человека.

            Parameters
            ----------
            height : str
                Строка с проверяемым ростом человека

            Returns
            -------
            bool:
                Булевый результат проверки на корректность
        '''
        pattern = "^[1-2]+\\.+\\d\\d$"
        if re.match(pattern, str(height)):
            return True
        return False

    def check_snils(self, snils: str) -> bool:
        '''
            Выполняет проверку корректности снилса

            Parameters
            ----------
            snils : str
                Строка с проверяемым снилсом

            Returns
            -------
            bool:
                Булевый результат проверки на корректность
        '''
        pattern = "^\\d{11}$"
        if re.match(pattern, snils):
            return True
        return False

    def check_passport_number(self, passport_number: str) -> bool:
        '''
            Выполняет проверку корректности паспортного номера

            Parameters
            ----------
            passport_number : str
                Строка с проверяемым номером

            Returns
            -------
            bool:
                Булевый результат проверки на корректность
        '''
        pattern = "^\\d{6}$"
        if re.match(pattern, str(passport_number)):
            return True
        return False

    def check_occupation(self, occupation: str) -> bool:
        '''
            Выполняет проверку корректности занятости человека

            Parameters
            ----------
            occupation : str
                Строка с проверяемым словом

            Returns
            -------
            bool:
                Булевый результат проверки на корректность
        '''
        pattern = "^([а-яА-Я]|-| ){3,}$"
        if re.match(pattern, occupation):
            return True
        return False

    def check_age(self, age: int) -> bool:
        '''
                    Выполняет проверку корректности возраста человека

                    Parameters
                    ----------
                    age : str
                        Строка с проверяемым возрастом

                    Returns
                    -------
                    bool:
                        Булевый результат проверки на корректность
                '''
        pattern = "^([1-9]|[1-9][0-9]|1[0-1][1-9]|120)$"
        if re.match(pattern, str(age)):
            return True
        return False

    def check_academic_degree(self, academic_degree: str) -> bool:
        '''
                    Выполняет проверку корректности академической степени

                    Parameters
                    ----------
                    academic_degree : str
                        Строка с проверяемой степенью

                    Returns
                    -------
                    bool:
                        Булевый результат проверки на корректность
                '''
        pattern = "Кандидат наук|Доктор наук|Специалист|Бакалавр|Магистр"
        if re.match(pattern, academic_degree):
            return True
        return False

    def check_worldview(self, worldview: str) -> bool:
        '''
                    Выполняет проверку корректности веры человека

                    Parameters
                    ----------
                    worldview : str
                        Строка с проверяемым словом

                    Returns
                    -------
                    bool:
                        Булевый результат проверки на корректность
                '''
        pattern = "Конфуцианство|Иудаизм|Католицизм|Секулярный гуманизм|Пантеизм|Агностицизм|Деизм|Буддизм|Атеизм"
        if re.match(pattern, worldview):
            return True
        return False

    def check_address(self, address: str) -> bool:
        '''
                    Выполняет проверку корректности адресса, вводимого человеком

                    Parameters
                    ----------
                    address : str
                        Строка с проверяемым адрессом

                    Returns
                    -------
                    bool:
                        Булевый результат проверки на корректность
                '''
        pattern = "^([а-я-]|\\s|[А-Я]|\\.|(\\d{1,2}-[а-я])|(\\d{1,3} \\W{2})+(\\s[1-9][0-9])*)+\\s[1-9][0-9]*$"
        if re.match(pattern, address):
            return True
        return False

    def parse_valid(self) -> list[Users]:
        '''
          Выполняет парсинг валидных значений

          Если ошибок нет, записывает запись в список

          Returns
          -------
            legal_users : list[Users]
              Список пользователей с валидными значениями
          '''
        legal_users: list[Users] = []
        count_invalid = 0
        count_valid = 0
        with tqdm(total=len(self.list_users), colour='green', desc='Validation of writes', ncols=150) as progress_bar:
            for i in self.list_users:
                illegal_keys = self.parse_user(i)
                if (len(illegal_keys) == 0):
                    legal_users.append(i)
                    progress_bar.update(1)
                    count_valid += 1
                else:
                    count_invalid += 1
                    progress_bar.update(1)
        print("Число валидных записей =  ", count_valid)
        print("Число невалидных записей = ", count_invalid)
        return legal_users

    def parse_invalid(self) -> dict:
        '''
          Выполняет подсчёт невалидных значений

          С помощью функции parse_user записывает категории где значения оказались невалидными, и
          записывает в словарь нелегальных значений количество

          Returns
          -------
            illegal_writes : dict
              Словарь с количеством невалидных значений по каждой категории
          '''
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
        '''
          Выполняет парсинг определённого пользователя(объекта)

          Делает проверку каждой категории с помощью соответствующей функции и если категория невалидна,
          записывает соотвествующее название категории в список

          Parameters
          ----------
            user: Users
              Объект класса Users

          Returns
          -------
            illegal_keys : list[str]
              Список строк
          '''
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
