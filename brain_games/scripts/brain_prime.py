#!/usr/bin/env python
import random

from brain_games.cli import welcome_user, brain_prime


def main():
    name = welcome_user()
    counter = 0
    while counter != 3:
        random_number = random.randrange(100)
        k = 0
        for i in range(2, random_number // 2 + 1):
            if random_number % i == 0:
                k = k + 1
        if k <= 0:
            simple = "yes"
        else:
            simple = "no"
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
