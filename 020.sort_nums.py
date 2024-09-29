# 20. Сортировка чисел по убыванию:
#     Отсортируйте числа в списке в порядке убывания. Пример:
#     input: [1, 5, 3, 2, 8, 6]
#     output: [8, 6, 5, 3, 2, 1]

from typing import List
import random

# 1-usul
def reverse_sort(nums: List[int]) -> List[int]:
    """ function for reverse sort """
    for run in range(len(nums)-1):
        for i in range(len(nums)-1-run):
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

numbers = [1, 5, 3, 2, 8, 6]
print(reverse_sort(
    numbers
))

# 2-usul
def reverse_sort_quick(nums: List[int]) -> List[int]:
    """ function for reverse sort """
    if len(nums) > 1:
        x = nums[random.randint(0, len(nums)-1)]
        left = [i for i in nums if i > x]
        center = [i for i in nums if i == x]
        right = [i for i in nums if i < x]
        result = reverse_sort(left) + center + reverse_sort(right)
    return result

print(reverse_sort_quick(numbers))
