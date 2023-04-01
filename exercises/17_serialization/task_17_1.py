# -*- coding: utf-8 -*-
import re
import os
import csv
from pprint import pprint

"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
def get_decp_snoop_file(filename):
    '''
        Функция обрабатывает файл и возвращвет список котрежей с нужными
        данными
        - filename - имя файла
        - result - список кортежей
    '''
    result = []
    pattern_marh = re.compile(r"(?P<mac_add>(?:\w\w:){5}\w\w) +"
                              r"(?P<ip_add>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) +\d+ +\S+ +"
                              r"(?P<vlan_add>\d{1,4}) +"
                              r"(?P<intf>\S+)")
    with open (filename) as snoop_file:
        for snoop_line in snoop_file:
            mash_snoop = pattern_marh.match(snoop_line)
            if mash_snoop:
                #pprint (mash_snoop.group('mac_add', 'ip_add', 'vlan_add', 'intf'))
                result.append(list(mash_snoop.group('mac_add', 'ip_add', 'vlan_add', 'intf')))

    return result

def write_dhcp_snooping_to_csv (filenames, output): 
    '''
        - filename список файлов
        - output файл для записи
    '''
    snoop_svg_list = [['switch', 'mac', 'ip', 'vlan', 'interface']] # шапка
    mach_file_name = re.compile(r"(\w+)_dhcp_snooping.txt") # Шаблон для имени устройства
    for snoop_file in filenames:
        device_list = [mach_file_name.search(snoop_file).group(1)]
        #print (mach_file_name.match(snoop_file).group(1))
        #pprint(str(snoop_file).split('_')[0])
        for device_line in get_decp_snoop_file(snoop_file):
            snoop_svg_list.append(device_list + device_line)

    with open(output, 'w') as f:
        writer = csv.writer(f, lineterminator='\n') 
        writer.writerows(snoop_svg_list)   
       

if __name__ == "__main__":
    file_catalog = r'c:\Users\user\Documents\Python\Training_Project\Training_clone_natenca\exercises\17_serialization' #Каталог где лежат файлы
    # Формирует список нужных файлов
    snoop_list_file = [snoop_file for snoop_file in os.listdir(file_catalog) if '_dhcp_snooping.txt' in snoop_file]
    
    write_dhcp_snooping_to_csv(snoop_list_file, r'c:\Users\user\Documents\Python\Training_Project\Training_clone_natenca\exercises\17_serialization\output.scv')