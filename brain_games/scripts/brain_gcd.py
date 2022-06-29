#!/usr/bin/env python
import math
from random import randint

from brain_games.cli import welcome_user, gcd_game


def main():
    name = welcome_user()
    counter = 0
    while counter != 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        correct_answer = str(math.gcd(num1, num2))
        answer = gcd_game(num1, num2)
        if answer == correct_answer:
            print("Correct!")
            counter = counter + 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}. "
                  f"Let's try again, {name}!")
            break
        if counter == 3:
            print(f"Congratulations, {name}!")

