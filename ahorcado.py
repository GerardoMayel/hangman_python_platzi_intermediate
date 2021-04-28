
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


# class player():
#     def __init__(self, name, lives):

#         self.name = input('Enter Player Nickname : ')
#         self.lives = 5

#     def obtain_name(self):
#         try:
#             if self.name != None:
#                 pass


# class game(player):
#     def __init__(self, name, lives, difficulty):
#         super().__init__(name, lives)
#         self.difficulty = difficulty
#         pass


# class dashboard(player, game):
#     pass


def run():
    cleaner = clean_screen()
    cleaner.clean()

    print(os.name)

    # if os.name == "posix":
    #     _ = system('clear')
    # else:
    #     _ = system('cls')


if __name__ == '__main__':
    run()
