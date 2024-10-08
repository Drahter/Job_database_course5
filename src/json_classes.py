import json
from abc import ABC, abstractmethod


class File(ABC):
    @abstractmethod
    def save_data(self, vacancies):
        pass


class JSONSaver(File):
    def __init__(self, file_name="vacancies.json"):
        self.filename = f"data/{file_name}"

    def save_data(self, vacancies):
        """Запись файла в формате json"""
        with open(self.filename, "w") as file:
            json.dump(vacancies, file, indent=2)

    def get_data(self):
        """Получение данных из файла формата json"""
        with open(self.filename, "r") as file:
            data = json.load(file)

        return data
