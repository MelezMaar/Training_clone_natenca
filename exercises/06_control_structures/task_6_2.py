# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_user = input()

ip_oct_list = ip_user.split('.') #Разбиваем стоку на список октетов

f_local_broadcast = 0 #Вспомогательные переменные, показывают сколько из октетов равны 255 и 0 соответсвенно
f_unassigned = 0
# Пробегаемся по списку и выясняем, сколько октетов равны 255 и 0
for oct_ip in ip_oct_list:
     if int(oct_ip) == 255:
          f_local_broadcast +=1
     elif int(oct_ip) == 0:
          f_unassigned += 1
     else: 
         break       

result = '____'
# Собственно анализ данных и вывод результатов
if f_local_broadcast == 4:
     result = 'local broadcast'
elif f_unassigned == 4:
     result = 'unassigned'
elif int(ip_oct_list[0]) > 239:
     result = 'unused'
elif int(ip_oct_list[0]) > 223:
     result = result = 'multicast'    
elif int(ip_oct_list[0]) == 0:
     result = 'unused'
else:
     result = 'unicast'     

print(result)