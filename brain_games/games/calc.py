import operator
from random import choice

from brain_games.engine import generate_number

DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def make_question():
    num1 = generate_number()
    num2 = generate_number()
    operation = choice(list(operations.keys()))
    question = f'{num1} {operation} {num2}'
    answer = str(operations[operation](num1, num2))
    return question, answer
