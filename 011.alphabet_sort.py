# 11. Сортировка слов по алфавиту: Отсортируйте слова в строке, введённой пользователем, по алфавиту и верните результат. Пример:

#     input: "hello from the other side"
#     output: "from hello other side the"


def sorted_alphabet(letter):
    """ This function sorted with alphabet """
    new_letter = letter.split()
    new_letter = sorted(new_letter)
    result = ""
    for word in new_letter:
        result += word + " "
    return result.strip()


text = "hello from the other side"
print(text)
print(sorted_alphabet(text))