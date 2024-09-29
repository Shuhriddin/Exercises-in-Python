# 19. Проверка баланса скобок:
#     Проверьте, сбалансированы ли открытые и закрытые скобки ((), [], {}) в строке, введённой пользователем. Пример:
#     input: "(a + b) * (c / d)"
#     output: True


def checking_balance_brackets(letter: str) -> bool:
    """ This function for checking the balance of brackets """    
    stack = []
    matching_brackets = {')': '(', ']': '[', '}':'{'}
    for char in letter:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char in [")", "]", "}"]:
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    return not stack



s = "(a + b) * (c / d)"
print(checking_balance_brackets(s))  # True