import tkinter as tk
from tkinter import messagebox
import random

# Tic-Tac-Toe logic
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def make_move(self, position):
        if self.board[position] == " " and not self.game_over:
            self.board[position] = self.current_player
            if self.check_winner():
                self.game_over = True
                return f"Player {self.current_player} wins!"
            elif " " not in self.board:
                self.game_over = True
                return "It's a draw!"
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        return None

def play_tic_tac_toe():
    def on_click(button, position):
        result = tic_tac_toe_game.make_move(position)
        if result:
            messagebox.showinfo("Result", result)
        button.config(text=tic_tac_toe_game.board[position])
        if tic_tac_toe_game.game_over:
            disable_buttons()
            tic_tac_toe_window.protocol("WM_DELETE_WINDOW", tic_tac_toe_window.destroy)  # Close window on game over

    def disable_buttons():
        for button in buttons:
            button.config(state=tk.DISABLED)

    tic_tac_toe_window = tk.Toplevel()
    tic_tac_toe_window.title("Tic-Tac-Toe")

    tic_tac_toe_game = TicTacToe()
    buttons = []
    for i in range(9):
        row, col = divmod(i, 3)
        button = tk.Button(tic_tac_toe_window, text=" ", width=10, height=4,
                        command=lambda pos=i: on_click(buttons[pos], pos))
        button.grid(row=row, column=col)
        buttons.append(button)

# Rock-Paper-Scissors logic
def play_rock_paper_scissors():
    def show_result(user_choice):
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Paper" and computer_choice == "Rock") or \
            (user_choice == "Scissors" and computer_choice == "Paper"):
            result = f"You win! {user_choice} beats {computer_choice}."
        else:
            result = f"You lose! {computer_choice} beats {user_choice}."
        messagebox.showinfo("Result", result)

    rock_paper_scissors_window = tk.Toplevel()
    rock_paper_scissors_window.title("Rock-Paper-Scissors")

    rock_button = tk.Button(rock_paper_scissors_window, text="Rock", command=lambda: show_result("Rock"))
    paper_button = tk.Button(rock_paper_scissors_window, text="Paper", command=lambda: show_result("Paper"))
    scissors_button = tk.Button(rock_paper_scissors_window, text="Scissors", command=lambda: show_result("Scissors"))

    rock_button.pack(side=tk.LEFT, padx=5, pady=10)
    paper_button.pack(side=tk.LEFT, padx=5, pady=10)
    scissors_button.pack(side=tk.LEFT, padx=5, pady=10)

# Number Guessing logic
class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.secret_number:
            return True
        elif guess < self.secret_number:
            messagebox.showinfo("Result", "Try a higher number.")
        else:
            messagebox.showinfo("Result", "Try a lower number.")
        return False

    def play_game(self):
        def on_submit():
            try:
                user_guess = int(guess_entry.get())
                if self.check_guess(user_guess):
                    messagebox.showinfo("Result", f"Congratulations! You guessed the number in {self.attempts} attempts.")
                    number_guessing_window.destroy()
                guess_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")

        number_guessing_window = tk.Toplevel()
        number_guessing_window.title("Number Guessing Game")

        instruction_label = tk.Label(number_guessing_window, text="Guess a number between 1 and 100:")
        instruction_label.pack(pady=10)

        guess_entry = tk.Entry(number_guessing_window)
        guess_entry.pack(pady=5)

        submit_button = tk.Button(number_guessing_window, text="Submit", command=on_submit)
        submit_button.pack(pady=10)

def show_message(game_name):
    messagebox.showinfo("Game Selection", f"You selected {game_name}!")
    if game_name == "Tic-Tac-Toe":
        play_tic_tac_toe()
    elif game_name == "Rock-Paper-Scissors":
        play_rock_paper_scissors()
    elif game_name == "Number Guessing Game":
        number_guessing_game = NumberGuessingGame()
        number_guessing_game.play_game()

#calling 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game Combination")

    game_list = ["Tic-Tac-Toe", "Rock-Paper-Scissors", "Number Guessing Game"]
    game_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
    for game in game_list:
        game_listbox.insert(tk.END, game)
    game_listbox.pack(pady=10)

    game_listbox.bind("<<ListboxSelect>>", lambda event: show_message(game_listbox.get(game_listbox.curselection())))

    root.mainloop()
