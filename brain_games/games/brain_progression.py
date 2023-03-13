from brain_games.games import games_functions


GAME_RANDOM_RANGE = (1, 99)
PROGRESSION_LENGTH_RANDOM_RANGE = (5, 15)
DESCRIPTION = 'What number is missing in the progression?'


def make_expression():
    progression_length = games_functions.get_random_value_by_range(PROGRESSION_LENGTH_RANDOM_RANGE)
    progression_start = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    progression_step = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    result_list = [progression_start]
    for i in range(progression_length):
        result_list.append(result_list[i] + progression_step)
    temp_idnex = games_functions.get_random_value_by_range((0, progression_length - 1))
    result = result_list[temp_idnex]
    result_list[temp_idnex] = '..'
    return result, ' '.join(map(str, result_list))
