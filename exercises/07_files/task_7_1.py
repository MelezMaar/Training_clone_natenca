# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

with open('ospf.txt', 'r') as f:
    for ospf_route in f:
        ospf_route_list = ospf_route.strip().replace(' ', ',').split(',') #Получаем список, не забыв удалить лишние пробелы
        #print(ospf_route_list)
        #Для урезания числа элементов списка, преобазование в множество не подойдет.
        # Элементы внутри разных множеств, будут на разных метсах
        # Сначало во множество, потом обратно в список и включить сортировку тоже не подойдет. Окажется "время" меньше чем ip и пордок тоже нарушится
        ospf_route_dic = {
            'Prefix': ospf_route_list[8],
            'AD/Metric': ospf_route_list[9][1:-1], #не забываем удалить скобочки
            'Next-Hop': ospf_route_list[11],
            'LastUpdate': ospf_route_list[13],
            'OutboundInterface' : ospf_route_list[15]
        }
        print(template.format(ospf_route_dic['Prefix'], ospf_route_dic['AD/Metric'], ospf_route_dic['Next-Hop'], ospf_route_dic['LastUpdate'], ospf_route_dic['OutboundInterface']))
        
