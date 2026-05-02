# ============================================================
# DICE ROLLING GAME
# ============================================================
# Imagine you're sitting at a board game night with friends.
# Someone says "we need a dice roller!" — so you build one.
# This program lets you roll two dice as many times as you
# want, keeps track of your total rolls, and lets you quit
# whenever you're done. Let's walk through how it works!
# ============================================================

# First, we bring in Python's built-in "random" toolbox.
# We need it to simulate the randomness of a real dice roll.
import random

# This variable remembers how many dice rolls happened
# across the ENTIRE game session — even across multiple rounds.
# We place it here (outside the functions) so both functions
# can see and update it. This is called a "global" variable.
total_rolls = 0


# ------------------------------------------------------------
# FUNCTION: roll_dice
# ------------------------------------------------------------
# Think of this as the moment you pick up two dice and throw
# them on the table. Each die can land on any number from 1
# to 6, chosen randomly. The result is handed back as a pair
# of numbers — one for each die.
def roll_dice():
    return (random.randint(1, 6), random.randint(1, 6))


# ------------------------------------------------------------
# FUNCTION: main  (the "game loop")
# ------------------------------------------------------------
# This is the heart of the game. It greets the player, asks
# what they want to do, rolls the dice if they say yes, and
# keeps coming back (by calling itself) until the player
# decides to leave. That "calling itself" trick is known as
# RECURSION — the function loops by restarting itself.
def main():

    # Ask the player: do you want to roll or walk away?
    choice = input("Roll the Dice? (y/n): ")

    if choice == "y":
        # Great — they want to roll! Now ask how many times.
        times = int(input("How many times to roll the dice? (1-10): "))

        # We need to reach out and update the global counter.
        # Without the "global" keyword Python would create a
        # brand-new local variable instead of touching the real one.
        global total_rolls

        # Only accept a number between 1 and 10.
        # If the player types 0, -3, or 99 we politely refuse
        # and send them back to the beginning of main().
        if times < 1 or times > 10:
            print("Please enter a number between 1 and 10.")
            return main()

        # Add this round's rolls to the running total.
        total_rolls += times

        # Roll the dice "times" number of times, one by one.
        # i goes 0, 1, 2 ... so we add 1 to show a friendly
        # "Roll 1", "Roll 2" label instead of "Roll 0".
        for i in range(times):
            die1, die2 = roll_dice()
            print(f"({i + 1}) 🎲:({die1}, {die2})")

        # Round is done — ask if they want to go again.
        return main()

    elif choice == "n":
        # The player is done. Say goodbye and show the score.
        print("Thanks for playing!")
        print(f"You rolled the dice {total_rolls} time(s) this session.")

    else:
        # They typed something unexpected (not "y" or "n").
        # Let's gently nudge them back to try again.
        print('Please type "y" to roll or "n" to quit.')
        main()


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------
# This is where the story begins. When Python runs this file
# it reaches this line and kicks off the main() function.
# Everything above was just defining the pieces — this line
# actually starts the game.
main()
