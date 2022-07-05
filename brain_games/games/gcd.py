#!/usr/bin/env python

from brain_games.engine import generate_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
    num1 = generate_number()
    num2 = generate_number()
    question = f'Question: {num1} {num2}'
    answer = gcd(num1, num2)
    return question, str(answer)


def gcd(num1, num2):
    if not num2:
        return num1
    return gcd(num2, num1 % num2)
