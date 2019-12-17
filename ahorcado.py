# -*- coding: utf-8 -*-
import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''','''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''','''

''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'democracia',
    'dictadura',
    'computadora',
    'movil',
    'virtual'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries, user_letter_use):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('LETTERS USE:')
    print(user_letter_use)
    print('ERROR:{}'.format(tries))    
    print('--- * --- * --- * --- * --- * --- ')

def main():
    word =  random_word()
    user_letter_use = []
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries, user_letter_use)
        current_letter = str(input('Escoge una letra: '))
        user_letter_use.append(current_letter)

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == len(IMAGES) - 2 :                 
                print('')
                display_board(hidden_word, tries, user_letter_use)
                print('YOU LOSE! The word was {}'.format(word))
                break

        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter                            

        try:
            hidden_word.index('-')
        except ValueError:
            print('')            
            print('YOU WIN!!!')
            break
            

if __name__ == '__main__':
    print('BIENVENIDOS AL JUEGO DEL AHORCADO')
    main()