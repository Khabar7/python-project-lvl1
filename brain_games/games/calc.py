import operator
from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def make_question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operation = choice(list(operations.keys()))
    question = f'{num1} {operation} {num2}'
    answer = str(operations[operation](num1, num2))
    return question, answer
