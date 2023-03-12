# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    #Удаляем "шапку"
    conf_list = [ist for ist in command_output.split('\n') if ist != '' and ist.startswith(('Capability Codes', 'Device ID', '   ')) == False]

    result = [] # будет максимально удобный список списков, для последующей удобной обработки

    # делим строку на список, по двойному пробелу. Тем самым названия портов будут как одна строка, а не две разные
    for conf_line in conf_list:
        result.append([conf_element.strip() for conf_element in conf_line.split('  ') if conf_element != '' ]) 

    # Костыль, когда имя платформы и имя интерфэйса разделены одним пробелом, а не двумя
    # Исправляет эту "багу"
    for ind, conf_list in enumerate(result):
        if len(conf_list) == 5: 
            result[ind].append('')               
            result[ind][4], result[ind][5] = cut_str(conf_list[4])

    parse_cdp_result = {}  # Собственно будет итоговый сдловарь
    main_dev = cut_str(result[0][0], '>')[0]  # Имя устройства, с которого передавались данные
    #Формирование словаря
    for inx_pars in range(1, len(result)):
        key_dev = (main_dev, result[inx_pars][1].replace(' ', ''))    
        value_dev = (result[inx_pars][0], result[inx_pars][5].replace(' ', ''))
        parse_cdp_result[key_dev] = value_dev
        # Не забываем удалять кортежы
        del value_dev 
        del key_dev
    
    return parse_cdp_result

def cut_str (obg_str_line, cut_token=' '):
    ''' Функция, которая делит строку на двое, по указанному
            obg_str_line - строка, которую надо разделить
            cut_token - символ, по которуму надо разделить
            return - список из двух элементов
                cut_list[0] - первая часть строки до указанного символа 
                cut_list[1] - часть строки после указанного символа
    '''
    cut_list = []
    cut_list.append(obg_str_line.split(cut_token)[0])
    cut_list.append(obg_str_line[len(cut_list[0])+1:])
    return cut_list
    
def print_list(list_str):
    # Вспомогательная функция для более очевидного вывода списков
    for i, obj_print in enumerate(list_str):
        print(f'{i:<3} ' , end=' ' )
        print(obj_print)

#sh_cdp_n_r1.txt  
#sh_cdp_n_sw1.txt 
#.\Training_clone_natenca\exercises\11_modules\

if __name__ == "__main__":
    with open(r"h_cdp_n_sw1.txt") as f:
            print(parse_cdp_neighbors(f.read()))
  



    #print_list(conf_list)
    #print_list(result)
    #print_list(cut_str(str(result[0]), '>'))
    #test = cut_str(str(result[0]), '>')
    #print(cut_str(result[0][0], '>'))
    #print(parse_cdp_result)