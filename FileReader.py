import json
import Users


class FileReader():
    data: list[Users]

    def __init__(self, path) -> None:
        self.path = path

    def __del__(self):
        print("del obj")

    def read_file(self) -> list[Users]:
        data = json.load(open(self.path, encoding='windows-1251'))
        return data
