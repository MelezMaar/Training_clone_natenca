# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
conf_file = argv[1]
result = ''

with open(conf_file) as file:
    for conf_line in file:
        if '!' in conf_line:
            pass
        else:
            for ignore_conf in ignore:
                if ignore_conf in conf_line:
                    break
            else:
                result += conf_line

print(result)
