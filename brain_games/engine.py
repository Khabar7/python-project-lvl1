from brain_games.cli import get_user_answer, welcome_user

NUMBER_OF_ROUNDS = 3


def engine(game=None):
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    if game:
        print(game.DESCRIPTION + '\n')
    else:
        return
    correct_answers = 0
    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = game.make_question()
        print(f'Question: {question}')
        user_answer = get_user_answer()
        if user_answer == correct_answer:
            msg = 'Correct!'
            res = True
        else:
            msg = f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.'
            res = False
        print(msg)
        if not res:
            print(f"Let's try again, {user_name}!")
            exit()
        correct_answers += 1
    print(f'Congratulations, {user_name}!')
