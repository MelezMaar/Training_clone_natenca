# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
            # Если порт в режиме access, помещаем его в первй VLAN     
            elif 'mode access' in line_conf: 
                port_access[intf] = 1    
            # Если Vlan задан явно, то переписываем 1 vlan по умолчанию, на нужный    
            elif 'access vlan' in line_conf:
                port_access[intf] = int(line_conf.split()[3])
            elif 'trunk allowed vlan' in line_conf:
                vlan_int = [int(num_vlan) for num_vlan in line_conf.split()[4].split(',')]
                port_trunk[intf] = vlan_int
    return port_access, port_trunk

print(get_int_vlan_map('config_sw1.txt'))