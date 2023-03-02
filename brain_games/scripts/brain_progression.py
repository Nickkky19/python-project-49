#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import games_functions


GAME_RANDOM_RANGE = (1, 99)
PROGRESSION_LENGTH_RANDOM_RANGE = (5, 15)


def make_expression():
    progression_length = games_functions.\
                get_random_value_by_range(PROGRESSION_LENGTH_RANDOM_RANGE)
    progression_start = games_functions.\
                get_random_value_by_range(GAME_RANDOM_RANGE)
    progression_step = games_functions.\
                get_random_value_by_range(GAME_RANDOM_RANGE)
    result_list = [progression_start]
    for i in range(progression_length):
        result_list.append(result_list[i] + progression_step)
    temp_idnex = games_functions.\
                get_random_value_by_range((0, progression_length - 1))
    result = result_list[temp_idnex]
    result_list[temp_idnex] = '..'
    return result, result_list


def main():
    name = games_functions.welcome_user_and_get_his_name()
    print('What number is missing in the progression?')
    correct_answers_counter = 0
    while correct_answers_counter < 3:
        correct_answer, expression = make_expression()
        games_functions.print_question(' '.join(map(str, expression)))
        user_answer = games_functions.print_ask_user_answer()
        is_user_correct = games_functions.\
                                  check_correctness(str(correct_answer),
                                                    user_answer)
        if is_user_correct:
            correct_answers_counter += 1
            games_functions.print_answer(True)
        else:
            games_functions.print_answer(False, user_answer,
                                         correct_answer, name)
            break
    else:
        games_functions.print_end_game(True, name)


if __name__ == '__main__':
    main()
