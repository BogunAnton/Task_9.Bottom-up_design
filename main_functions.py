from array import array

from additional_functions import is_int, input_large_number, generate_random_number

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
    return True  # Возвращаем True, чтобы указать, что текст был введен

if __name__ == "__main__":
    array1 = []
    array2 = []
    input_two_mas(array1, array2)
