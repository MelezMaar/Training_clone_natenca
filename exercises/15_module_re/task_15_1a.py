# -*- coding: utf-8 -*-
import re
from pprint import pprint
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
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
            if result.get(intfs) != None and result[intfs] == ' ':
              del result[intfs] # удаляем интерфэйсы без ip.
            match_conf = pattern_mash.match(line_conf)
            if match_conf:
                if match_conf.lastgroup == 'intf':
                    intfs = match_conf.group(match_conf.lastgroup)
                    result[intfs] = ' '
                else:
                    result[intfs] = match_conf.group('ip_add', 'ip_mask')
    return result

if __name__ == "__main__":
    #pprint (get_ip_from_cfg(r'.\Training_clone_natenca\exercises\15_module_re\config_r1.txt'))
    print (get_ip_from_cfg(r'config_r1.txt', 'r'))
