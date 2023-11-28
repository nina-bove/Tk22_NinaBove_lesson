import random

attempts = 1
words = ("christmas", "candles", "cinnamon", "winter", "holiday", "reindeer", "snowflake", "chimney",
         "mistletoe", "december", "snowman", "sleigh", "celebrate", "advent")  # A list of words
secret_word = random.choice(words)  # Randomly chooses a word from the list above
revealed_letters = {secret_word[0]}  # The first letter of the secret word is already revealed

print("Guess the secret word")
print("The word has a maximum of 10 letters and starts with the letter", secret_word[0])
print("You have a maximum of 5 attempts. Good luck!")

while attempts <= 5:  # When the number of attempts is lower than 5, the user can keep guessing
    guess = input(f"\nAttempt {attempts}. Current word: "
                  # All revealed letters are shown and put together to one set with the .join feature and the 
                  # if and else conditions are there to make sure that the same letter is not revealed more than once. 
                  # Those letters in the secret word that are not revealed yet will be replaced by a dash.
                  f"{''.join(letter if letter in revealed_letters else '_' for letter in secret_word)}\nYour guess: ")

    if guess == secret_word:  # If the user got the word right:
        print(f"Congratulations! You guessed the word {secret_word} in {attempts} attempts")
        break  # Allows the program to simply skip til the next piece of relevant code since there is no need to run
        # through the 'else'-conditions when the 'if'-conditions are already met.
    else:
        # If the user guess wrong, reveal another random letter of the secret word and show all the current revealed
        # letters and also add 1 to the attempts variable
        unrevealed_letters = [letter for letter in secret_word if letter not in revealed_letters]
        revealed_letters.add(random.choice(unrevealed_letters))
        attempts += 1

if attempts > 5:
    print("\nSorry, you reached the maximum number of attempts")
    print(f"The secret word was {secret_word}")

input("\n\nPress the Enter key to exit")
