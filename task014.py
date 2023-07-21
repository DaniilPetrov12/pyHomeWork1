# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int (input ('Введите число = '))
count = 0
squar = 2


for i in range (number):
    count = squar**i
    if count < number:
    
        print(count)    
    





