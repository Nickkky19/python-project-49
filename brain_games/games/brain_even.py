from brain_games.games import games_functions


GAME_RANDOM_RANGE = (1, 99)
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_expression():
    number = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    result = games_functions.is_even(number)
    result = 'yes' if result else 'no'
    return result, number
