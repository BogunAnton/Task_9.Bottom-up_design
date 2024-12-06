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
    #number_str = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    # Преобразование строки в массив цифр
    number_array = [random.randint(0, 9) for _ in range(length)]
    return number_array

def input_number_array():
    # Ввод строки, содержащей числа, разделенные пробелами
    input_str = input("Введите числа, разделенные пробелами: ")
    # Разделение строки на отдельные числа и преобразование их в целые числа
    number_array = [int(number) for number in input_str.split()]
    return number_array

def generate_random_array(length):
    # Генерация случайного массива чисел от 1 до 100 заданной длины
    number_array = [random.randint(1, 100) for _ in range(length)]
    return number_array

def input_matrix():
    # Ввод размеров матрицы
    m = int(input("Введите количество строк (m): "))
    n = int(input("Введите количество столбцов (n): "))
    # Ввод матрицы
    matrix = []
    print("Введите элементы матрицы по строкам (разделенные пробелами):\n"
          "В каждой строке должно быть по", n, "элементов")
    for i in range(m):
        while True:
            row = list(map(int, input(f"Строка {i+1}: ").split()))
            if len(row) == n:
                matrix.append(row)
                break
            else:
                print(f"Ошибка: Введено неверное количество элементов в строке {i+1}. Пожалуйста, введите {n} элементов.")
    return matrix

def generate_random_matrix():
    m = random.randint(1, 10)
    n = random.randint(1, 10)
    # Генерация случайной матрицы
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]
    return matrix

def transpose_list_comprehension(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

#Hi