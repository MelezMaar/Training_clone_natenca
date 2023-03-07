# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
cam_table_list = []
with open('CAM_table.txt', 'r') as file:
    for cam_line in file:
        cam_line = cam_line.strip()
        if cam_line.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')):
            #for i in range(10):
            #    cam_line.strip().split(' ').remove('')
            cam_table_list.append(cam_line.strip().split())

for i in cam_table_list:
    i[0] = int(i[0])
 
vlan_cam = input('Введи номер vlan: ')
if vlan_cam.isdigit(): # не забываем про банальную проверочку
    for element in sorted(cam_table_list):
        if element[0] == int(vlan_cam): # Выводим только указанный VLAN
            print('{:<9}{:20}{}'.format(element[0], element[1], element[3]))
else:
    print('Неверные данные!')