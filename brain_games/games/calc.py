import operator
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operation = choice(list(operations.keys()))
    question_number = f'{num1} {operation} {num2}'
    answer = str(operations[operation](num1, num2))
    return question_number, answer
