
class Button:
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1
        print(f'Кликов: {self.clicks}')

b = Button()
b.click()
b.click()