# 8. Подсчет гласных и согласных: Программа считает количество
# гласных (а, е, и, о, у) и согласных букв в введенном слове.


vowels_letters = ['а', 'я', 'о', 'ё', 'у', 'ю', 'и', 'ы', 'э', 'е',]

text = "Правильное произношение слов — одна из составляющих красивой и грамотной речи"

def counter_volwes_and_consonants(letter: str) -> int:
    """ FUNCTION for Counter volwes and consinants """
    counts_volwes, counts_consonants = 0, 0
    for char in letter.lower().split():
        if char.isalpha():
            for i in char:
                if i in vowels_letters:
                    counts_volwes += 1
                else:
                    counts_consonants += 1

    return "гласных: {} шт и согласных: {} шт".format(counts_volwes, counts_consonants)


print(counter_volwes_and_consonants(text))
# гласных: 28 шт и согласных: 38 шт