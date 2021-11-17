import re
from Users import Users


class Vadidator():
    def __init__(self, list_users: list[Users]):
        self.list_users = []

        for i in list_users:
            self.list_users.append(i.copy())

    def check_email(self, email: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        return False
