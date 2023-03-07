# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
conf_file = argv[1]
save_file_conf = argv[2]
result = ''

with open(conf_file) as file, open(save_file_conf, "w") as file_save:
    for conf_line in file:
        if '!' in conf_line:
            pass
        else:
            for ignore_conf in ignore:
                if ignore_conf in conf_line:
                    break
            else:
                file_save.write(conf_line)

#print(result)
