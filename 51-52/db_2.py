import json


class DB:

    def __init__(self, filename):
        self.filename = filename
    def read_database(self):
        """Чтение файла базы данных"""
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def write_database(self, data: dict):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_day(self, data):
        data = self.read_database()
        data['days'].append({})
        self.write_database(data)


db = DB('data.json')
db.add_day({})