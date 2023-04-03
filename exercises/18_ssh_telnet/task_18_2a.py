# -*- coding: utf-8 -*-
"""
Задание 18.2a

Скопировать функцию send_config_commands из задания 18.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода информация о том
к какому устройству выполняется подключение.
По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства
из файла devices.yaml с помощью функции send_config_commands.
"""
import yaml
from pprint import pprint
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

def send_config_commands(device, config_commands, log=True):
    try:
        with ConnectHandler(**device) as ssh_session:
            ssh_session.enable()
            result = ssh_session.send_config_set(config_commands)
        if log == True:
            print(f"Подключаюсь к {device['host']}...")    
        return result
    except (NetmikoAuthenticationException, NetmikoTimeoutException) as error:
        print(error)    


if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    #with open("devices.yaml") as f:
    with open(r"C:\Users\user\Documents\Python\Training_Project\Training_clone_natenca\exercises\18_ssh_telnet\devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_config_commands(dev, commands))

