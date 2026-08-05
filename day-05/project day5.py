secret = 7

guess = int(input("Guess the Number (1-10): "))

if guess == secret:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess. Try Again.")