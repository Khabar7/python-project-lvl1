import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!\n'
    print(greeting)
    return user_name


def get_user_name():
    return prompt.string('May I have your name? ')


def get_user_answer():
    return prompt.string('Your answer: ')
