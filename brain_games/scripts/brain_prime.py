#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import games_functions


GAME_RANDOM_RANGE = (2, 99)


def make_expression():
    number = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    if number == 2:
        return 'yes', number
    for i in range(2, number // 2 + 1):
        if not number % i:
            return 'no', number
    return 'yes', number


def main():
    name = games_functions.welcome_user_and_get_his_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers_counter = 0
    while correct_answers_counter < 3:
        correct_answer, expression = make_expression()
        games_functions.print_question(expression)
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
