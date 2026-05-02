# -*- coding: utf-8 -*-
# ============================================================
# PYTHON MINI GAMES — Desktop App
# ============================================================
# A tkinter GUI that hosts two games in separate tabs:
#   • Number Guessing Game  (same logic as number_guessing_game.py)
#   • Dice Rolling Game     (same logic as dice_rolling_game.py)
# ============================================================

import random
import tkinter as tk
from tkinter import ttk, messagebox

# Unicode dice faces for the six sides
DICE_FACES = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}


# ──────────────────────────────────────────────────────────
# NUMBER GUESSING GAME TAB
# ──────────────────────────────────────────────────────────
class NumberGuessingGame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.number_one    = None
        self.number_two    = None
        self.attempts_left = None
        self.secret_number = None
        self.game_active   = False
        self._build_ui()

    # ── UI layout ──────────────────────────────────────────
    def _build_ui(self):
        # Setup panel
        setup = ttk.LabelFrame(self, text="  Game Setup  ", padding=15)
        setup.pack(fill="x", padx=20, pady=(15, 8))

        row1 = ttk.Frame(setup)
        row1.pack(fill="x")

        ttk.Label(row1, text="From:").grid(row=0, column=0, padx=(0, 4), sticky="w")
        self.entry_num1 = ttk.Entry(row1, width=8)
        self.entry_num1.insert(0, "1")
        self.entry_num1.grid(row=0, column=1, padx=(0, 16))

        ttk.Label(row1, text="To:").grid(row=0, column=2, padx=(0, 4), sticky="w")
        self.entry_num2 = ttk.Entry(row1, width=8)
        self.entry_num2.insert(0, "100")
        self.entry_num2.grid(row=0, column=3, padx=(0, 16))

        ttk.Label(row1, text="Attempts:").grid(row=0, column=4, padx=(0, 4), sticky="w")
        self.entry_attempts = ttk.Entry(row1, width=8)
        self.entry_attempts.insert(0, "10")
        self.entry_attempts.grid(row=0, column=5, padx=(0, 16))

        self.btn_start = ttk.Button(setup, text="🎮  Start Game",
                                    command=self.start_game, style="Accent.TButton")
        self.btn_start.pack(pady=(12, 0))

        # Guess panel
        guess_panel = ttk.LabelFrame(self, text="  Your Guess  ", padding=15)
        guess_panel.pack(fill="x", padx=20, pady=8)

        self.lbl_prompt = ttk.Label(guess_panel,
                                    text="Configure the game above and press Start.",
                                    font=("Segoe UI", 10, "italic"))
        self.lbl_prompt.pack(pady=(0, 8))

        guess_row = ttk.Frame(guess_panel)
        guess_row.pack()

        self.entry_guess = ttk.Entry(guess_row, width=14, font=("Segoe UI", 13),
                                     state="disabled")
        self.entry_guess.grid(row=0, column=0, padx=5)
        self.entry_guess.bind("<Return>", lambda _: self.submit_guess())

        self.btn_submit = ttk.Button(guess_row, text="Submit",
                                     command=self.submit_guess, state="disabled")
        self.btn_submit.grid(row=0, column=1, padx=5)

        self.btn_quit_game = ttk.Button(guess_row, text="Quit Game",
                                        command=self.quit_game, state="disabled")
        self.btn_quit_game.grid(row=0, column=2, padx=5)

        self.lbl_attempts = ttk.Label(guess_panel, text="",
                                      font=("Segoe UI", 10))
        self.lbl_attempts.pack(pady=(8, 0))

        # Log
        log_frame = ttk.LabelFrame(self, text="  Game Log  ", padding=10)
        log_frame.pack(fill="both", expand=True, padx=20, pady=(8, 15))

        self.log_text = tk.Text(
            log_frame, height=10, state="disabled",
            font=("Consolas", 10), bg="#1e1e2e", fg="#cdd6f4",
            insertbackground="white", relief="flat", padx=6, pady=6,
            selectbackground="#45475a"
        )
        sb = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self.log_text.pack(fill="both", expand=True)

        self.log_text.tag_config("success", foreground="#a6e3a1")
        self.log_text.tag_config("error",   foreground="#f38ba8")
        self.log_text.tag_config("info",    foreground="#89dceb")
        self.log_text.tag_config("warning", foreground="#fab387")
        self.log_text.tag_config("header",  foreground="#cba6f7",
                                 font=("Consolas", 10, "bold"))

        self._log("Welcome to the Number Guessing Game!", "header")
        self._log("Set your range and attempts, then press Start.\n", "info")

    # ── Helpers ────────────────────────────────────────────
    def _log(self, message, tag=""):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", message + "\n", tag)
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def _set_controls(self, active: bool):
        state = "normal" if active else "disabled"
        self.btn_submit.configure(state=state)
        self.btn_quit_game.configure(state=state)
        self.entry_guess.configure(state=state)
        self.btn_start.configure(state="disabled" if active else "normal")
        if active:
            self.entry_guess.focus()

    # ── Game logic ─────────────────────────────────────────
    def start_game(self):
        try:
            n1  = int(self.entry_num1.get())
            n2  = int(self.entry_num2.get())
            att = int(self.entry_attempts.get())
        except ValueError:
            messagebox.showerror("Invalid Input",
                                 "Please enter whole numbers in all three fields.")
            return

        if n1 >= n2:
            messagebox.showerror("Invalid Range",
                                 "The first number must be less than the second.")
            return
        if att < 1:
            messagebox.showerror("Invalid Attempts",
                                 "You need at least 1 attempt.")
            return

        self.number_one    = n1
        self.number_two    = n2
        self.attempts_left = att
        self.secret_number = random.randint(n1, n2)
        self.game_active   = True

        self.entry_guess.delete(0, "end")
        self._set_controls(True)
        self.lbl_prompt.configure(
            text=f"Guess a number between {n1} and {n2}:",
            font=("Segoe UI", 10))
        self.lbl_attempts.configure(text=f"❤️   Attempts left: {att}")

        self._log("=" * 48, "header")
        self._log("🎮  New game started!", "header")
        self._log(f"🤫  I'm thinking of a number between {n1} and {n2}.", "info")
        self._log(f"❤️   You have {att} attempt(s). Type a number and press Submit.", "info")
        self._log("=" * 48 + "\n", "header")

    def submit_guess(self):
        if not self.game_active:
            return

        raw = self.entry_guess.get().strip()
        self.entry_guess.delete(0, "end")

        # Validate — match original: digits only (no negatives)
        if not raw.isdigit():
            self._log(f"⚠️  Invalid input. Please enter a number between "
                      f"{self.number_one} and {self.number_two}.", "warning")
            return

        guess = int(raw)
        self.attempts_left -= 1
        self.lbl_attempts.configure(
            text=f"❤️   Attempts left: {self.attempts_left}")
        self._log(f"🔢  You guessed: {guess}")

        if guess == self.secret_number:
            self._log("🎉  You guessed the number! Well done!", "success")
            self._end_game()
        elif guess < self.secret_number:
            self._log("📉  Too low!", "warning")
            if self.attempts_left <= 0:
                self._log(f"\n💀  Out of attempts! The number was {self.secret_number}.",
                          "error")
                self._end_game()
            else:
                self._log(f"❤️   {self.attempts_left} attempt(s) left.\n", "info")
        else:
            self._log("📈  Too high!", "warning")
            if self.attempts_left <= 0:
                self._log(f"\n💀  Out of attempts! The number was {self.secret_number}.",
                          "error")
                self._end_game()
            else:
                self._log(f"❤️   {self.attempts_left} attempt(s) left.\n", "info")

    def quit_game(self):
        if not self.game_active:
            return
        self._log(f"👋  Thanks for playing! The number was {self.secret_number}.", "info")
        self._end_game()

    def _end_game(self):
        self.game_active = False
        self._set_controls(False)
        self.lbl_prompt.configure(
            text="Game over — configure settings and press Start for a new game.",
            font=("Segoe UI", 10, "italic"))
        self.lbl_attempts.configure(text="")


