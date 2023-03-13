from brain_games.games import games_functions


MAX_CORRECT_ANSWERS = 3


def run_game(game_name):
    name = games_functions.welcome_user_and_get_his_name()
    print(game_name.DESCRIPTION)
    correct_answers_counter = 0
    while correct_answers_counter < MAX_CORRECT_ANSWERS:
        correct_answer, expression = game_name.make_expression()
        games_functions.print_question(expression)
        user_answer = games_functions.print_ask_user_answer()
        if games_functions.check_correctness(correct_answer, user_answer):
            correct_answers_counter += 1
            games_functions.print_answer(True)
        else:
            games_functions.print_answer(False, user_answer, correct_answer, name)
            break
    else:
        games_functions.print_end_game(True, name)
