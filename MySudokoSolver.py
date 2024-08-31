import tkinter as tk
from tkinter import messagebox


class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(frame, textvariable=self.board[i][j], width=5, justify='center', font=("Arial", 18))
                entry.grid(row=i, column=j, padx=1, pady=1)
                self.entries[i][j] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.pack(pady=10)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear)
        clear_button.pack(pady=5)

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j].set("")

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.board[i][j].get()
                if value.isdigit():
                    row.append(int(value))
                else:
                    row.append(0)
            board.append(row)
        return board

    def solve(self):
        board = self.get_board()
        if self.solve_sudoku(board):
            self.display_solution(board)
        else:
            messagebox.showerror("Error", "No solution exists for the provided Sudoku")

    def display_solution(self, board):
        for i in range(9):
            for j in range(9):
                self.board[i][j].set(board[i][j])

    def find_empty_location(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_safe(self, board, row, col, num):
        if num in board[row]:
            return False

        if num in [board[i][col] for i in range(9)]:
            return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve_sudoku(self, board):
        empty_location = self.find_empty_location(board)
        if not empty_location:
            return True

        row, col = empty_location

        for num in range(1, 10):
            if self.is_safe(board, row, col, num):
                board[row][col] = num

                if self.solve_sudoku(board):
                    return True

                board[row][col] = 0

        return False


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()
