# Задание 2. Даны два кортежа: C_1 = (35, 78,21,37, 2,98, 6, 100, 231). C_2 = (45, 21,124,76,5,23,91,234). Необходимо определить: 1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..) 2) Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей.

C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
a = sum(C_1)
print(a)
b = sum(C_2)
print(b)
if a > b:
    print('Сумма чисел больше в кортеже С_1')
else:
    print('Сумма чисел больше в кортеже С_2')
print('max', max(C_1), 'min', min(C_1))
print('max', max(C_2), 'min', min(C_2))



# Задание 3. Напишите программу, демонстрирующую работу try\except\finally.

try:
    a = int(input('Введите число'))
    b = int(input('Введите число'))
    c = a / b
    print(c)
except ZeroDivisionError:
    c = 0
    print('Результат деления на ноль',c)
except Exception:
    print('Общее исключение')
finally:
    print('Работа программы завершена')



# Задание 4. Создайте 2 множества: Если они одинаковые: вывести что они равны. Если 1 множество полностью состоит из второго: вывести сообщение множество 1 состоит из множества 2.

a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 15, 17}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 15, 17}
if a == b:
    print('a = b')
else:
    print('a =! b')



# Задание 5. Создайте словарь из строки ' An apple a day keeps the doctor away'    следующим образом: в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

a = 'An apple a day keeps the doctor away'
gold_apple = {symbol: a.count(symbol) for symbol in a}
print(gold_apple)



# Задание 6. Ввести 10 чисел, данные числа добавить их во множество.

import random
b = [random.randint(0, 11) for i in range(10)]
f = set(b)
print(f)



# Задание 7. Найти самое длинное слово в строке.

g = 'How are u?'
u = g.split()
id_longest = 0
y = 0
for i in u:
    if len(u) < len(u[y]):
        id_longest = y
    y += 1
print(u[id_longest])



# Задание 8. Есть словарь песен группы Depeche Mode violator songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }. Выведите общее время звучания всех песен. Создайте список песен, время звучаниях которых больше 5 минут Создайте новый словарь тех песен, в название которых состоит из одного слова.

Depeche_Mode_violator_songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
rtm = 1
for key in Depeche_Mode_violator_songsdict:
    rtm = rtm + Depeche_Mode_violator_songsdict[key]
print(rtm)
print([x[0] for x in filter(lambda x: x[1] > 5, Depeche_Mode_violator_songsdict.items())])
print(dict(filter(lambda x: len(x[0].split()) == 1, Depeche_Mode_violator_songsdict.items())))