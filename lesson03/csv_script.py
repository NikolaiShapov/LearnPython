'''
Задание

    Создайте список словарей:
            [
            {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
            {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]
    Запишите содержимое списка словарей в файл в формате csv
'''
import csv

BaseUser = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'},
            {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
            ]

with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in BaseUser:
        writer.writerow(user)
    print('Файл export.csv сохранен, проверяй ;)!')
