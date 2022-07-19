from random import randint, randrange

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    start = randint(1, 100)
    step = randint(1, 25)
    length = randint(5, 10)
    stop = (step * length) + start
    return list(range(start, stop, step))


def get_question_and_answer():
    question_progression = make_progression()
    secret = randrange(0, len(question_progression))
    answer, question_progression[secret] = question_progression[secret], '..'
    return ' '.join(map(str, question_progression)), str(answer)
