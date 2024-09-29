# 13. Подсчёт количества букв:
#     Посчитайте количество каждой буквы в строке, введённой пользователем. Пример:
#     input: "hello world"
#     output: {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}

def cnt_letter(word: str) -> dict:
    """ This function counter letters """
    word = word.lower()
    result = {}
    for i in range(len(word)):
        if word[i] == " ":
            continue
        else:
            if word[i] in result:
                result[word[i]] += 1
            else:
                result[word[i]] = 1
    return result

text: str = "hello world"
print(cnt_letter(text))