# 5. Определение палиндрома: Программа проверяет, является ли введенное
# слово или число палиндромом (читается одинаково в обоих направлениях).
# Пример: "radar" или 121 => палиндром.

from typing import Optional, Union

#  1 - usul
def check_polindrome(words: str) -> bool:
    return words == words[::-1]



# 2 - usul
def cheking_polindrome(words: Optional[Union[str, int]]) -> bool:
    """ Function for checking Palindrome """
    count, result = 0, " "
    if isinstance(words, int):
        words = str(words)
    for line in words.split():
        count += 1
        for i in range(len(words)-1, -1, -1):
            result += line[i]
    result = result.replace(" ", "").lower()
    if words == result:
        return True
    else:
        return False


text = "radar"

if cheking_polindrome(121):
    print("{}: палиндром".format(121))
else:
    print("{}: не палиндром".format(121))