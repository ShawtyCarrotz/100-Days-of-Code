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

choice = input("Let's play rock paper scissors! Which one do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

import random

if choice != "0" and choice != "1" and choice != "2":
  print("You typed an invalided number, you lose!")
else:
  if choice == "0":
    print(rock + "\n")
  elif choice == "1":
    print(paper + "\n")
  else:
    print(scissors + "\n")

# or create list options before and print(options[choice])

  options = [rock, paper, scissors]
  computer = random.choice(options)
  
  print("Computer chose:\n" + computer)

# or 
# computer = random.randint(0, 2)
# print("Computer chose:")
# print(options[computer])
  
    
  if computer == rock:
    if choice == "0":
      print("You tie!")
    elif choice == "1":
      print("You win!")
    else:
      print("You lose!")
  elif computer == paper:
    if choice == "0":
      print("You lose!")
    elif choice == "1":
      print("You tie!")
    else:
      print("You win!")
  elif computer == scissors:
    if choice == "0":
      print("You win!")
    elif choice == "1":
      print("You lose!")
    else:
      print("You tie!")

# or
# if user_choice == 0:
#   if computer_choice == 0:
#     print("You tied!")
#   elif computer_choice == 1:
#     print("You lose :( ")
#   else:
#     print("You win!")
# elif user_choice == 1: 
#   if computer_choice == 0:
#     print("You win!")
#   elif computer_choice == 1:
#     print("You tied!")
#   else:
#     print("You lose :( ")
# else: 
#   if computer_choice == 0:
#     print("You lose :( ")
#   elif computer_choice == 1:
#     print("You win!")
#   else:
#     print("You tied!")
