# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
from pprint import pprint

def parse_sh_cdp_neighbors (neighbors_line):
    devise_name = neighbors_line.split('>')[0].strip()
    pattern_neighbors = re.compile(r'(?P<devise_id>\S+) +'
                                   r'(?P<local_intf>\S+ \S+) +'
                                   r'\d+ +'
                                   r'.+'
                                   r' (?P<port_id>\S+ \S+)')
    result = {}
    result[devise_name] = {}

    match_neighbors = pattern_neighbors.finditer(neighbors_line)
    for neighbors in match_neighbors:
        device_id, local_intf, port_id = neighbors.group('devise_id', 'local_intf', 'port_id')
        result[devise_name][local_intf] = {}
        result[devise_name][local_intf][device_id] = port_id    
    return result

if __name__ == "__main__":
    with open(r"sh_cdp_n_r2.txt") as f:
            pprint(parse_sh_cdp_neighbors(f.read()))
