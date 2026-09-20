import random
choices=['r','p','s']
user_choice=input("enter your choice(r/p/s):").lower()
if user_choice not in choices:
    print("invalid choice")
else:
    computer_choice=random.choice(choices)

    print("you chose:",user_choice)
    print("computer chose:",computer_choice)

    if user_choice == computer_choice:
        print("TIE")

    elif user_choice=="r" and computer_choice=="s" or\
        user_choice=="s" and computer_choice=="p" or \
        user_choice=="p" and computer_choice=="r":
        print("you won")
    else:
        print("computer won")


