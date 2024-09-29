# 12. Проверка числа Армстронга:
#     Проверьте, является ли введённое пользователем число числом Армстронга. (Число Армстронга — это число, равное сумме кубов его цифр.) Пример:

#     input: 153
#     output: True
#     (153 = 1³ + 5³ + 3³)

x = 1**3 + 5**3 + 3**3

def func_armstronga(number: int) -> bool:
    """ This function returned boolen with checked armstrong """
    num_str, result = str(number), 0
    for i in num_str:
        nums = int(i)
        result += nums ** 3
    if result == number:
        return True
    return False

print(func_armstronga(153))