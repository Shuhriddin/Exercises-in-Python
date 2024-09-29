# 15. Нахождение максимального числа:
#     Напишите программу, которая находит самое большое число в последовательности чисел, введённых пользователем. Пример:
#     input: [3, 5, 7, 2, 8]
#     output: 8

from typing import List

def search_big_number(my_lst: List[int]) -> int:
    """ This function find big number in list """
    big_num = 0
    for i in my_lst:
        if i > big_num:
            big_num = i
    return big_num

print(search_big_number([3, 5, 7, 2, 8]))
