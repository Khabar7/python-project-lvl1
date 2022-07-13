from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question():
    number = generate_number()
    return number, 'no' if number % 2 else 'yes'
