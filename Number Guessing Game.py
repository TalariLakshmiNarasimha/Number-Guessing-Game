import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess it?")
    
    # Computer picks a random number
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    while True:
        # Get user input
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Provide feedback
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
