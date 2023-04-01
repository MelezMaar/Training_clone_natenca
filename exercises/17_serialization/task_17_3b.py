# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий
для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно,
чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии,
но и удалять "дублирующиеся" соединения (их лучше всего видно на схеме, которую
генерирует функция draw_topology из файла draw_network_graph.py).
Тут "дублирующиеся" соединения, это ситуация когда в словаре есть два соединения:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Из-за того что один и тот же линк описывается дважды, на схеме будут лишние соединения.
Задача оставить только один из этих линков в итоговом словаре, не важно какой.

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии
с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть "дублирующихся" линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

import yaml
from pprint import pprint
from draw_network_graph import draw_topology

def unique_network_map (topology_dict):
    '''
        Функция удаляет зеркальные соединения топологии
    '''
    result_nt_map = topology_dict.copy() #Копируем словарь
    
    #Если мы находим имя ключа, равное одному из значений, то значение это ключа делаем пустым
    for key_nt_map, value_nt_map in result_nt_map.items():
        if value_nt_map != '' and result_nt_map.get(value_nt_map) != None:
            result_nt_map[value_nt_map] = ''

    # Выводим словарь БЕЗ пустых значений       
    return {key: value for key, value in result_nt_map.items() if value != ''}

def transform_topology(file_topolog):

    with open(file_topolog) as file:
        topolog = yaml.safe_load(file)
        
    result = {(device_name, local_intf_key): (device_id_key, port_id) 
              for device_name, local_intf in topolog.items() 
              for local_intf_key, device_id in local_intf.items()
              for device_id_key, port_id in device_id.items()}
    
    return unique_network_map(result)
    
if __name__ == "__main__":
    #pprint(transform_topology('topology.yaml'))
    draw_topology(transform_topology('topology.yaml'))