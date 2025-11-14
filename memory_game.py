# Final push — Farooq hadir confirmed update
import tkinter as tk
import random
# GUI layout improved with better emoji variety
class ColorMatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Match Reflex")
        self.root.geometry("400x300")
        self.score = 0
        self.colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange']
        self.symbols = ['🍎', '🍌', '🍇', '🍓', '🍍', '🥝']
        self.current_color = ''
        self.current_symbol = ''
        self.create_widgets()
        self.next_round()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="", font=("Arial", 24))
        self.label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack()

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        self.buttons = []
        for color in self.colors:
            btn = tk.Button(self.buttons_frame, text=color, width=10, command=lambda c=color: self.check_answer(c))
            btn.pack(side=tk.LEFT, padx=5)
            self.buttons.append(btn)

        self.restart_btn = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_btn.pack(pady=10)

    def next_round(self):
        self.current_color = random.choice(self.colors)
        self.current_symbol = random.choice(self.symbols)
        self.label.config(text=f"{self.current_symbol}", fg=self.current_color)

    def check_answer(self, selected_color):
        if selected_color == self.current_color:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            if self.score >= 10:
                self.show_win()
            else:
                self.next_round()
        else:
            self.score = 0
            self.score_label.config(text="Score: 0")
            self.next_round()

    def show_win(self):
        self.label.config(text="🎉 You Win!", fg="black")
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def restart_game(self):
        self.score = 0
        self.score_label.config(text="Score: 0")
        for btn in self.buttons:
            btn.config(state=tk.NORMAL)
        self.next_round()

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorMatchGame(root)
    root.mainloop()
