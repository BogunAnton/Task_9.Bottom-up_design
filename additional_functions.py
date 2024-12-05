from array import array
import random

def is_int(choice):
    """ Проверка на то, что s - целое число"""
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False

def input_large_number():
    # Ввод строки, представляющей большое число
    number_str = input("Введите большое число: ")
    # Преобразование строки в массив цифр
    number_array = [int(number) for number in number_str]
    return number_array

def generate_random_number(length):
    # Генерация случайного большого числа заданной длины
    number_str = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    # Преобразование строки в массив цифр
    number_array = [int(digit) for digit in number_str]
    return number_array
