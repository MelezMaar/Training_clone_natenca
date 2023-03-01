# -*- coding: utf-8 -*-
"""
Задание 5.1d

Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра,
пользователь мог вводить название параметра в любом регистре.

Пример выполнения скрипта:
$ python task_5_1d.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): IOS
15.4


Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно
решить без использования условия if.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

equip = input ("Введите название устройства: ").lower() #Собственно понижаем регистр сразу при вводе
equip_chr = london_co.copy() #Копируем, что бы не изменять начальный словарь
equip_chr.setdefault(equip, {'Non': 'non'}) # при ошибке ввода устройства, не вываливается в ошибку, а создается новый элемент
charac_list = list(equip_chr[equip].keys()) #Получаем список ключей
charac = input ('Введите параметор устройства (' + str(charac_list)[1:-1].replace("'", '') + '): ').lower()
equip_chr[equip].setdefault(charac, 'Такого параметра нет')#Выдает осмысленное сообщение при неверных параметрах
print(equip_chr[equip][charac]) 
del equip_chr[equip] # Убираем за собой