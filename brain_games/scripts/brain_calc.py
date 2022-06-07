#!/usr/bin/env python
import random

from brain_games.cli import welcome_user, calc_game

calc_game


def main():
    name = welcome_user()
    counter = 0
    while counter != 3:
        first_number = random.randrange(100)  # Генерация первого числа
        operator = random.choice(['win', 'lose', 'draw'])  # Генерация оператора (+, -, *)
        second_number = random.randrange(100)  # Генерация второго числа
        math_operator = str(first_number, operator, second_number)
        equally = first_number, operator, second_number
        if equally:
            answer_calc !=
        if answer_calc == equally:
            print("Correct!")
            counter = counter + 1
        else:
            print(f"{answer_calc} is wrong answer ;(. Correct answer was {equally}. "
                  f"Let's try again, {name}")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")

        # if random_number % 2:
        #     is_even = "no"
        # else:
        #     is_even = "yes"
        # answer = answer_for_even(random_number)
        # if answer == is_even:
        #     print("Correct!")
        #     counter = counter + 1
        # else:
        #     print(f"{answer} is wrong answer ;(. Correct answer was {is_even}. "
        #           f"Let's try again, {name}")
        #     break
