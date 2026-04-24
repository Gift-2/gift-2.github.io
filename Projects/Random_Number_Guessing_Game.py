import random
again = "y"
while again.lower() == "y":
    lower = int(input("Enter the lower bound of the range: "))
    upper = int(input("Enter the upper bound of the range: "))
    found = False
    count = 1
    number = random.randint(lower, upper)
    
    #Priming Read - reading the intial value into a variable that will be used in a loop as a controlled variable.
    guess = int(input("Please type in your guess for the random number: "))
    
    while not found and guess != -99:
        while guess < lower or guess > upper:
            guess = int(input(f"Invalid Guess! Please guess between {lower} and {upper}: "))
        if guess == number:
            print(f"Excellent! You got it right, after {count} attempts!")
            found = True
        elif guess > number + 5:
            print("Sorry, Too High!")
        elif guess < number - 5:
            print("Sorry, Too Low!")
        elif guess > number:
            print("Close, but High")
        else:
            print("Close, but Low!")
        
        if not found:
            guess = int(input("Sorry! please try again to guess a random number or type -99 to give up: "))
            count += 1
    if guess == -99:
        print(f"Sorry you gave up on the {count} attempt!!! The number is {number}!")

    again = input("Would you like to continue playing ? Answer y or n: ")
