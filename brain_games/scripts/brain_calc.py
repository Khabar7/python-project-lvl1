#!/usr/bin/env python
from brain_games.engine import engine
from brain_games.games import calc
from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    engine(user_name, calc)


if __name__ == '__main__':
    main()
