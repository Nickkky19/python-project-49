#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
import prompt


GAME_RANDOM_RANGE = (1, 99)


def is_even(temp_number: int) -> str:
    if temp_number % 2:
        return 'no'
    return 'yes'


def main():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_counter = 0
    while correct_answers_counter < 3:
        correct_answer = is_even(number := randint(*GAME_RANDOM_RANGE))
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        print(answer.lower() == correct_answer, answer.lower(), correct_answer)
        if answer.lower() == correct_answer:
            print('Correct!')
            correct_answers_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
