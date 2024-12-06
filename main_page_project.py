"""
Главный файл проекта, содержащий меню для выбора задачи, ввода данных и выполнения алгоритмов.
"""

from main_functions import *
from additional_functions import is_int

def menu():
    """
    Основная функция меню, которая позволяет пользователю выбрать задачу, ввести данные и выполнить алгоритмы.
    """
    array1 = []
    array2 = []
    matrix = []
    choice_task = ''
    final_result = 0
    task_selected = False # Флаг для отслеживания выбора задачи
    data_entered = False  # Флаг для отслеживания ввода данных
    algorithm_executed = False  # Флаг для отслеживания выполнения алгоритма
    while True:
        print("Выберите пункт меню:\n"
              "1. Выбор задачи\n"
              "2. Ввод исходных данных, как вручную, так и сгенерированных случайным образом\n"
              "3. Выполнение алгоритма по заданию\n"
              "4. Вывод результата\n"
              "0. Завершение работы программы")
        choice = input()
        if is_int(choice):
            choice = int(choice)
        if choice == 1:
            print("Выберите номер задачи:\n"
                  "1. Входные данные: 2 массива с цифрами, каждый представляет собой большое число.\n"
                  "Нужно произвести сумму или разность массивов.\n"
                  "2. Входные данные: 2 массива с числами. Требуется проверить, сколько у массивов общих чисел.\n"
                  "Также, число будет считаться общим, если оно входит в один массив,\n"
                  "а в другом массиве находится его перевернутая версия.\n"
                  "3. Входные данные: матрица N на M. Требуется повернуть матрицу на 90\n"
                  "градусов против часовой или по часовой.")
            choice_task = input()
            if is_int(choice_task):
                choice_task = int(choice_task)
            task_selected = True
        elif choice == 2:
            if task_selected:
                if choice_task == 1:
                    array1, array2 = input_two_mas(array1, array2)
                    data_entered = True
                elif choice_task == 2:
                    array1, array2 = input_two_numbers_mas(array1, array2)
                    data_entered = True
                elif choice_task == 3:
                    matrix = get_matrix()
                    data_entered = True
                else:
                    print("error")
            else:
                print("Сначала выполните пункт 1.")
        elif choice == 3:
            if task_selected and data_entered:
                if choice_task == 1:
                    final_result = sum_or_difference_arrays(array1, array2)
                    algorithm_executed = True
                if choice_task == 2:
                    final_result = count_total_numbers(array1, array2)
                    algorithm_executed = True
                if choice_task == 3:
                    matrix = rotation_matrix(matrix)
                    algorithm_executed = True
                if algorithm_executed:
                    print("Алгоритм выполнен")
                else:
                    print("error")
            else:
                print("Сначала выполните пункты 1 и 2.")
        elif choice == 4:
            if task_selected and data_entered and algorithm_executed:
                if choice_task == 1:
                    print("Итог выполнения алгоритма:", final_result)
                if choice_task == 2:
                    print("Итог выполнения алгоритма:", final_result)
                if choice_task == 3:
                    print("Итог выполнения алгоритма:\n")
                    for row in matrix:
                        print(row)
            else:
                print("Сначала выполните пункты 1, 2, 3.")
        elif choice == 0:
            break
        else:
            print('error')

if __name__ == "__main__":
    menu()