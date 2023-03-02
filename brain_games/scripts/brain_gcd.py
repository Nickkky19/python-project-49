#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import gcd
from brain_games import games_functions
from games_functions.games_functions import check_correctness


GAME_RANDOM_RANGE = (1, 99)


def make_expression():
    number1 = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    number2 = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    result = gcd(number1, number2)
    return result, f'{number1} {number2}'


def main():
    name = games_functions.welcome_user_and_get_his_name()
    print('Find the greatest common divisor of given numbers.')
    correct_answers_counter = 0
    while correct_answers_counter < 3:
        correct_answer, expression = make_expression()
        games_functions.print_question(expression)
        user_answer = games_functions.print_ask_user_answer()
        is_user_correct = check_correctness(str(correct_answer),
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
