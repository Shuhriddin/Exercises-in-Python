# 9. Задача "FizzBuzz" на Python: Выведите числа от 1 до 100, заменяя числа, кратные 3, на "Fizz",
#  числа, кратные 5, на "Buzz", а кратные 3 и 5 одновременно — на "FizzBuzz".

def get_game(numbers: int):
    """FIZZBUZZ game"""    
    FIZZ = "Fizz"
    BUZZ = "Buzz"
    FIZZBUZZ = "FizzBuzz"
    for number in range(numbers+1):
        if number % 3 == 0 and number % 5 == 0:
            print(FIZZBUZZ)
        elif number % 3 == 0:
            print(FIZZ)
        elif number % 5 == 0:
            print(BUZZ)
        else:
            print(number)
    
        
get_game(100)