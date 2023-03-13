from brain_games.games import games_functions


GAME_RANDOM_RANGE = (2, 99)
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_expression():
    number = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    if number == 2:
        return 'yes', number
    for i in range(2, number // 2 + 1):
        if not number % i:
            return 'no', number
    return 'yes', number
