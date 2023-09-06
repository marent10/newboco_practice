import random
# 1. give us a random number
# 2. get input from player as int
# 3. tell us how they guessed
#   - too low
#   - correct
#   - too high
# 4. repeat the process


def is_correct(guess: int, correct: int) -> bool:
    if guess < correct:
        print("Your guess is too low!")
    elif guess > correct:
        print("Your guess is too high!")
    else:
        print("Congratulations! You got it right!")
    return guess == correct
def main():
    num_to_guess = random.randrange(100)
    max_guesses = 8
    guess_count = 0
    correct = False
    while not correct and guess_count < max_guesses:
        guess = int(input("Guess a number between 0 and 100: "))
        correct = is_correct(guess, num_to_guess)
        guess_count += 1
    if correct:
        print("You have won the game! (free fruit pizza)")
    else:
        print("Game Over! You have run out of guesses.")
        print(f"The correct number was: {num_to_guess}")
        
if __name__ == "__main__":
    main()


