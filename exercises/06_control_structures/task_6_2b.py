# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_user_correct = False #Если истинна, то ip введено верно, ввод корректен
#ip_user = '10...10.400'

while ip_user_correct == False:
     ip_user = input("Введите ip: ")
     if len(ip_user) > 15: #Проверяем длинну
          print('Неправильный IP-адрес')
     elif ip_user.count('.') != 3: #проверяем количество точек
          print('Неправильный IP-адрес')
     else:
          ip_oct_list = ip_user.split('.') #Разбиваем стоку на список октетов
          for i in range(4):
               if ip_oct_list[i].isdigit() == False: # Проверяем, являются ли данные числами
                    print('Неправильный IP-адрес')
                    break
               else: # провлеряем диапозон данных
                    ip_oct_list[i] = int(ip_oct_list[i])
                    if ip_oct_list[i] > 255:
                        print('Неправильный IP-адрес')
                        break
                    elif ip_oct_list[i] < 0:
                       print('Неправильный IP-адрес')
                       break  
          else:
               ip_user_correct = True
                    
#print (ip_oct_list)
          
if ip_user_correct == True:
     f_local_broadcast = 0 #Вспомогательные переменные, показывают сколько из октетов равны 255 и 0 соответсвенно
     f_unassigned = 0
     # Пробегаемся по списку и выясняем, сколько октетов равны 255 и 0
     for oct_ip in ip_oct_list:
          if oct_ip == 255:
               f_local_broadcast +=1
          elif oct_ip == 0:
               f_unassigned += 1
          else: 
               break       

     result = '____'
     # Собственно анализ данных и вывод результатов
     if f_local_broadcast == 4:
          result = 'local broadcast'
     elif f_unassigned == 4:
          result = 'unassigned'
     elif ip_oct_list[0] > 239:
          result = 'unused'
     elif ip_oct_list[0] > 223:
          result = result = 'multicast'    
     elif ip_oct_list[0] == 0:
          result = 'unused'
     else:
          result = 'unicast'     
else:
     result = 'Неправильный IP-адрес' 
print(result)