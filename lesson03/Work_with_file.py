'''
Задание

    Скачайте файл по ссылке
    Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
    Подсчитайте количество слов в тексте
    Замените точки в тексте на восклицательные знаки
    Сохраните результат в файл referat2.txt

'''

with open('referat.txt', 'r', encoding= 'utf_8') as f:
    dump_text = f.read()
    len_dump_text = len(dump_text)
    print(f'длина получившейся строки(файла): {len_dump_text}')

    word_count = len(dump_text.split())
    print(f'количество слов в тексте: {word_count}')

with open('referat.txt', 'r', encoding= 'utf_8') as f:
    for line in f:
        line = line.replace('.','!')
        with open ('referat2.txt', 'a', encoding= 'utf_8') as file:
            file.write(line)
    print('Файл referat2.txt сохранен, проверяй ;)!')
