
import random
import re
from collections import Counter


# ==========================================
# PART 1: NUMBER GUESSING GAME
# ==========================================

def number_guessing_game():

    print("\n===== NUMBER GUESSING GAME =====")

    secret_number = random.randint(1, 100)

    max_attempts = 7
    attempts = 0

    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it!")

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess == secret_number:

                score = (max_attempts - attempts + 1) * 10

                print("\nCongratulations! You guessed correctly!")
                print("Number:", secret_number)
                print("Attempts used:", attempts)
                print("Your score:", score)

                break

            elif guess < secret_number:

                print("Too low! Try a higher number.")

            else:

                print("Too high! Try a lower number.")

            print("Attempts remaining:", max_attempts - attempts)

        except ValueError:

            print("Invalid input! Please enter a whole number.")

    else:

        print("\nGame Over!")
        print("The correct number was:", secret_number)
        print("Better luck next time!")


# ==========================================
# PART 2: WORD COUNTER
# ==========================================

def word_counter():

    print("\n===== WORD COUNTER =====")

    filename = input("Enter the text file name (default: sample.txt): ").strip()

    if not filename:
        filename = "sample.txt"

    try:

        # Read the text file
        with open(filename, "r", encoding="utf-8") as file:

            text = file.read()

        # Convert text into lowercase words
        words = re.findall(r"\b[\w']+\b", text.lower())

        if not words:
            print("The file is empty or contains no readable words.")
            return

        # Total number of words
        total_words = len(words)

        # Count frequency of each word
        word_frequency = Counter(words)

        # Number of unique words
        unique_words = len(word_frequency)

        # Display results
        print("\n===== WORD ANALYSIS RESULTS =====")

        print("File name:", filename)

        print("Total words:", total_words)

        print("Unique words:", unique_words)

        print("\nWord Frequency:")

        for word, count in word_frequency.most_common(10):

            print(f"{word}: {count}")

        print("\nMost frequent word:")

        most_common_word, frequency = word_frequency.most_common(1)[0]

        print(most_common_word, "appears", frequency, "times.")

    except FileNotFoundError:

        print("Error! File not found.")

    except PermissionError:

        print("Error! You do not have permission to read this file.")

    except OSError as error:

        print("Unable to read the file:", error)


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n====================================")
        print("     PYTHON MINI PROJECT")
        print("====================================")

        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":

            number_guessing_game()

        elif choice == "2":

            word_counter()

        elif choice == "3":

            print("\nThank you for using the application!")
            print("Goodbye!")

            break

        else:

            print("Invalid choice! Please select 1, 2 or 3.")


# Run the program
if __name__ == "__main__":

    main()
