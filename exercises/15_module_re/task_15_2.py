# -*- coding: utf-8 -*-
import re
from pprint import pprint
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
def parse_sh_ip_int_br(file_conf):
    '''
        - file_conf - конфигурационный файл
        - result - список кортежей 
    '''
    result = []
    #pattern_mash = re.compile(r"(?P<intf>\S+) +(?P<ip_add>\d.\d.\d.\d) +(?:YES|NO) +\S +(?P<status>(?:administratively down)|up|down) +(?P<protocol>up|down)")
    pattern_mash = re.compile(r"(?P<intf>\S+) +(?P<ip_add>(?:\d+.\d+.\d+.\d+)|unassigned) +(?:YES|NO) +\S+ +(?P<status>(?:administratively down)|up|down) +(?P<protocol>up|down)")                         
    with open(file_conf, "r") as conf_file:
        for line_conf in conf_file:
            match_conf = pattern_mash.match(line_conf)
            if match_conf:
                result.append(match_conf.group('intf', 'ip_add', 'status', 'protocol'))
                #result.append(match_conf.group('intf', 'ip_add'))
    return result

if __name__ == "__main__":
    #pprint (parse_sh_ip_int_br(r'.\Training_clone_natenca\exercises\15_module_re\sh_ip_int_br.txt'))
    print (parse_sh_ip_int_br(r'sh_ip_int_br.txt', 'r'))