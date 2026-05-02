import random


def roll_dice():
  return (random.randint(1,6), random.randint(1,6))

def main():
  data = input("Roll the Dice? (y/n): ", )

  if data == "y":
    return {print(roll_dice()), main()}
  elif data == "n":
    return {print("Exiting..."), exit()}
  else:
    return {print("Invalid input"), main()}

print( main())