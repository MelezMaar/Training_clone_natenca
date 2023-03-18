# -*- coding: utf-8 -*-
import re
from pprint import pprint
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
def generate_description_from_cdp(file_conf):
    '''
        - file_conf - конфигурационный файл
        - result - список 
    '''
    result = {}
    pattern_mash = re.compile(r"(?P<dev>\S+) +"
                              r"(?P<l_intf>Eth \S+) +"
                              r".+(?P<port>Eth \S+)")
    
    pattern_desc = 'description Connected to {0} port {1}'
    
    
    with open(file_conf, "r") as conf_file:
        for line_conf in conf_file:
            match_conf = pattern_mash.match(line_conf)
            if match_conf:
                intfs = match_conf.group('l_intf')
                dev, port = match_conf.group('dev', 'port')
                result[intfs] = pattern_desc.format(dev, port)
    return result

if __name__ == "__main__":
    #pprint (get_ip_from_cfg(r'.\Training_clone_natenca\exercises\15_module_re\sh_cdp_n_sw1.txt'))
    print (generate_description_from_cdp(r'sh_cdp_n_sw1.txt', 'r'))
