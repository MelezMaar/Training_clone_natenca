# -*- coding: utf-8 -*-
import subprocess
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
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
               "8.8.8.8", 
               "8.8.4.4",
               "232.22.1.34", 
               "8.5.7.1"]

if __name__ == "__main__":
    print(ping_ip_addresses(list_of_ips))
