import tkinter as tk
import tkinter.messagebox as msg
class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" "]*9

        # Create buttons for the game board
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", font=("Helvetica", 32), 
                                width=3, height=1, command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Create a reset button
        reset_button = tk.Button(self.master, text="Reset Game", font=("Helvetica", 16),
                                command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3)

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.check_win():
                # tk.messagebox.showinfo("Congratulations!", f"{self.current_player} won!")
                msg.showinfo("Congratulations!", f"{self.current_player} won!")

                self.reset_game()
            elif self.check_tie():
                # tk.messagebox.showinfo("Tie Game!", "It's a tie!")
                msg.showinfo("Tie Game!", "It's a tie!")

                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def check_tie(self):
        return " " not in self.board

    def reset_game(self):
        self.current_player = "X"
        self.board = [" "]*9
        for button in self.buttons:
            button.config(text=" ")

root = tk.Tk()
game = TicTacToe(root)
root.geometry("500x500")
root.mainloop()
