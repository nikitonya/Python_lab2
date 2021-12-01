class Users:
    """ Класс для объектов типа "Пользователя" """
    email: str
    height: str
    snils: str
    passport_number: str
    occupation: str
    age: str
    academic_degree: str
    worldview: str
    address: str

    def __init__(self, dct: dict):
        """
            Конструктор класса

            Parameters
            ----------
                dict: dict
                    Словарь с полями из файла
        """
        self.email = dct['email']
        self.height = dct['height']
        self.snils = dct['snils']
        self.passport_number = dct['passport_number']
        self.occupation = dct['occupation']
        self.age = dct['age']
        self.academic_degree = dct['academic_degree']
        self.worldview = dct['worldview']
        self.address = dct['address']
