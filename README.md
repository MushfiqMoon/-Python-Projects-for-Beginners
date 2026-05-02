# Python Projects for Beginners

A collection of small, well-commented Python projects built for people who are just starting out.
Each game is written in a story-telling style so the code reads like a journey, not a manual.

---

## Table of Contents

| # | Game | File | Description |
|---|------|------|-------------|
| 1 | [Dice Rolling Game](#1-dice-rolling-game) | `dice_rolling_game.py` | Roll two six-sided dice as many times as you like |
| 2 | [Number Guessing Game](#2-number-guessing-game) | `number_guessing_game.py` | Crack the secret number before your attempts run out |

---

## 1. Dice Rolling Game

> *Imagine you're sitting at a board game night with friends. Someone says "we need a dice roller!" — so you build one.*

A simple command-line dice roller that simulates throwing two six-sided dice.

### What it does
- Asks the player if they want to roll the dice
- Lets them choose how many rolls they want in one round (1–10)
- Displays the result of each individual roll
- Keeps a running total of all rolls across the whole session
- Loops back and asks again until the player chooses to quit

### Concepts covered

| Concept | Where it appears |
|---|---|
| `import` — using a built-in module | `import random` at the top |
| Functions (`def`) | `roll_dice()` and `main()` |
| `random.randint()` | Inside `roll_dice()` to simulate a die |
| `input()` | Asking the player what to do |
| `if / elif / else` | Branching based on player choices |
| `for` loop | Rolling the dice multiple times |
| Global variables | `total_rolls` shared across function calls |
| Recursion | `main()` calls itself to keep the game going |
| f-strings | Formatting the output with variable values |

### How to run

```bash
python dice_rolling_game.py
```

### Example output

```
Roll the Dice? (y/n): y
How many times to roll the dice? (1-10): 3
(1) 🎲:(4, 2)
(2) 🎲:(6, 1)
(3) 🎲:(3, 5)
Roll the Dice? (y/n): n
Thanks for playing!
You rolled the dice 3 time(s) this session.
```

### Bug fixes applied
- `roll_dice()` was being called without its required argument — fixed by refactoring to a global counter
- Input guard used `< 0` instead of `< 1`, allowing `0` rolls — corrected to `< 1`
- Return values were accidentally built as Python sets `{}` — replaced with clean statements
- `print(main())` at the bottom was printing `None` — changed to a plain `main()` call

---

## 2. Number Guessing Game

> *A friend hides a number in their head and dares you to figure it out. They'll tell you if you're too high or too low — but you only get so many tries.*

A classic number guessing game where you set the range and the number of attempts yourself.

### What it does
- Asks the player to define their own number range (e.g. 1 to 100)
- Asks the player how many attempts they want
- Picks a secret random number inside that range
- Gives "too high" or "too low" hints after each wrong guess
- Tracks remaining attempts and ends the game when they run out
- Accepts `q` at any time to quit gracefully

### Concepts covered

| Concept | Where it appears |
|---|---|
| `import` — using a built-in module | `import random` at the top |
| Functions (`def`) | `get_guess()` and `main()` |
| `random.randint()` | Inside `main()` to generate the secret number |
| `input()` + `int()` | Collecting the range and attempt count from the player |
| Input validation | `get_guess()` rejects non-numeric input with a friendly message |
| `while` loop | Keeps the game going while attempts remain |
| `while / else` | Detects when the loop ends naturally (no attempts left) |
| Global variables | `number_one`, `number_two`, `attempts` shared across functions |
| f-strings | Showing personalised prompts and feedback |

### How to run

```bash
python number_guessing_game.py
```

### Example output

```
Enter the first number:  1
Enter the second number: 50
Number of attempts:      5

================================================
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 50.
You have 5 attempt(s). Type 'q' to quit.
================================================

Guess a number between 1 and 50: 25
Too high!
You have 4 attempt(s) left.

Guess a number between 1 and 50: 12
Too low!
You have 3 attempt(s) left.

Guess a number between 1 and 50: 18
You guessed the number! Well done!
```

### Bug fixes applied
- `int(input(...))` crashed on non-numeric input — replaced with a safe `get_guess()` validator loop
- Quit check compared the `input` function object to `'q'` (always `False`) — fixed to check the actual user input
- Repeated `int(input(...))` calls scattered across the loop — consolidated into a single `get_guess()` helper
- Multi-line string literal caused a `SyntaxError` — rewritten using implicit string concatenation

---

## Credits

A huge thank you to **Mosh Hamedani** for the inspiration behind these projects.
If you're learning Python and haven't watched his tutorials yet, highly recommend checking them out:

▶️ [Python for Beginners — Mosh](https://www.youtube.com/watch?v=yVl_G-F7m8c)
