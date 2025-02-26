print("Welcome to the Guess the Number Game!")
print("Think of a number between 1 and 100, and I will try to guess it.")
print("Give me hints by typing 'higher', 'lower', or 'correct'.\n")
low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    attempts += 1
    print(f"My guess is {guess}.")
    
    feedback = input("Is it 'higher', 'lower', or 'correct'? ").lower()
    
    if feedback == "higher":
        low = guess + 1
    elif feedback == "lower":
        high = guess - 1
    elif feedback == "correct":
        print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
        break 
    else:
        print("Invalid input! Please type 'higher', 'lower', or 'correct'.")

