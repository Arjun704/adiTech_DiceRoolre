import tkinter as tk
from tkinter import messagebox
import random

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller App")
        
        self.label = tk.Label(root, text="Select the number of dice:")
        self.label.pack(pady=10)
        
        self.dice_count = tk.IntVar()
        self.dice_count.set(2)
        
        self.dice_count_menu = tk.OptionMenu(root, self.dice_count, 1, 2, 3, 4, 5,6)
        self.dice_count_menu.pack()
        
        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=10)
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()
        
    def roll_dice(self):
        num_dice = self.dice_count.get()
        dice_results = [random.randint(1, 7) for _ in range(num_dice)]
        
        result_str = "Dice Rolled: " + ", ".join(map(str, dice_results))
        
        total_sum = sum(dice_results)
        result_str += "\nTotal: " + str(total_sum)
        
        messagebox.showinfo("Dice Roll Result", result_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()
