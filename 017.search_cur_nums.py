# 17. Выделение составных чисел:
#     Найдите все составные числа в данной последовательности чисел и верните их в виде списка. (Составные числа — это числа, которые не являются простыми.) Пример:
#     input: [4, 5, 6, 7, 8]
#     output: [4, 6, 8]

from typing import List
from math import sqrt



def checking_prime_nums(num: int) -> bool:
    """ Проверяет, является ли число простым. """    
    n, i = num, 2
    simple = True
    while i <= sqrt(n):
        if n % i == 0:
            simple = False
            break
        i += 1
    if simple:
        return True
    else:
        return False


def search_any_number(nums: List[int]) -> List[int]:
    """ This function search number diveder owner """
    result = []
    if len(nums) > 0:
        for line in nums:
            if checking_prime_nums(line) == False:
                result.append(line)
            else:
                continue
        return result
    else:
        return None
        
print(search_any_number([4,5,6,7,8]))