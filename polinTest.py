from typing import Optional, Union

def check_polin(word: Optional[Union[int, str]]) -> bool:
    """check polin"""
    if word is None:
        return False
    if isinstance(word, int):
        word = str(word)

    result, count = "", 0
    for line in word.split():
        london = ""
        count += 1
        for i in range(len(word)-1, -1, -1):
            london += line[i]
        result += london
    if word == result:
        return True
    else:
        return False
    
if check_polin(455):
    print("{} POLINDROME!".format(455))
else:
    print("{} No Wrong!".format(455))
