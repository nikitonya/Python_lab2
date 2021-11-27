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

