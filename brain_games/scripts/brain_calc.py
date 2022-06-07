#!/usr/bin/env python
import random

from brain_games.cli import calc_game, welcome_user


def main():
    name = welcome_user()
    answer_calc = calc_game()
    equally = random.randrange(100), random.choice(['win', 'lose', 'draw']), random.randrange(100)
    task = str(equally)
    counter = 0
    while counter != 3:
        if answer_calc == equally:
            print("Correct!")
            counter = counter + 1
        else:
            print(f"{answer_calc} is wrong answer ;(. Correct answer was {equally}. "
                  f"Let's try again, {name}")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")


    # a = random.randrange(100)  Генерация первого числа
    # b = random.choice(['win', 'lose', 'draw'])  Генерация оператора (+, -, *)
    # c = random.randrange(100)  Генерация второго числа