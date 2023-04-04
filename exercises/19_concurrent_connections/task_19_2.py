# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""

from concurrent.futures import ThreadPoolExecutor
import yaml
from pprint import pprint
from netmiko import (ConnectHandler)

def send_show_command(device, command):
    with ConnectHandler(**device) as ssh_session:
        ssh_session.enable()
        result = ssh_session.find_prompt() + command + '\n'
        result += ssh_session.send_command(command) + '\n'
        
    return result

def send_show_command_to_devices(devices, command, filename, limit=3):
        #with open(devices) as f:
            #devices_list = yaml.safe_load(f)
        with ThreadPoolExecutor(max_workers=limit) as executor:
            future_list = []
            for device in devices:
                future = executor.submit(send_show_command, device, command)
                future_list.append(future)
            result = [f.result() for f in future_list]    
        with open (filename, 'w') as result_file:
             result_file.writelines(result)    

if __name__ == "__main__":
    with open(r"C:\Users\user\Documents\Python\Training_Project\Training_clone_natenca\exercises\19_concurrent_connections\devices.yaml") as f:
        devices_list = yaml.safe_load(f)
    send_show_command_to_devices(devices_list,
                                'sh ip int br', 
                                r"C:\Users\user\Documents\Python\Training_Project\Training_clone_natenca\exercises\19_concurrent_connections\result.txt", 3)


    