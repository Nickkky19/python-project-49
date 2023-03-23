import random


GAME_RANDOM_RANGE = (2, 99)
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(temp_number):
    if temp_number == 2:
        return True
    for i in range(2, temp_number // 2 + 1):
        if not temp_number % i:
            return False
    return True


def make_expression():
    number = random.randint(*GAME_RANDOM_RANGE)
    result = is_prime(number)
    result = 'yes' if result else 'no'
    return result, number
