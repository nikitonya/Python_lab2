import json
import Users


class FileReader():
    """Класс для считывания из файла"""

    def __init__(self, path) -> None:
        """
          Конструктор класса
          Parameters
          ----------
          path : str
            Путь к файлу
          """
        self.path = path

    def read_file(self) -> list[Users]:
        """
          Возвращает список объектов типа Users

          Данная функция считывает данные из файла
          Returns
          -------
          list[Users]
            Список объектов типа Users
          """
        data = json.load(open(self.path, encoding='windows-1251'))
        return data
