import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name


def answer_for_even(number: int):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    return answer.lower()


def calc_game(num1, operation, num2):
    print('What is the result of the expression?')
    print(f'Question: {num1} {operation} {num2}')
    answer = prompt.string("Your answer: ")
    return answer
