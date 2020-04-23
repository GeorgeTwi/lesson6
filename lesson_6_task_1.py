"""Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

 64 разрядная система.
 Версия Python - 3.8

 """

from sys import *


# Ф-ия по проверки памяти.
def show(a):
    res = getsizeof(a)
    print('\t', f'type={type(a)}, size={getsizeof(a)}, obj={a}')
    if hasattr(a, '__iter__'):
        if hasattr(a, 'items'):
            for key, val in a.items:
                res += show(key)
                res += show(val)
        elif not isinstance(a, str):
            for i in a:
                res += show(i)
    return res


# __________________________________________________________________________________


# Урок 3, задание 3
list = [-89, -65, -62, -63, -95, -74, -69, -79, -50]
MAX = list[0]

print(list)

for idx in list:
    if MAX < idx:
        MAX = idx

MIN = MAX

for idx in list:
    if idx < MIN:
        MIN = idx

list[list.index(MAX)], list[list.index(MIN)] = list[list.index(MIN)], list[list.index(MAX)]
print(list)
print(f'Выделено байтов на переменные: {show(list)}') # Общее кол-во памяти выделено на переменные: 380 байт



print('-' * 60)
# __________________________________________________________________________________

# Урок 3, задание 5
COUNT = 1
num = None

list_numbers = (11, 13, 87, 23, 99, 99, 9, 71, 70, 23, 92, 23)

for i in range(len(list_numbers) - 1):
    temp_count = 1
    for idx in range(i + 1, len(list_numbers)):
        if list_numbers[i] == list_numbers[idx]:
            temp_count += 1
    if temp_count > COUNT:
        COUNT = temp_count
        num = list_numbers[i]


print(f'Число {num} повторялось {COUNT} раз(а)')
print(f'Выделено байтов на переменные: {show(list_numbers)}')        #Общее кол-во памяти выделено на переменные: 472 байт
#

# __________________________________________________________________________________
print('-' * 60)

def some(num):
    count = 1
    current_prime = 2
    count_byte = show(current_prime)

    while count < num:
        current_prime += 1
        count_byte += show(current_prime)
        for i in range(2, current_prime):
            if current_prime % i == 0:
                break

        else:
            count += 1

    return current_prime, count_byte



numb = 10
print(f'Выделено байтов на переменные: {some(numb)[1]}')      #Общее кол-во памяти выделено на переменные: 784 байт