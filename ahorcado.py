
import os
from os import system
from os import name


class clean_screen():
    def __init__(self):
        self.os_name = os.name

    def clean(self):
        if self.os_name == 'posix':
            _ = system('clear')
        else:
            _ = system('cls')


def run():
    cleaner = clean_screen()
    cleaner.clean()


if __name__ == '__main__':
    run()
