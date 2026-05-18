import random

# Generate the number and pick a random number
random_num = random.randint(1, 100)

while True:

    ask = input("Do you want to play? (y/n): ").lower()

    if ask == "y": 
        print("Great! Let's start.") # The game start if you type 'y'
        
        while True:
            try:
                guess = int(input("Guess the number: "))
                if guess < random_num: 
                    print("Too low! Try again.")
                elif guess > random_num:
                    print("Too high! Try again.")
                elif guess == random_num:
                    print("You got it!")
                    break
            except ValueError:
                print('Please enter a valid number.')
            
    elif ask == 'n':
        print("Okay, maybe next time!") # The game stop if you type 'n'
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'") # Error if type random than 'y' or 'n'
