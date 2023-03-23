import prompt


MAX_CORRECT_ANSWERS = 3


def run_game(game_name):
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game_name.DESCRIPTION)
    correct_answers_counter = 0
    while correct_answers_counter < MAX_CORRECT_ANSWERS:
        correct_answer, expression = game_name.make_expression()
        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ').lower()
        if str(correct_answer) == str(user_answer):
            correct_answers_counter += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
