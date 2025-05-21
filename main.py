import random

computer_choice = random.choice([1, 0, -1])
user_choice = input("Enter rock, paper, or scissor:")
dict = {"rock": 1,"scissor" : -1, "gun" : 0}
you = dict[user_choice]
reverse_dict = {1:"rock", -1:"scissor", 0:"gun"}

print(f"you chose : {user_choice}\nComputer chose : {reverse_dict[computer_choice]}")

if(computer_choice == you):
  print("Its a draw")


else:
  if(computer_choice == -1 and you == 1):
    print("You Win!")

  elif(computer_choice == -1 and you == 0):
    print("You Lose!")

  elif(computer_choice == 1 and you == -1):
    print("You Lose!")

  elif(computer_choice == 1 and you == 0):
    print("You Win!")
    
  elif(computer_choice == 0 and you == -1):
    print("You Win!")

  elif(computer_choice == 0 and you == -1):
    print("You Lose")

  else:
    print("Something went wrong")
  








