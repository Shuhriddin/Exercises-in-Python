# Переворачивание букв в словах: Введите текст, и программа перевернет
# буквы в каждом слове, сохранив порядок слов. Пример: "hello world" => "olleh dlrow"

# "double  spaces"      ==> "elbuod  secaps"

text = "double  spaces"

def reverse_text(letter: str) -> str:
    """REVERSED TEXT"""
    result = ""
    for line in letter.split():
        letter = ""
        for char in range(len(line)-1, -1, -1):
            if line[char] == " ":
                continue
            letter += line[char]
        result += letter + " "
    return result

print(reverse_text(text))
# "double  spaces"      ==> "elbuod  secaps"
letr = "his is an example!"
print(reverse_text(letr))
# "This is an example!" ==> "sihT si na !elpmaxe"