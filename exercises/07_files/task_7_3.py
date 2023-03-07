# -*- coding: utf-8 -*-
"""
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
cam_table_list = []
with open('CAM_table.txt', 'r') as file:
    for cam_line in file:
        cam_line = cam_line.strip() #Не забываем удалять лишние символы
        if cam_line.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')): #Проверяем, начинается ли строка с цифр
            #for i in range(10):
            #    cam_line.strip().split(' ').remove('')
            cam_table_list.append(cam_line.strip().split())
          
for i in cam_table_list:
    print('{:<9}{:20}{}'.format(i[0], i[1], i[3]))
       
