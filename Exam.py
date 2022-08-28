# Задание 1. Используя стандартные арифметические операции представьте самое большое целое число из цифр 4, 4, 4 и приведите его значение.

a = 4
b = 4
c = 4
print(a + b + c)
print(a - b - c)
print(a / b / c)
print(a * b * c)
print(a ** b ** c)
print(a % b % c)
print(a // b // c)


# Задание 2. Написать программу для вычисления значения выражений. Проверить правильность выполнения задания с помощью тестовых значений.

a = int(input('Введите значение переменной а: '))
y = (((1 + a + (a ** 2)) / (2 * a +(a ** 2)) + 2) - (((1 - a + (a ** 2)) / (2 * a - (a ** 2))) ** -1)) * (5 - (2 * (a ** 2)) )
print(y)


import math
a = int(input('Введите значение переменной а: '))
B = int(input('Введите значение переменной B: '))
y = int(input('Введите значение переменной y: '))
y1 = math.sin(a + B - y)
y2 = math.sin(B + y - a)
y3 = math.sin(y + a - B)
y4 = math.sin(a + B + y)
Y = 0.25 * (y1 + y2 + y3 - y4)
print(Y)


# Задание 3. Создать пустую переменную. Проверить ее на истинность и ложность. Объясните полученный результат.

a = None
if a is None:
    print('It is True')
else:
    print('It is False, this is a different number')


#Задание 4. Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все числа от m до n включительно.

n = int(input('Введите значение переменной n: '))
m = int(input('Введите значение переменной m: '))
if m <= n:
    for i in range(m, n + 1):
        print(i)


# Задание 5. Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания, если m<n, или в порядке убывания в противном случае.

n = int(input('Введите значение переменной n: '))
m = int(input('Введите значение переменной m: '))
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)


# Задание 6. В строке “Иван Иванов” поменяйте местами слова. Может быть предоставлена любая строка с именем и фамилией, например: “Петр Иванов” => “Иванов Петр”.

string = str(input('Введите имя и фамилию'))
words = string.split()
words.reverse()
string = ' '.join(words)
print(string)


# Задание 7. Создать список с числами от 1 до 50 используя генератор списков.

red_moon = [i for i in range(0, 51)]
print(red_moon)



# Задание 8. Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5.

blue = [ 1, 5, 2, 9, 2, 9, 1]
blue_moon = [i for i in blue if blue.count(i) == 1]
print(blue_moon)


# Задание 9. Дан список [student1, student2, student3] с помощью цикла for добавить к каждому элементу списка слово “_good”. Вывести на экран.

arr = ['student_one, student_two, student_three']
arr_res = []
for i in arr:
    i += '_good'
    arr_res.append(i)
print(arr_res)


# Задание 10. Вывести на экран числа от 0 до 50, кроме 35.

blue_moon = [i for i in range(0, 51)]
blue_moon.remove(35)
print(blue_moon)


# Задание 11. Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”]. В новый список добавить элементы, которые содержат пробел.

hellcat = ['hello my friend', 'my name is', 'horse', 'cat', 'dog']
hellcat_res = []
for i in hellcat:
    if i.count(' ') < 1:
        break
    else:
        hellcat_res.append(i)
        print(hellcat_res)