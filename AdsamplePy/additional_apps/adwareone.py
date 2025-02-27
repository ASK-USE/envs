import tkinter as tk
from tkinter import messagebox
import random

class AdwareOn:
    def __init__(self, master):
        self.master = master
        master.title("AdwareOn")
        master.geometry("300x200")
        master.configure(bg='yellow')

        self.label = tk.Label(master, text="Willkommen bei AdwareOn!", bg='yellow', font=("Arial", 14))
        self.label.pack(pady=20)

        self.button = tk.Button(master, text="Klick mich!", command=self.show_ad)
        self.button.pack()

    def show_ad(self):
        ads = [
            "Kaufen Sie jetzt! Nur für kurze Zeit!",
            "Sie sind der 1.000.000 Besucher! Gewinnen Sie einen Preis!",
            "Unglaubliches Angebot! Nicht verpassen!",
            "Verdienen Sie Geld von zu Hause aus!",
            "Kostenlose Geschenke warten auf Sie!"
        ]
        messagebox.showinfo("Werbung", random.choice(ads))

if __name__ == "__main__":
    root = tk.Tk()
    app = AdwareOn(root)
    root.mainloop()
