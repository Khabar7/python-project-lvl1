#!/usr/bin/env python
import random

import task as task

from brain_games.cli import calc_game, welcome_user


def main():
    name = welcome_user()
    operator = random.choice('+', '-', '*')
    num1 = random.randint(1, 100)
    num2 = random.randint(1,100)
    task = {num1}, {operator}, {num2}
    answer_calc = calc_game(task)
    counter = 0
    while counter != 3:
        equally = (num1, operator, num2)
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