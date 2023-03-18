# -*- coding: utf-8 -*-
import re
from pprint import pprint
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
def convert_ios_nat_to_asa(nat_cisco, nat_asa):
    result = ''
    pattern_asa ='object network LOCAL_{0}\n host {0}\n nat (inside,outside) static interface service tcp {1} {2}\n'
    #pattern_asa = '{0} {1} {2}'          
    pattern_mash = re.compile(r'(?:\S+ ){6}(?P<ip_add>\d+.\d+.\d+.\d+) (?P<in_port>\d+) \S+ \S+ (?P<out_port>\d+)')
    #pattern_mash = re.compile(r'(?:\S+ ){6}(?P<ip_add>\d+.\d+.\d+.\d+)')
    with open(nat_cisco) as conf_cisco, open(nat_asa, 'w') as conf_asa:
        for cisco_conf in conf_cisco:
            mathe_conf = pattern_mash.match(cisco_conf)
            if mathe_conf:
                ip, inp, outp = mathe_conf.group('ip_add', 'in_port', 'out_port')
                conf_asa.writelines(pattern_asa.format(ip, inp, outp))
                #result += str(ip)
                
        

if __name__ == "__main__":
    #convert_ios_nat_to_asa(r'.\Training_clone_natenca\exercises\15_module_re\cisco_nat_config.txt', r'.\Training_clone_natenca\exercises\15_module_re\asa_nat_config.txt')
    convert_ios_nat_to_asa(r'cisco_nat_config.txt', r'asa_nat_config.txt')
    #print (parse_sh_ip_int_br(r'sh_ip_int_br.txt', 'r'))