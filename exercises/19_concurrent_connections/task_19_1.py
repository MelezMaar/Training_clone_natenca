# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint

def ping_ip_address(ip_add):
    command = subprocess.run(['ping', ip_add], stdout=subprocess.DEVNULL)
    if command.returncode == 0:
        return ip_add, True
    else:
        return ip_add, False

def ping_ip_addresses(ip_list, limit=3): #limit
    '''
        Функция получает в качестве аргумента список ip адресов
        она проверяет их  доступность и позвращает кортеж из двух списков
        первый список доступных адресов, а втрой недоступных
    '''
    available_ip = [] # Доступные адреса
    unavailable_ip = [] # недоступные адреса
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_list = []
        for ip_address in ip_list:
            future = executor.submit(ping_ip_address, ip_address)
            future_list.append(future)
        for f in future_list:
            #print(f.result())
            if f.result()[1] == True:
                available_ip.append(f.result()[0])
            else:
                unavailable_ip.append(f.result()[0])
        
    result = (available_ip, unavailable_ip)
    return result

if __name__ == "__main__":
    
    list_of_ips = ["192.168.100.10", 
               "8.8.8.8", 
               "8.8.4.4",
               "192.168.100.1", 
               "192.168.100.4",
               "192.168.100.2",
               "192.168.100.3",]

    print(ping_ip_addresses(list_of_ips, 5))
