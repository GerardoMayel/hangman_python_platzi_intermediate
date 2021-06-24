
# Import OS library to identify OS, for Lunix and Mac OS the name is 'posix'
# For Windows os.name is 'nt'
# Import Random for Random Words

import random
import os
from os import system
from os import name
import unicodedata

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
        print('Welcome to Hangman Game')
        print('--' * 32)
        self.name = input('Enter your player nickname: ')

        return self.name


# Data Reading Data Module


class data_reader():

    def __init__(self):
        self.data = []

    def txt_reader(self):

        with open("./Data/data.txt", 'r', encoding='utf8') as f:
            for line in f:
                line = line.replace('\n', '')
                self.data.append(line)
        return self.data


class hangman_game(data_reader, player):

    def __init__(self):
        super().__init__()

    def random_word(self):
        self.letters_from_word = []
        self.game_word = {}
        self.word_vector = data_reader.txt_reader(self)
        self.random_word = random.sample(self.word_vector, 1)
        self.random_word = self.random_word[0].strip().upper()

        self.letters_from_word = [letters for letters in self.random_word]

        self.random_word_hide = [letters for letters in self.random_word]
        word_len = len([letters for letters in self.random_word]) - 1
        random_hide_1 = random.randint(0, word_len)
        random_hide_2 = random.randint(0, word_len)

        self.random_word_hide[random_hide_1] = '_'
        self.random_word_hide[random_hide_2] = '_'

        self.game_word = {
            'word': self.random_word,
            'letters_from_word': self.letters_from_word,
            'word_with_hide_letters': self.random_word_hide
        }
        return self.game_word

    def game_control(self):

        self.player_name = player.ask_name(self)

        #print('Guess the letter to complete the word')

        self.word_dict = hangman_game.random_word(self)
        # print(self.word_dict)
        self.word_game = self.word_dict.get('word_with_hide_letters')
        # print(self.word_game)

        self.final_word = self.word_dict.get('word')
        # print(self.final_word)
        self.real_word = self.word_dict.get('letters_from_word')
        # print(self.real_word)

        self.attempt_counter = 0

        self.compressed_word = ''

        for letter in self.word_game:
            self.compressed_word = self.compressed_word + letter

        # print(self.compressed_word)

        while unicodedata.normalize('NFKD', self.compressed_word).encode('ASCII', 'ignore').strip().lower() != unicodedata.normalize('NFKD', self.final_word).encode('ASCII', 'ignore').strip().lower():

            print(self.word_game)

            if self.attempt_counter == 0:
                self.word_input = input('Enter the correct letter : ')
            else:
                self.word_input = input('Try Again : ')

            self.word_input = self.word_input.strip().upper()
            self.attempt_counter += 1
            # print(self.word_input)

            for i in range(0, len(self.real_word) - 1):
                # print(unicodedata.normalize('NFKD', self.word_input).encode(
                #     'ASCII', 'ignore').strip().upper())
                # print(unicodedata.normalize('NFKD', self.real_word[i]).encode(
                #     'ASCII', 'ignore').strip().upper())
                if unicodedata.normalize('NFKD', self.word_input).encode('ASCII', 'ignore').strip().upper() == unicodedata.normalize('NFKD', self.real_word[i]).encode('ASCII', 'ignore').strip().upper():
                    self.word_game[i] = self.word_input
                    print(self.word_game)

            self.compressed_word = ''

            for letter in self.word_game:
                self.compressed_word = self.compressed_word + letter

        self.end_game = 'Congratulations ' + self.player_name + ' the word was ' + self.final_word + \
            ' and you solved it in: ' + \
            str(self.attempt_counter) + ' attempts, Game Over'

        return self.end_game


def run():

    cleaner = clean_screen()
    cleaner.clean()

    game_1 = hangman_game()
    print(game_1.game_control())


if __name__ == '__main__':
    run()
