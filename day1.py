import random

user_choice = int(input("Rock =1 Paper =2 Scissors =3?"))
computer_choice = random.randint(0,2)

print(type(user_choice))

rock = 1
paper = 2
scissors = 3

def userChoice():
       if user_choice == rock or user_choice == paper or user_choice == scissors:
                print("That is a valid choice")
       else:
                print("That is an invalid choice")

userChoice()


print(f"This is the computer choice: {computer_choice} ")


