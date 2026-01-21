import os
import json

class DB:
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return f'Класс для работы с файлом {self.filename}'

    def read_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, encoding='utf-8') as f:
            data = json.load(f)
        return data

    def write_data(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False)
