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

    def parse_user(self, user: Users):
        illegal_keys = []
        if not self.check_email(user['email']):
            illegal_keys.append(user['email'])
        return illegal_keys

    def parse_valid(self):
        legal_users = []
        for i in self.list_users:
            illegal_keys = self.parse_user(i)
            if (len(illegal_keys) == 0):
                legal_users.append(i)
        return legal_users
