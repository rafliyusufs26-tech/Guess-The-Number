import random

random_num = random.randint(1, 100)

while True:
    ask = input("Do you want to play? (y/n): ").lower()
    if ask == "y":
        print("Great! Let's start.")
        try:
            guess = int(input("Guess the number: "))
            if guess < random_num:
                print("Too low! Try again.")
            elif guess > random_num:
                print("Too high! Try again.")
            else:
                print("You got it!")
                break
        except ValueError:
            print("Please Enter Valid Number")
    elif ask == 'n':
        print("Okay, maybe next time!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")