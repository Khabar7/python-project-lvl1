#!/usr/bin/env python
import random

from brain_games.cli import answer_for_even, welcome_user


def main():
    name = welcome_user()
    counter = 0
    while counter != 3:
        random_number = random.randrange(100)
        if random_number % 2:
            is_even = "no"
        else:
            is_even = "yes"
        answer = answer_for_even(random_number)
        if answer == is_even:
            print("Correct!")
            counter = counter + 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {is_even}. "
                  f"Let's try again, {name}")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")

