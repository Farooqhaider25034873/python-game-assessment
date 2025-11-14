import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match Game")
        self.root.geometry("400x400")
        self.symbols = ['🍎', '🍌', '🍇', '🍓'] * 2
        random.shuffle(self.symbols)
        self.buttons = []
        self.revealed = []
        self.matched = []
        self.score = 0
        self.create_grid()

    def create_grid(self):
        for i in range(4):
            for j in range(2):
                index = i * 2 + j
                btn = tk.Button(self.root, text="❓", font=("Arial", 24), width=4, height=2,
                                command=lambda idx=index: self.reveal(idx))
                btn.grid(row=i, column=j, padx=10, pady=10)
                self.buttons.append(btn)

    def reveal(self, idx):
        if idx in self.matched or idx in self.revealed:
            return
        self.buttons[idx].config(text=self.symbols[idx])
        self.revealed.append(idx)
        if len(self.revealed) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        i1, i2 = self.revealed
        if self.symbols[i1] == self.symbols[i2]:
            self.matched.extend([i1, i2])
            self.score += 1
        else:
            self.buttons[i1].config(text="❓")
            self.buttons[i2].config(text="❓")
        self.revealed.clear()
        if len(self.matched) == len(self.symbols):
            self.show_win()

    def show_win(self):
        win_label = tk.Label(self.root, text=f"You won! Score: {self.score}", font=("Arial", 16), fg="green")
        win_label.grid(row=5, column=0, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()