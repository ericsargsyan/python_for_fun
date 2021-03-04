import random


def computerChoice():
    computer_choice = ["Rock", "Paper", "Scissors"]
    return random.choice(computer_choice)


player = input("Enter your name: ")

while True:
    while True:
        user_choice = input("Enter your choice (Rock(r)/Paper(p)/Scissors(s)/ 0 to exit)\n")
        if user_choice == 'r' or user_choice == 'p' or user_choice == 's' or user_choice == '0':
            break
        print("Please enter valid character!")
    comp_choice = computerChoice()
    print(f"Computer choice is {comp_choice}")
    if (comp_choice == "Paper" and user_choice == "r") or \
            (comp_choice == "Rock" and user_choice == "s") or \
            (comp_choice == "Scissors" and user_choice == "p"):
        print("Computer Wins!!!")
    elif (user_choice == "p" and comp_choice == "Rock") or \
            (user_choice == "r" and comp_choice == "Scissors") or \
            (user_choice == "s" and comp_choice == "Paper"):
        print(f"{player} Wins!!!")
    elif (comp_choice == 'Rock' and user_choice == 'r') or \
            (comp_choice == 'Paper' and user_choice == 'p') or \
            (comp_choice == 'Scissors' and user_choice == 's'):
        print("Draw!")
    elif user_choice == "0":
        break

