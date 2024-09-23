# Подсчет слов в тексте: Программа считает, сколько раз каждое слово
#  встречается в тексте. Пример: "hello world hello" => {"hello": 2, "world": 1}

text = "hello world hello hello"

def counter_words(word: str) -> dict:
    """FUNCTION for COUNTER WORDS"""
    word_dict = {}
    for letter in word.split():
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
    return word_dict

print(counter_words(text))
# {'hello': 3, 'world': 1}
