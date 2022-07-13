from random import choice, randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    initial_number = randint(1, 100)
    delta = randint(1, 25)
    length = randint(5, 10)
    maximum_number = (delta * length) + initial_number
    return range(initial_number, maximum_number, delta)


def make_question():
    prog = make_progression()
    secret = choice(prog)
    answer, prog[secret] = prog[secret], '..'
    return ' '.join(prog), answer