# ──────────────────────────────────────────────────────────
# DICE ROLLING GAME TAB
# ──────────────────────────────────────────────────────────
class DiceRollingGame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.total_rolls = 0
        self._build_ui()

    # ── UI layout ──────────────────────────────────────────
    def _build_ui(self):
        ctrl = ttk.LabelFrame(self, text="  Roll Controls  ", padding=15)
        ctrl.pack(fill="x", padx=20, pady=(15, 8))

        row = ttk.Frame(ctrl)
        row.pack()

        ttk.Label(row, text="Times to roll (1–10):").grid(row=0, column=0,
                                                          padx=(0, 8))
        self.spin = ttk.Spinbox(row, from_=1, to=10, width=5,
                                font=("Segoe UI", 12))
        self.spin.set(1)
        self.spin.grid(row=0, column=1, padx=(0, 12))

        ttk.Button(row, text="🎲  Roll Dice!",
                   command=self.roll,
                   style="Accent.TButton").grid(row=0, column=2, padx=5)

        ttk.Button(row, text="🔄  Reset Session",
                   command=self.reset).grid(row=0, column=3, padx=5)

        # Session counter
        self.lbl_total = ttk.Label(
            self, text="🏆  Total rolls this session: 0",
            font=("Segoe UI", 11, "bold"))
        self.lbl_total.pack(pady=6)

        # Results log
        log_frame = ttk.LabelFrame(self, text="  Dice Results  ", padding=10)
        log_frame.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.log_text = tk.Text(
            log_frame, height=14, state="disabled",
            font=("Consolas", 11), bg="#1e1e2e", fg="#cdd6f4",
            insertbackground="white", relief="flat", padx=6, pady=6,
            selectbackground="#45475a"
        )
        sb = ttk.Scrollbar(log_frame, orient="vertical",
                           command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self.log_text.pack(fill="both", expand=True)

        self.log_text.tag_config("header", foreground="#cba6f7",
                                 font=("Consolas", 11, "bold"))
        self.log_text.tag_config("roll",   foreground="#a6e3a1")
        self.log_text.tag_config("info",   foreground="#89dceb")
        self.log_text.tag_config("total",  foreground="#fab387",
                                 font=("Consolas", 11, "bold"))

        self._log("🎲  Welcome to the Dice Roller!", "header")
        self._log("Pick how many times to roll and press Roll Dice.\n", "info")

    # ── Helpers ────────────────────────────────────────────
    def _log(self, message, tag=""):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", message + "\n", tag)
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    # ── Game logic ─────────────────────────────────────────
    def roll(self):
        try:
            times = int(self.spin.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please select a valid number.")
            return

        if times < 1 or times > 10:
            messagebox.showwarning("Out of Range",
                                   "Please enter a number between 1 and 10.")
            return

        self.total_rolls += times
        self.lbl_total.configure(
            text=f"🏆  Total rolls this session: {self.total_rolls}")

        self._log(f"── Rolling {times} time(s) ──────────────────────", "header")
        for i in range(times):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            face1 = DICE_FACES[die1]
            face2 = DICE_FACES[die2]
            self._log(f"  ({i + 1})  {face1} {die1}   {face2} {die2}"
                      f"   →  Sum: {die1 + die2}", "roll")
        self._log(f"  Session total: {self.total_rolls} roll(s)\n", "total")

    def reset(self):
        self.total_rolls = 0
        self.lbl_total.configure(text="🏆  Total rolls this session: 0")
        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", "end")
        self.log_text.configure(state="disabled")
        self._log("🔄  Session reset.", "info")
        self._log("Pick how many times to roll and press Roll Dice.\n", "info")


# ──────────────────────────────────────────────────────────
# MAIN APPLICATION WINDOW
# ──────────────────────────────────────────────────────────
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Mini Games")
        self.geometry("720x620")
        self.minsize(620, 520)
        self.configure(bg="#181825")
        self._apply_styles()
        self._build_ui()

    def _apply_styles(self):
        s = ttk.Style(self)
        s.theme_use("clam")

        bg      = "#181825"
        surface = "#313244"
        hover   = "#45475a"
        text    = "#cdd6f4"
        accent  = "#cba6f7"

        s.configure(".",
                    background=bg, foreground=text,
                    font=("Segoe UI", 10), borderwidth=0)
        s.configure("TFrame",        background=bg)
        s.configure("TLabel",        background=bg, foreground=text)
        s.configure("TLabelframe",   background=bg, foreground=accent,
                    relief="solid", bordercolor=surface, borderwidth=1)
        s.configure("TLabelframe.Label",
                    background=bg, foreground=accent,
                    font=("Segoe UI", 10, "bold"))
        s.configure("TButton",
                    background=surface, foreground=text,
                    relief="flat", padding=(10, 6))
        s.map("TButton",
              background=[("active", hover), ("pressed", "#585b70")])
        s.configure("Accent.TButton",
                    background="#7c3aed", foreground="#ffffff",
                    font=("Segoe UI", 10, "bold"), padding=(12, 7))
        s.map("Accent.TButton",
              background=[("active", "#6d28d9"), ("pressed", "#5b21b6")])
        s.configure("TEntry",
                    fieldbackground=surface, foreground=text,
                    insertcolor=text, relief="flat")
        s.configure("TSpinbox",
                    fieldbackground=surface, foreground=text,
                    arrowcolor=text, relief="flat")
        s.configure("TNotebook",
                    background=bg, tabmargins=[2, 5, 2, 0])
        s.configure("TNotebook.Tab",
                    background=surface, foreground=text,
                    padding=[16, 7], font=("Segoe UI", 10))
        s.map("TNotebook.Tab",
              background=[("selected", hover)],
              foreground=[("selected", accent)])
        s.configure("TScrollbar",
                    background=surface, troughcolor=bg,
                    arrowcolor=text, relief="flat")

    def _build_ui(self):
        # Header
        tk.Label(self, text="🎮  Python Mini Games",
                 font=("Segoe UI", 17, "bold"),
                 bg="#181825", fg="#cba6f7").pack(pady=(18, 2))
        tk.Label(self, text="Pick a game from the tabs below",
                 font=("Segoe UI", 9),
                 bg="#181825", fg="#6c7086").pack(pady=(0, 10))

        # Notebook
        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        num_tab  = NumberGuessingGame(nb)
        dice_tab = DiceRollingGame(nb)

        nb.add(num_tab,  text="  🔢  Number Guessing  ")
        nb.add(dice_tab, text="  🎲  Dice Roller  ")


# ──────────────────────────────────────────────────────────
# ENTRY POINT
# ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = App()
    app.mainloop()
