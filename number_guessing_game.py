# ============================================================
# NUMBER GUESSING GAME
# ============================================================
# Picture this: a friend hides a number in their head and
# dares you to figure it out. They'll tell you if you're
# too high or too low — but you only get so many tries.
# This program recreates that classic game. You choose the
# range, you choose how many guesses you get, and then the
# hunt begins. Good luck — you'll need it!
# ============================================================

# Python's "random" toolbox gives us the power to pick a
# secret number that even we (the programmer) don't know
# until it's time to play. That's what makes it a real game!
import random

# These three variables hold the player's chosen range and
# attempt limit. They live outside the functions so every
# part of the program can see and use them freely.
number_one = int(input("📊 Enter the first number:  "))
number_two = int(input("📊 Enter the second number: "))
attempts   = int(input("🎯 Number of attempts:      "))


# ------------------------------------------------------------
# FUNCTION: get_guess
# ------------------------------------------------------------
# Think of this as the moment the player cups their hands
# around their mouth and calls out a number. If they shout
# something that isn't a number — say, they accidentally
# type "k" — we patiently ask them to try again instead of
# crashing the game. They can also whisper 'q' to walk away.
def get_guess():
    while True:
        user_input = input(f"🔢 Guess a number between {number_one} and {number_two}: ").strip()

        # The player decided to quit — honour that choice.
        if user_input.lower() == 'q':
            return 'q'

        # A valid guess must be made of digits only.
        # isdigit() catches letters, symbols, and empty input.
        if user_input.isdigit():
            return int(user_input)

        # They typed something we can't work with — let them know.
        print(f"⚠️  Invalid input. Please enter a number between "
              f"{number_one} and {number_two}, or 'q' to quit.")


# ------------------------------------------------------------
# FUNCTION: main  (the "game loop")
# ------------------------------------------------------------
# This is where the story unfolds. A secret number is chosen,
# the player guesses one by one, and with every wrong answer
# we give them a clue — higher or lower. The game ends when
# they nail it, run out of tries, or choose to quit.
def main():
    global attempts

    # The secret is born — randomly picked inside the range
    # the player chose. Only the computer knows it for now.
    number = random.randint(number_one, number_two)

    print("\n================================================")
    print("🎮  Welcome to the Number Guessing Game!")
    print(f"🤫  I'm thinking of a number between {number_one} and {number_two}.")
    print(f"❤️   You have {attempts} attempt(s). Type 'q' to quit.")
    print("================================================\n")

    # As long as the player has attempts left, the game goes on.
    while attempts > 0:
        guess = get_guess()

        # Every guess — right or wrong — costs one attempt.
        attempts -= 1

        # The player chose to walk away before the game ended.
        if guess == 'q':
            print(f"👋 Thanks for playing! The number was {number}.")
            break

        # Bull's-eye! The player cracked the secret.
        elif guess == number:
            print("🎉 You guessed the number! Well done!")
            break

        # Their guess was too small — nudge them upward.
        elif guess < number:
            print("📉 Too low!")
            if attempts > 0:
                print(f"❤️  You have {attempts} attempt(s) left.\n")

        # Their guess was too big — pull them back down.
        else:
            print("📈 Too high!")
            if attempts > 0:
                print(f"❤️  You have {attempts} attempt(s) left.\n")

    # The loop ended naturally — the player used every attempt.
    else:
        print(f"\n💀 Out of attempts! The number was {number}. Better luck next time!")


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------
# The story starts here. Every variable is set, every function
# is defined — now we fire the starting pistol and let main()
# take it from here.
main()
