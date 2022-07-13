from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question():
    number = generate_number()
    answer = correct_answer(number)
    return number, answer


def correct_answer(number):
    return 'no' if number % 2 else 'yes'
