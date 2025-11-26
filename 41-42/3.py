from datetime import datetime, timedelta

d = datetime.now()

# 1. Сформировать список дат для записи
dates = []
for i in range(3):
    new_date = d + timedelta(days=i+1)
    dates.append(new_date)

dates = [date.strftime('%m.%d') for date in dates]

