from brain_games.cli import get_user_answer

NUMBER_OF_ROUNDS = 3


def engine(user_name, game):
    print(game.DESCRIPTION + '\n')
    correct_answers = 0
    while correct_answers < NUMBER_OF_ROUNDS:
        question, right = game.get_question_and_answer()
        print(f'Question: {question}')
        answer = get_user_answer()
        if answer == right:
            msg = 'Correct!'
            res = True
        else:
            msg = f'{answer} is wrong answer ;(. Correct answer was {right}.'
            res = False
        print(msg)
        if not res:
            print(f"Let's try again, {user_name}!")
            return
        correct_answers += 1
    print(f'Congratulations, {user_name}!')
