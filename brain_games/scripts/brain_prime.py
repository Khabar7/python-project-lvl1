#!/usr/bin/env python
import random

from brain_games.cli import welcome_user, brain_prime


def main():
    name = welcome_user()
    counter = 0
    while counter != 3:
        random_number = random.randrange(100)
        if random_number < 2 or not random_number % 2:
            simple = "no"
        else:
            simple = "yes"
        answer = brain_prime(random_number)
        if answer == simple:
            print("Correct!")
            counter = counter + 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {simple}. "
                  f"Let's try again, {name}")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")
