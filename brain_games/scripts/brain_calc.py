#!/usr/bin/env python
import operator
from random import choice, randint

from brain_games.cli import welcome_user, calc_game

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def main():
    name = welcome_user()
    counter = 0
    while counter != 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operation = choice(list(operations.keys()))
        correct_answer = str(operations[operation](num1, num2))
        answer = calc_game(num1, operation, num2)
        if answer == correct_answer:
            print("Correct!")
            counter = counter + 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}. "
                  f"Let's try again, {name}")
            break
        if counter == 3:
            print(f"Congratulations, {name}!")
