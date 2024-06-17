import random

def game(you, computer):
    if you == computer:
        return 0
    elif you == 'r' and computer == 'p':
        return 1
    elif you == 'p' and computer == 'r':
        return -1
    elif you == 'r' and computer == 's':
        return 0
    elif you == 's' and computer == 'r':
        return 2
    elif you == 'p' and computer == 's':
        return 0
    elif you == 's' and computer == 'p':
        return 2

while True:
    you = input("Enter rock , paper, or scissor  : ")
    num = random.randint(1, 100)
    if num < 33:
        computer = 'rock'
    elif num > 33 and num < 66:
        computer = 'paper'
    else:
        computer = 'scissor'

    result = game(you, computer)
    if result == 0:
        print("The game is a tie\n")
    elif result == -1:
        print("Computer wins\n")
    elif result == 1:
        print("You win\n")
    else:
        print("You lose\n")

    print("You chose:", you)
    print("Computer chose:", computer)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
