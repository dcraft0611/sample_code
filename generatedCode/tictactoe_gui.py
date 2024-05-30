import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def button_click(row, col):
    global player

    if board[row][col] == ' ':
        buttons[row][col].config(text=player)
        board[row][col] = player

        if check_winner(board):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            player = 'O' if player == 'X' else 'X'

def reset_game():
    global board, player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ')

root = tk.Tk()
root.title("Tic Tac Toe")

board = [[' ' for _ in range(3)] for _ in range(3)]
player = 'X'

buttons = [[None]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2,
                                   command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=reset_game)
reset_button.grid(row=3, column=1, pady=10)

root.mainloop()
