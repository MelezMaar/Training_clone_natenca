# -*- coding: utf-8 -*-
import re
from pprint import pprint
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
def get_ints_without_description(file_conf):
    '''
        - file_conf - конфигурационный файл
        - result - список 
    '''
    result = []
    pattern_mash = re.compile(r"interface (?P<intf>\S+)"
                              r"| description (?P<des>\S+)")
    
    with open(file_conf, "r") as conf_file:
        for line_conf in conf_file: 
            match_conf = pattern_mash.match(line_conf)
            if match_conf:
                if match_conf.lastgroup == 'intf':
                    intfs = match_conf.group(match_conf.lastgroup)
                    result.append(intfs)
                else:
                    result.remove(intfs)
    return result

if __name__ == "__main__":
    #pprint (get_ints_without_description(r'.\Training_clone_natenca\exercises\15_module_re\config_r1.txt'))
    print (get_ints_without_description(r'config_r1.txt', 'r'))

