# 18. Подсчёт палиндромов:
#     Определите, сколько палиндромов содержится в строке, введённой пользователем. Пример:
#           input: "radar level kayak racecar"
#           output: 4

from typing import Optional, Union

# Function for checking polindrome
def check_polindrome(words: Optional[Union[str, int]]) -> bool:
    """ Function for checking polindrome """
    count, result = 0, ""
    if isinstance(words, int):
        words = str(words).lower()   # Constant must be diference with arguments

    for line in words.split():      
        count += 1
        for i in range(len(words)-1, -1, -1):
            result += line[i]

    if words != result:
        return False
    return True

print(check_polindrome(121))


def counter_polindrome(letter: Optional[Union[str, int]]) -> int:
    """ Function for counting polindrome """
    count = 0
    my_letter = letter.split()
    for line in my_letter:
        if check_polindrome(line):
            count += 1
    return count

print(counter_polindrome("radar level kayak racecar"))