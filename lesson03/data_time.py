'''
Задание

    Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
    Превратите строку "01/01/25 12:10:03.234567" в объект datetime

'''

from datetime import datetime, timedelta

data_today1 = datetime.now() # сегодня
data_today2 = datetime.today() # сегодня
# datetime.now() datetime.today() в чем принципиальная разница и какой метод в каких случаях применяется?

yesterday = data_today1 - timedelta(days = 1) # вчера
ago_30_days  = data_today1 - timedelta(days = 30) # 30 дней назад

print(f'сегодня_1: {data_today1}')
print(f'сегодня_2: {data_today2}')
print(f'вчера: {yesterday}')
print(f'30 дней назад: {ago_30_days}')

data = '01/01/25 12:10:03.234567'
print(datetime.strptime(data, '%d/%m/%y %H:%M:%S.%f'))
object_datetime_data = datetime.strptime(data, '%d/%m/%y %H:%M:%S.%f')
print(type(object_datetime_data))
