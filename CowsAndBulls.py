import random


def cows_and_bulls():
    """
    For every digit that the user guessed correctly in the correct place,
    they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull”.
    """
    new_game = False
    while True:
        level = int(input("Select level of difficulty (2 /very easy/ - 6 /very hard/ -> "))
        if level in range(2, 7):
            random_number = [random.randint(0, 9) for i in range(level)]
            step = 0
            cows = 0
            bulls = 0
            while True:
                step += 1
                print(f"Try to guess {level} digit number! ")
                while True:
                    guess = [int(i) for i in input()]
                    if len(guess) == len(random_number):
                        break
                    print("Invalid action!")
                if guess == random_number:
                    print(f"You Correctly Guessed The Number!!!\n Steps needed to guess {step}")
                    new_game = input('Do you want to play again? (y/n)')
                    if new_game == 'y':
                        cows_and_bulls()
                    break
                else:
                    cows = 0
                    bulls = 0
                    for i in range(len(random_number)):
                        if guess[i] == random_number[i]:
                            cows += 1
                        elif guess[i] in random_number:
                            bulls += 1
                    print(f"Cows: {cows}  Bulls: {bulls}")
            break
        print("Invalid action!")


# if __name__ == '__main__'
#     CowsAndBulls()


