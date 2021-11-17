class Users:
    def __init__(self, dict: dict):
        self.email = dict['email']
        self.height = dict['height']
        self.snils = dict['snils']
        self.passport_number = dict['passport_number']
        self.occupation = dict['occupation']
        self.age = dict['age']
        self.academic_degree = dict['academic_degree']
        self.worldview = dict['worldview']
        self.address = dict['address']
