# -*- coding: utf-8 -*-
"""
Задание 18.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству
и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml
с помощью функции send_show_command (эта часть кода написана).

"""
import yaml
from pprint import pprint
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

def send_show_command(device, command):
    with ConnectHandler(**device) as ssh_session:
        ssh_session.enable()
        result = ssh_session.send_command(command)
    return result    


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
    #with open(r"C:\Users\user\Documents\Python\Training_Project\Training_clone_natenca\exercises\18_ssh_telnet\devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))
