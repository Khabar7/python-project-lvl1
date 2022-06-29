#!/usr/bin/env python
from random import randint, choice

from brain_games.cli import welcome_user, brain_progression


def make_progression():
    initial_number = randint(1, 100)
    delta = randint(1, 25)
    length = 10
    maximum_number = (delta * length) + initial_number
    return range(initial_number, maximum_number, delta)


def main():
    name = welcome_user()
    counter = 0
    while counter != 3:
        prog = make_progression()
        secret = choice(prog)
        progression = ' '.join([
            '..' if num == secret else str(num) for num in prog
        ])
        correct_answer = str(secret)
        answer = brain_progression(progression)
        if correct_answer == answer:
            print("Correct!")
            counter = counter + 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}. "
                  f"Let's try again, {name}!")
            break
        if counter == 3:
            print(f"Congratulations, {name}!")
