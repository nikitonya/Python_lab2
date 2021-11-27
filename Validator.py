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

    def check_height(self, height:str) -> bool:
        f_height = float(height)
        if 2.3 > f_height > 1.0:
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
        if not self.check_height(user['height']):
            illegal_keys.append('height')
        return illegal_keys
