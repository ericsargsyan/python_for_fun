import os
import random
import time


def isvalid():
    while True:
        choice = input("Do you want to play again (y/n)? ")
        if choice == 'y':
            return True
        elif choice == 'n':
            exit()
        else:
            print("Invalid syntax! ")


def hangman():
    with open('sowpods.txt', 'r') as random_words:
        word = list(random.choice(list(random_words)).rstrip())
        # print(word)
        word_length = len(word)

    not_guessed = list('_' * word_length)
    guessed = []
    while True:
        if not_guessed == word:
            print(f"You Correctly Guessed the word\nThe word was {word}")
            if isvalid():
                os.system('CLS')
                hangman()
        letter = input('Make your Guess! ')
        if letter.upper() not in word:
            print('Letter does not exist in the word!')
        elif letter.upper() in guessed:
            print('Already Guessed letter!')
        else:
            for i in range(len(word)):
                if word[i].lower() == letter or word[i] == letter:
                    not_guessed[i] = letter.capitalize()
                    guessed.append(letter.upper())
            os.system('CLS')
            print(not_guessed)


hangman()

