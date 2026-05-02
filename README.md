# Python Projects for Beginners

A collection of small, well-commented Python projects built for people who are just starting out.

---

## 🎲 Dice Rolling Game (`dice_rolling_game.py`)

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
  Roll 1: 🎲 4  🎲 2
  Roll 2: 🎲 6  🎲 1
  Roll 3: 🎲 3  🎲 5
Roll the Dice? (y/n): n
Thanks for playing!
You rolled the dice 3 time(s) this session.
```

### Bug fixes applied
- `roll_dice()` was being called without its required argument — fixed by refactoring to a global counter
- Input guard used `< 0` instead of `< 1`, allowing `0` rolls — corrected to `< 1`
- Return values were accidentally built as Python sets `{}` — replaced with clean statements
- `print(main())` at the bottom was printing `None` — changed to a plain `main()` call
