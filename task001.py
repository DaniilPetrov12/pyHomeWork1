# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

monet = int (input('Введите кол-во монеток = '))
min_monet = max_monet = 0
count = 0
for _ in range (monet):
    monet = randint(0, 1)
    print(monet, end = ' ')
    if monet == 0:
        min_monet += 1
    else : 
        max_monet += 1
if min_monet < max_monet:
    print(f'\n Количество монет, которое нужно перевернуть {min_monet}')
elif min_monet == max_monet:
    print(f'\n Безразницы, по {min_monet} ')    
else:
    print(f'\n Количество монет, которое нужно перевернуть {max_monet}')            
     
       
