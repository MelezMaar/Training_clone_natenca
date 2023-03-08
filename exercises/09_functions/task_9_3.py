# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map (config_filename):
    
    '''- config_filename - файл конфигурации
     - Возвращает кортеж из двух словарей:
     словарь портов в режиме access, где ключи номера портов,
     а значения access VLAN (числа)
     - словарь портов в режиме trunk, где ключи номера портов,
     а значения список разрешенных VLAN (список чисел)
    '''
    port_access = {}
    port_trunk = {}
    with open (config_filename, 'r') as file:
        for line_conf in file:
            if line_conf.strip().startswith('interface'):
                intf = line_conf.split()[1]
            elif 'access vlan' in line_conf:
                port_access[intf] = int(line_conf.split()[3])
            elif 'trunk allowed vlan' in line_conf:
                vlan_int = [int(num_vlan) for num_vlan in line_conf.split()[4].split(',')]
                port_trunk[intf] = vlan_int
    return port_access, port_trunk

print(get_int_vlan_map('config_sw1.txt'))