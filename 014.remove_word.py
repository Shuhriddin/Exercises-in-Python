# 14. Удаление повторяющихся слов:
#     Удалите повторяющиеся слова в строке, оставив только одно вхождение каждого. Пример:
#     input: "this is is a test test"
#     output: "this is a test"


def remove_dublicate(my_word: str) -> str:
    """ This function removed dublicate words """
    words = my_word.split()
    result = []
    for item in words:
        if item not in result:
            result.append(item)
    return " ".join(result)


print(remove_dublicate("this is is a test test"))