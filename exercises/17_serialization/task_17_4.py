# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать функцию write_last_log_to_csv.

Аргументы функции:
* source_log - имя файла в формате csv, из которого читаются данные (mail_log.csv)
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Функция write_last_log_to_csv обрабатывает csv файл mail_log.csv.
В файле mail_log.csv находятся логи изменения имени пользователя. При этом, email
пользователь менять не может, только имя.

Функция write_last_log_to_csv должна отбирать из файла mail_log.csv только
самые свежие записи для каждого пользователя и записывать их в другой csv файл.
В файле output первой строкой должны быть заголовки столбцов,
такие же как в файле source_log.

Для части пользователей запись только одна и тогда в итоговый файл надо записать
только ее.
Для некоторых пользователей есть несколько записей с разными именами.
Например пользователь с email c3po@gmail.com несколько раз менял имя:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Из этих трех записей, в итоговый файл должна быть записана только одна - самая свежая:
C-3PO,c3po@gmail.com,16/12/2019 17:24

Для сравнения дат удобно использовать объекты datetime из модуля datetime.
Чтобы упростить работу с датами, создана функция convert_str_to_datetime - она
конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
Полученные объекты datetime можно сравнивать между собой.
Вторая функция convert_datetime_to_str делает обратную операцию - превращает
объект datetime в строку.

Функции convert_str_to_datetime и convert_datetime_to_str использовать не обязательно.

"""

import datetime
import csv
from pprint import pprint


def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")

def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")

def write_last_log_to_csv(source_log, output):
    #Читаем лог и сохраняем его в список из словарей
    with open(source_log) as file:
        log_iter = csv.DictReader(file)
        list_user = []
        for dir_user in log_iter:
            list_user.append(dir_user)

    # Создаем итоговый список словарей с нужной нам структурой, иначе ошибка
    output_list = [{'Email': 'NON', 'Last Changed': 'NON', 'Name': 'NON'}]

    for user_dir in list_user:
        name_chek = False # Флаг. проверяющий был ли email раньше в списке
        #Данный цикл проверяет, есть ли email из лога, в итоговом списке, если нет, добовляет его
        for out_user_dir in output_list:
            if out_user_dir['Email'] == user_dir['Email']:
                # Если email уже есть в итоговом списке, то сравниваются даты
                if convert_str_to_datetime(user_dir['Last Changed']) > convert_str_to_datetime(out_user_dir['Last Changed']):
                    i = output_list.index(out_user_dir) # Определяется индекс
                    output_list[i] = user_dir # обновляется итоговый список
                name_chek = True # email уже был в списке, тоак что его не добовляем
        # Добавляем новый email в итоговый список        
        if name_chek == False:
            output_list.append(user_dir)
    # Удаляем начальную структуру        
    output_list.remove({'Email': 'NON', 'Last Changed': 'NON', 'Name': 'NON'})

    # Записываем результат в файл
    with open(output, 'w') as file_read:
        writer = csv.DictWriter(
            file_read, fieldnames=list(output_list[0].keys()), quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for read_data in output_list:
            writer.writerow(read_data)

    #pprint(output_list)



if __name__ == "__main__":
    write_last_log_to_csv('mail_log.csv', 'output_mail.csv')