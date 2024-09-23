text = "Shuxriddin Solixov"

def counter_words(word: str) -> int:
    """COUNTER LETTERS"""
    new_word = word.split()
    all_count = 0
    for line in new_word:
        count = 0
        for char in range(len(line)):
            if line[char] == " ":
                continue
            else:
                count += 1
        all_count += count
    result = "{} => textidagi harflar soni: {} ta".format(word, all_count)
    return result

print(counter_words(text))
# Shuxriddin Solixov => textidagi harflar soni: 17 ta
