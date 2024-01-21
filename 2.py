#Задание 2
#Где-то неподалеку от центра Теней – этот район до сих пор не целиком нанесен на карту
#– расположен небольшой дворик. По крайней мере, здесь на стенках горят факелы, но
#проливаемый ими свет – это свет самих Теней: скупой, красноватый, с темной
#сердцевиной.
#Напишите функцию shadow(), которая из Света сделает Тень.
#В глобальной переменной district находится кортеж строк.
#Функция принимает произвольное количество аргументов строк и именованный
#параметр slice со значением по умолчанию 3
#Если у аргумента функции и стоящего на том же месте элемента кортежа есть общие
#символы, если на регистр не обращать внимания, то элемент кортежа заменяется на срез
#от начала аргумента длиной, равной значению параметра slice.
#Функция возвращает сумму исходных длин измененных элементов кортежа.

def shadow(*args, slice=3):
    global district
    length_sum = 0

    for i, arg in enumerate(args):
        if district[i].lower()[:slice].startswith(arg.lower()):
            length_sum += len(district[i])
            district[i] = district[i][:slice]

    return length_sum


district = ("No far from the center", "city map", "DARK Heart")
data = ["light", "world", "GREAT"]
result = shadow(*data)
print(result)  # Output: 33

district = ("wall", "dark-red", "bright lights", "Ank-Morpork")
data = ["magic", "shadows", "map", "tapping"]
result = shadow(*data, slice=5)
print(result)  # Output: 23
