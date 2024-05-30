import tkinter as tk
import random
import time

# Define the size of the Tetris grid
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30

class TetrisGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tetris")
        self.canvas = tk.Canvas(self.root, width=GRID_WIDTH*BLOCK_SIZE, height=GRID_HEIGHT*BLOCK_SIZE, bg="black")
        self.canvas.pack()

        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_block = self.generate_block()
        self.current_block_x = 4
        self.current_block_y = 0
        self.score = 0
        self.game_over = False

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)

        self.update()

    def generate_block(self):
        return [[1, 1], [1, 1]]  # Square block

    def move_left(self, event):
        if not self.check_collision(self.current_block, self.current_block_x - 1, self.current_block_y):
            self.current_block_x -= 1

    def move_right(self, event):
        if not self.check_collision(self.current_block, self.current_block_x + 1, self.current_block_y):
            self.current_block_x += 1

    def move_down(self, event):
        if not self.check_collision(self.current_block, self.current_block_x, self.current_block_y + 1):
            self.current_block_y += 1
        else:
            self.lock_block()

    def lock_block(self):
        for y in range(len(self.current_block)):
            for x in range(len(self.current_block[0])):
                if self.current_block[y][x] == 1:
                    self.grid[self.current_block_y + y][self.current_block_x + x] = 1

        self.check_lines()
        self.current_block = self.generate_block()
        self.current_block_x = 4
        self.current_block_y = 0
        if self.check_collision(self.current_block, self.current_block_x, self.current_block_y):
            self.game_over = True

    def check_collision(self, block, x, y):
        for y_offset in range(len(block)):
            for x_offset in range(len(block[0])):
                if block[y_offset][x_offset] == 1:
                    grid_x = x + x_offset
                    grid_y = y + y_offset
                    if grid_x < 0 or grid_x >= GRID_WIDTH or grid_y >= GRID_HEIGHT or self.grid[grid_y][grid_x] == 1:
                        return True
        return False

    def check_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0] * GRID_WIDTH)
                lines_cleared += 1
        self.score += lines_cleared

    def update(self):
        if not self.game_over:
            self.canvas.delete("block")
            for y in range(GRID_HEIGHT):
                for x in range(GRID_WIDTH):
                    if self.grid[y][x] == 1:
                        self.canvas.create_rectangle(x*BLOCK_SIZE, y*BLOCK_SIZE, (x+1)*BLOCK_SIZE, (y+1)*BLOCK_SIZE, fill="cyan", tag="block")
            for y in range(len(self.current_block)):
                for x in range(len(self.current_block[0])):
                    if self.current_block[y][x] == 1:
                        self.canvas.create_rectangle((self.current_block_x + x) * BLOCK_SIZE, (self.current_block_y + y) * BLOCK_SIZE, (self.current_block_x + x + 1) * BLOCK_SIZE, (self.current_block_y + y + 1) * BLOCK_SIZE, fill="cyan", tag="block")
            self.root.after(500, self.update)
        else:
            self.canvas.create_text(GRID_WIDTH*BLOCK_SIZE/2, GRID_HEIGHT*BLOCK_SIZE/2, text=f"Game Over\nScore: {self.score}", fill="white", font=("Arial", 24))
        self.root.update_idletasks()
        self.root.update()

if __name__ == "__main__":
    game = TetrisGame()
    game.root.mainloop()
