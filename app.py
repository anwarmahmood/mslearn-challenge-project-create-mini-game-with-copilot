# write 'hello world' to the console
print('hello world')
# This is a simple game to play Rock, Paper, Scissors with a user
# The user will be prompted to enter their choice and the computer will randomly select a choice
# The winner will be determined based on the rules of the game
# The user will be prompted to play again or exit the game
# The game will continue until the user decides to exit
# The game will be written in Python
# The game will be written in a single file
# lets define the rules of the game
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# lets define the game
# The game will be a function called rock_paper_scissors
# The function will take no arguments
# The function will prompt the user to enter their choice
# The function will randomly select a choice for the computer
# The function will determine the winner based on the rules of the game
# The function will prompt the user to play again or exit the game
# The function will continue until the user decides to exit
# lets write the game
# Path: app.py
import random
def rock_paper_scissors():
    while True:
        user_choice = input('Enter Rock, Paper, or Scissors: ')
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        print(f'My choice was: {computer_choice}')
        if user_choice == computer_choice:
            print('Tie!')
        elif user_choice == 'Rock' and computer_choice == 'Scissors':
            print('You win!')
        elif user_choice == 'Scissors' and computer_choice == 'Paper':
            print('You win!')
        elif user_choice == 'Paper' and computer_choice == 'Rock':
            print('You win!')
        else:
            print('You lose!')
        while True:
            play_again = input('Do you want to play again? (yes/no): ')
            if play_again.lower() == 'yes' or play_again.lower() == 'no':
                break
            else:
                print('Invalid input. Please enter "yes" or "no".')
        if play_again.lower() == 'no':
            break
        else:
            print('Invalid option. Please enter "yes" or "no".')
rock_paper_scissors()
# The game is now complete