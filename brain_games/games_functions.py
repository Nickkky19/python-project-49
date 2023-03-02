#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
import prompt


def get_random_value_by_range(temp_range: tuple[int]) -> int:
    return randint(*temp_range)


def is_even(temp_number: int) -> bool:
    return True if temp_number % 2 else False


def welcome_user_and_get_his_name() -> str:
    print(f'Hello, {(name := prompt.string("May I have your name? "))}!')
    return name


def print_answer(is_good: bool,
                 user_answer: str | None = None,
                 correct_answer: str | None = None,
                 user_name: str | None = None) -> None:
    if is_good:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {user_name}!")


def print_question(question: str) -> None:
    print(f'Question: {question}')


def print_end_game(is_good: bool, user_name: str) -> None:
    if is_good:
        print(f'Congratulations, {user_name}!')


def print_ask_user_answer() -> str:
    return prompt.string('Your answer: ').lower()


def check_correctness(answer1, answer2):
    return answer1 == answer2
