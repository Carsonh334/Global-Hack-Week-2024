rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
rock_paper_scissors = [rock, paper, scissors]

def play_game():
    r = random.randint(0,2)
    x = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if x > 2 or x < 0:
        print("You entered an invalid number, You Lose")
    else:
        print(f"You chose: {rock_paper_scissors[x]}")
        print(f"Computer chose:\n {rock_paper_scissors[r]}")
    if x == 0 and r == 2:
        print("YOU WIN!")
    elif x == 1 and r == 0:
        print("YOU WIN!")
    elif x == 2 and r == 1:
        print("YOU WIN!")
    elif x == r:
        print("IT'S A DRAW :)")
    else:
        print("YOU LOSE :(")
    print("\n")

while input("Do you want to play a game of rock, paper, scissors? Type 'y' or 'n': ") == "y":
    play_game()
