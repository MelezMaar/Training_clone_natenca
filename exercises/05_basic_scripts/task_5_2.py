# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_template = '''
Network:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:08b}   {1:08b}   {2:08b}   {3:08b}

Mask:
{8:}
{4:<10} {5:<10} {6:<10} {7:<10}
{4:08b}   {5:08b}   {6:08b}   {7:08b}
'''

prefix = input("Введите адрес сети: ")
#prefix = "10.11.12.13/23"
ip = prefix[:-3]
number_ip = ip.split('.')
number_ip[0] = int(number_ip[0])
number_ip[1] = int(number_ip[1])
number_ip[2] = int(number_ip[2])
number_ip[3] = int(number_ip[3])
mask = prefix[-3:]
mask_bin = "1" * int(mask[1:]) + "0" * (32 - int(mask[1:]))
number_mask = []
number_mask.append(int(mask_bin[:-24], 2))
number_mask.append(int(mask_bin[8:-16], 2))
number_mask.append(int(mask_bin[16:-8], 2))
number_mask.append(int(mask_bin[24:], 2))

print(ip_template.format(number_ip[0], number_ip[1], number_ip[2], number_ip[3], number_mask[0], number_mask[1], number_mask[2], number_mask[3], mask))
