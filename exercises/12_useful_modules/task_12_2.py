# -*- coding: utf-8 -*-
import subprocess
import ipaddress
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

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

list_of_ips = ["192.168.1.0", 
               "8.8.8.0-8.8.8.10", 
               "8.8.4.4-10",
               "232.22.1.34", 
               "8.5.7.1"]

if __name__ == "__main__":
    correct_ip_list = convert_ranges_to_ip_list(list_of_ips)
    print(ping_ip_addresses(correct_ip_list))
    #ipv4 = correct_ip('192.168.1.0')
    #print(ipv4)
    #result = convert_ranges_to_ip_list(['192.168.1.0-10'])
    #print(result)
