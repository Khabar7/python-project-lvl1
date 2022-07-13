from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    initial_number = randint(1, 100)
    delta = randint(1, 25)
    length = randint(5, 10)
    maximum_number = (delta * length) + initial_number
    return list(range(initial_number, maximum_number, delta))


def make_question():
    prog = make_progression()
    secret = randint(0, len(prog) - 1)
    answer, prog[secret] = prog[secret], '..'
    return " ".join(str(x) for x in prog), str(answer)
