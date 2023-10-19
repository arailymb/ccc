#task 1.1
user_input = input("enter string without whitespaces: ")

result_tuple = tuple(user_input)

print("tuple:")
print(result_tuple)

#преобразовалa строку в кортеж
#использовав встроенную функцию 
#которая конвертирует каждый символ строки в элемент кортежа

#task 1.2
tuple_input = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')

result_string = ''.join(tuple_input)

print("The string is:", result_string)

#преобразовалa кортеж символов обратно в строку
#c помощью метода join(), объединилa все элементы кортежа в одну строку

#task 1.3
tuple_A = (1,2,3,4,5,6,7)
tuple_B = (5,6,7,9,7,1,10,10)

half_length_A = len(tuple_A) // 2
half_length_B = len(tuple_B) // 2

first_half_A = tuple_A[:half_length_A]
second_half_B = tuple_B[half_length_B:]

result_tuple = first_half_A + second_half_B

print(result_tuple)

#объединилa первую половину кортежа сo второй
#чтобы определить, где находится середина каждого кортежа, я использовалф целочисленное деление 
#затем я объединила обе части, используя +

#task 1.4
def count_elements(input_tuple):
    count_dict = {}
    for elem in input_tuple:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1

    result_tuple = tuple((key, value) for key, value in count_dict.items())
    
    return result_tuple

samples = [
    (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6),
    ('55', '6', '777', 54, 6, 7777, 9, 777, 6),
    ((1,2,3), (['A', 'B']), (1,2,3), (['A']))
]

for sample in samples:
    print("Elements and their occurrences:")
    print(count_elements(sample))
    print()

#подсчитала количество раз, которое каждый элемент встречается в кортеже
#для этого я создала функцию, где через цикл, мы проверяем каждый элемент кортежа

#task 1.5
sample_input = (55, 6, 777, 70.0, '7', 'A')

int_tuple = ()
float_tuple = ()
str_tuple = ()

for item in sample_input:
    if isinstance(item, int):  
        int_tuple += (item,)
    elif isinstance(item, float):  
        float_tuple += (item,)
    elif isinstance(item, str):  
        str_tuple += (item,)

print(int_tuple)
print(float_tuple)
print(str_tuple)

#разделила элементы кортежа на три категории: целые числа, числа с плавающей точкой и строки
#чтобы это сделать, я проверил тип каждого элемента с помощью функции isinstance()

#task 2.1
user_input = input("Введите строку без пробелов: ")

result_set = {char for char in user_input}

print("Created set is:")
print(result_set)

#преобразовала строку в множество.
#для этого я использовала циул который проходи через строку и добавляет каждый символ строки в множество

#task 2.2
set_A = {1,2,3,4,5}
set_B = {5,7,8,9,2,10}

result_set = set_A ^ set_B

print(result_set)

#нужно было найти симметричную разность между двумя множествами
#использовала готовый оператор ^

#task 2.3
set_A = {1,2,3,4,5}
set_B = {5,7,8,9,2,10}

result_set = set_A - set_B

print(result_set)

#нашла разницу между двумя множествами
#использовала готовый оператор -

#task 2.4
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}

for elem in set_C:
    if elem in set_A:  
        set_A.remove(elem)  
        set_B.add(elem)

print("Updated set_B =", set_B)

#удалила из множества A все элементы
#которые присутствуют в множестве C, и добавил их в множество B через цикл

#task 2.5
from itertools import combinations, islice

A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5

result = list(islice(map(set, combinations(A, n)), m))

print(result)

#создала список комбинаций заданной длины из множества A и ограничил количество комбинаций числом m
#для этого использовала функции combinations и islice из модуля itertools

#task 3.1
from itertools import groupby

cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

sorted_cars = sorted(cars_list, key=lambda x: x[0])

for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):
    models = list(group)
    print(manufacturer, len(models))
    for _, model in models:
        print(f"- {model}")

#сгруппировала список автомобилей по производителю
#для этого сначала отсортировала список по производителю
#а затем использовала функцию groupby из модуля itertools, чтобы сгруппировать автомобили по бренду

