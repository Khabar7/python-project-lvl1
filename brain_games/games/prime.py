from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2 or not number % 2:
        return False
    counter = 3
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 2
    return True


def make_question():
    number = randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer
