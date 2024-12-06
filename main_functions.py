from additional_functions import *
"""import numpy as np"""

def input_two_mas(array1, array2):
    print("Выберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы случайным образом\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == 1:
        # Ввод двух больших чисел вручную
        array1 = input_large_number()
        array2 = input_large_number()
    elif option == 2:
        # Генерация двух больших чисел случайным образом
        length1 = int(input("Введите количество цифр в случайном массиве: "))
        array1 = generate_random_number(length1)
        length2 = int(input("Введите количество цифр в случайном массиве: "))
        array2 = generate_random_number(length2)
    else:
        print('error')
    print("Первый массив цифр:", array1)
    print("Второй массив цифр:", array2)
    return array1, array2  # Возвращаем True, чтобы указать, что текст был введен

def sum_or_difference_arrays(array1, array2):
    print("Выберите находить сумму или разность массивов:\n"
          "1. Сумму\n"
          "2. Разность")
    sum_or_difference = input()
    if is_int(sum_or_difference):
        sum_or_difference = int(sum_or_difference)
    if sum_or_difference == 1:
        sum1 = sum(number for number in array1)
        sum2 = sum(number for number in array2)
        return sum1+sum2
    if sum_or_difference == 2:
        sum1 = sum(number for number in array1)
        sum2 = sum(number for number in array2)
        return sum1-sum2

def input_two_numbers_mas(array1, array2):
    print("Выберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы случайным образом\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == 1:
        array1 = input_number_array()
        array2 = input_number_array()
    elif option == 2:
        # Генерация двух больших чисел случайным образом
        length1 = int(input("Введите количество цифр в случайном массиве: "))
        array1 = generate_random_array(length1)
        length2 = int(input("Введите количество цифр в случайном массиве: "))
        array2 = generate_random_array(length2)
    else:
        print('error')
    print("Первый массив:", array1)
    print("Второй массив:", array2)
    return array1, array2  # Возвращаем True, чтобы указать, что текст был введен

def count_total_numbers(array1, array2):
    result = 0
    for i in array1:
        for j in array2:
            if i == j or str(i)[::-1] == str(j):
                result += 1
    return result

def get_matrix():
    # Запрос у пользователя, хочет ли он ввести матрицу вручную или сгенерировать её случайным образом
    print("Выберите опцию 1-2:\n"
          "1. Ввести матрицу самостоятельно\n"
          "2. Сгенерировать матрицу случайным образом\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == 1:
        # Ввод матрицы вручную
        matrix = input_matrix()
        print("Начальная матрица:\n")
        return matrix
    elif option == 2:
        matrix = generate_random_matrix()
        print("Начальная матрица:\n")
        for row in matrix:
            print(row)
        return matrix
    else:
        print("error")

def rotation_matrix(matrix):
    transposed_matrix = transpose_list_comprehension(matrix)
    rotated_matrix = []
    for row in transposed_matrix[::-1]:
        rotated_matrix.append(row)
    return rotated_matrix