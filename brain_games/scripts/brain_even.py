#!/usr/bin/env python
from brain_games.engine import engine
from brain_games.games import even

from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    engine(user_name, even)


if __name__ == '__main__':
    main()
