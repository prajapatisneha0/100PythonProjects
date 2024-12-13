import random
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
game_image = [rock , paper , scissors]
user_choice = int(input("What do you choose ?"
                        " type 0 for Rock ,"
                        " Type 1 for Paper ,"
                        " Type 2 for Scissors "))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])
computer_choice = random.randint(0,2)
print(f"computer chose:")
print(game_image[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you type an invalid number , you lose!")
elif user_choice == 0 and  computer_choice == 2:
    print("you win!")
elif user_choice > computer_choice:
    print("you win!")
elif user_choice == computer_choice:
    print("it's a draw")
elif user_choice == 2 and  computer_choice == 0:
    print("you lose!")
elif user_choice < computer_choice:
    print("you lose!")

