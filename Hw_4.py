# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.

# def square(st_kvadrata):
#    perimetr = 4 * st_kvadrata
#    ploshad = 2 * st_kvadrata
#    diagonal = st_kvadrata * 1.4142
#    return perimetr, ploshad, diagonal
#
# print(square(5))
#

# from my_calc import *
# def square (storona_kvadrata):
#     perimetr = multiply(4, storona_kvadrata)
#     ploshad = multiply(2, storona_kvadrata)
#     diagonal = multiply(storona_kvadrata, 1.414)
#     return perimetr,ploshad,diagonal
# print (square(4))

# не понимаю!!!

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def lesta(name='John', last_name='Smith',age=35, position='web developer'):
#     return f' {name} \n {last_name} \n {age} \n {position}'
# print(lesta())

# def person():
#     return f'name:John \nlast_name:Smith \nage: 35 \nposition: web developer'
# message = person()
# print(message)


# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)



# def divide(my_list):
#     positive = []
#     negative = []
#     for i in my_list:
#         if i > 0:
#             positive.append(i)
#         elif i < 0:
#             negative.append(i)
#
#     return positive, negative
# my_list = [20, -3, 15, 2, -1, -21]
# pos, neg = divide(my_list)
# print(pos)
# print(neg)


# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

# my_list = [20, -3, 15, 2, -1, -21]
# multi = lambda a, b, c, d, e, f: a * b * c * d * e * f
# print(multi(20, -3, 15, 2, -1, -21))
#
#
# my_list = [20, -3, 15, 2, -1, -21]
# from functools import reduce
# res = reduce(lambda x, y: x*y, [20, -3, 15, 2, -1, -21])
# print(res)


# my_list = [20, 15, 2]

# multi = lambda a, b, c: a * b * c
# print(multi(20, 15, 2))


# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

