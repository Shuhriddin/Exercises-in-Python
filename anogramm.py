

def check_anogram(first_word: str, second_word: str) -> bool:
    """Function for checking anogram"""
    first_result, second_result = list(first_word.lower()), list(second_word.lower())  
    if len(first_result) == len(second_result):
        count = 0
        for line in range(len(first_result)):
            if first_result[line] in second_result and second_result[line] in first_result:  # ikkala so`zdagi xar bir harf bor yoki yo`qligini tekshiradi
                count += 1
            else:
                count = 0
        print(count)
        if count == len(first_result) and count == len(second_result):
            return True
        else:
            return False
    else:
        return False
                


print(check_anogram("Solixov", "voxsoli"))