
# Import OS library to identify OS, for Lunix and Mac OS the name is 'posix'
# For Windows os.name is 'nt'

import os
from os import system
from os import name

# Object Clean Shell Screen


class clean_screen():
    def __init__(self):
        self.os_name = os.name

    def clean(self):
        if self.os_name == 'posix':
            _ = system('clear')
        else:
            _ = system('cls')

# Object Capture player Nickname


class player(clean_screen):
    def __init__(self):
        super().__init__()
        self.name = name

    def clean_screen(self):
        super().clean()

    def ask_name(self):
        self.name = input('Enter your player nickname: ')
        return self.name


def run():
    #cleaner = clean_screen()
    # cleaner.clean()
    player_1 = player()
    player_1.clean()
    print(player_1.ask_name())


if __name__ == '__main__':
    run()
