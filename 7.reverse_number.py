# Переворачивание числа: Программа принимает число и
#  возвращает его в обратном порядке. Пример: 12345 => 54321

# number = 12345

# 1 - usul
def reverse_number(nums: int) -> int:
    """FUNCTION for REVERSE NUMBERS"""
    count, letter = 0, " "
    new_nums = str(nums)
    for _ in new_nums.split():
        for i in range(len(new_nums)-1, -1, -1):
            letter += new_nums[i]
        count = int(letter)
    return "{} => reversed: {}".format(nums, count)

# print(reverse_number(number))
# 12345 => reversed: 54321


#  2 - usul
def reverse_number_with_loop(nums: int) -> int:
    """FUNCTION for REVERSE NUMBERS WITH LOOP
    1-tsiklda new_num = 0 * 10 + 3 bo'ladi (new_num = 3)
    2-tsiklda new_num = 3 * 10 + 2 bo'ladi (new_num = 32)
    3-tsiklda new_num = 32 * 10 + 1 bo'ladi (new_num = 321)
    """
    new_nums = 0
    while nums > 0:
        back = nums % 10
        new_nums = new_nums * 10 + back
        nums //= 10
    return new_nums

number = 12345
print(reverse_number_with_loop(number))
# Пример: 12345 => 54321