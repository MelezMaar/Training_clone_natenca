# -*- coding: utf-8 -*-
import subprocess
import ipaddress
from tabulate import tabulate
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

def correct_ip (ip_address):
    '''
        Функция проверяет, является ли строка ip адресом
    '''
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False
  
def convert_ranges_to_ip_list(ip_list):
    result = []
    for ip_addr in ip_list:
        if '-' in ip_addr:
            min_ip, max_ip = ip_addr.split('-')
            ipv4_min = ipaddress.ip_address(min_ip)
            if correct_ip(max_ip):
                ipv4_max = ipaddress.ip_address(max_ip)
                while ipv4_min <= ipv4_max:
                    result.append(str(ipv4_min))
                    ipv4_min += 1
            else:
                for i in range(int(max_ip) + 1):
                    result.append(str(ipv4_min))
                    ipv4_min += 1        
        else:
            result.append(ip_addr)
    return result        

def ping_ip_addresses(ip_list):
    '''
        Функция получает в качестве аргумента список ip адресов
        она проверяет их  доступность и позвращает кортеж из двух списков
        первый список доступных адресов, а втрой недоступных
    '''
    available_ip = [] # Доступные адреса
    unavailable_ip = [] # недоступные адреса
    for ip_address in ip_list:
        command = subprocess.run(['ping', ip_address], stdout=subprocess.DEVNULL)
        if command.returncode == 0:
            available_ip.append(ip_address)
        else:
            unavailable_ip.append(ip_address)
    result = (available_ip, unavailable_ip)
    return result

def print_ip_table(reachable_list, unreachable_list):
    ip_dir = {}
    ip_dir['Reachable'] = reachable_list
    ip_dir['Unreachable'] = unreachable_list
    print(tabulate(ip_dir, headers="keys"))

list_of_ips = ["192.168.1.0", 
               "8.8.8.0-8.8.8.10", 
               "8.8.4.4-10",
               "232.22.1.34", 
               "8.5.7.1"]

if __name__ == "__main__":
    correct_ip_list = convert_ranges_to_ip_list(list_of_ips)
    reac, ureac = ping_ip_addresses(correct_ip_list)
    #ipv4 = correct_ip('192.168.1.0')
    #print(ipv4)
    #result = convert_ranges_to_ip_list(['192.168.1.0-10'])
    #print(result)
    print_ip_table(reac, ureac)