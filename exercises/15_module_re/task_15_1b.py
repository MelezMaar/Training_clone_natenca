# -*- coding: utf-8 -*-
import re
from pprint import pprint
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
def get_ip_from_cfg(file_conf):
    '''
        - file_conf - конфигурационный файл
        - result - список кортежей (ip , mask)
    '''
    result = {}
    pattern_mash = re.compile(r"interface (?P<intf>\S+)"
                              r"| ip address (?P<ip_add>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) (?P<ip_mask>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})")
    
    with open(file_conf, "r") as conf_file:
        intfs = 'none'
        for line_conf in conf_file:
            match_conf = pattern_mash.match(line_conf)
            if match_conf:
                if match_conf.lastgroup == 'intf':
                    #if result.get(intfs) != None and result[intfs] == []:
                        #del result[intfs] # удаляем интерфэйсы без ip. 
                    intfs = match_conf.group(match_conf.lastgroup)
                    result[intfs] = []
                else:
                    result[intfs].append(match_conf.group('ip_add', 'ip_mask'))
    return {key: value for key, value in result.items() if value != []}

if __name__ == "__main__":
    #pprint (get_ip_from_cfg(r'.\Training_clone_natenca\exercises\15_module_re\config_r1.txt'))
    print (get_ip_from_cfg(r'config_r2.txt', 'r'))
