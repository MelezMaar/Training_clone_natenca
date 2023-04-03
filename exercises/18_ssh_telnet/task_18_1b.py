# -*- coding: utf-8 -*-
"""
Задание 18.1b

Скопировать функцию send_show_command из задания 18.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется при ошибке
аутентификации на устройстве, но и исключение, которое генерируется, когда IP-адрес
устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться
сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""
import yaml
from pprint import pprint
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh_session:
            ssh_session.enable()
            result = ssh_session.send_command(command)
        return result
    except (NetmikoAuthenticationException, NetmikoTimeoutException) as error:
        print(error)    


if __name__ == "__main__":
    command = "sh ip int br"
    #with open("devices.yaml") as f:
    with open(r"C:\Users\user\Documents\Python\Training_Project\Training_clone_natenca\exercises\18_ssh_telnet\devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))
