import tkinter as tk
from tkinter import messagebox

class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Sichere Hauptanwendung")
        master.geometry("300x200")

        self.label = tk.Label(master, text="Willkommen zur sicheren Hauptanwendung!")
        self.label.pack(pady=20)

        self.button = tk.Button(master, text="Klick mich!", command=self.button_click)
        self.button.pack()

    def button_click(self):
        messagebox.showinfo("Info", "Dies ist eine sichere Anwendung.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
