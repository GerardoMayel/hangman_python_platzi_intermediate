
# Import OS library to identify OS, for Lunix and Mac OS the name is 'posix'
# For Windows os.name is 'nt'
# Import Random for Random Words

import random
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


# Data Reading Data Module


class data_reader():

    def __init__(self):
        self.data = []
        self.word_length = []

    def txt_reader(self):

        with open("./Data/data.txt", 'r', encoding='utf8') as f:
            for line in f:
                line = line.replace('\n', '')
                self.data.append(line)
            for i in range(len(self.data)):
                self.word_length.append((self.data[i], len(self.data[i])))
        return self.word_length


def run():
    #cleaner = clean_screen()
    # cleaner.clean()
    player_1 = player()
    player_1.clean()
    print(player_1.ask_name())
    data_1 = data_reader()
    print(data_1.txt_reader())


if __name__ == '__main__':
    run()
