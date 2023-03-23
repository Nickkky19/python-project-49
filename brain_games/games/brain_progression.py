import random


GAME_RANDOM_RANGE = (1, 99)
PROGRESSION_LENGTH_RANDOM_RANGE = (5, 15)
DESCRIPTION = 'What number is missing in the progression?'


def make_list_with_step(list_length, list_start, list_step):
    result_list = [list_start]
    for i in range(list_length):
        result_list.append(result_list[i] + list_step)
    return result_list


def make_expression():
    progression_length = random.randint(*PROGRESSION_LENGTH_RANDOM_RANGE)
    progression_start = random.randint(*GAME_RANDOM_RANGE)
    progression_step = random.randint(*GAME_RANDOM_RANGE)
    result_list = make_list_with_step(progression_length,
                                      progression_start,
                                      progression_step)
    temp_idnex = random.randint(0, progression_length - 1)
    result = result_list[temp_idnex]
    result_list[temp_idnex] = '..'
    return result, ' '.join(map(str, result_list))
