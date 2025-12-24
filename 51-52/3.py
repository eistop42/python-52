from datetime import datetime

slots = ['9:00', '12:00', '14:00', '18:00', '21:00']

slot = datetime.strptime('18:00', '%H:%M').time()
current = datetime.now().time()
print(current, slot)
if slot < current:
    print('Меньше')