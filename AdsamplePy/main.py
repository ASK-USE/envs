import tkinter as tk
from tkinter import ttk
import time
from additional_apps.adwareone import AdwareOne

class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Installer")
        master.geometry("300x150")

        self.label = tk.Label(master, text="Willkommen zum Installer")
        self.label.pack(pady=20)

        self.install_button = tk.Button(master, text="Installieren", command=self.open_install_window)
        self.install_button.pack()

    def open_install_window(self):
        self.install_window = tk.Toplevel(self.master)
        self.install_window.title("Installation")
        self.install_window.geometry("400x200")

        self.progress = ttk.Progressbar(self.install_window, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        self.continue_button = tk.Button(self.install_window, text="Installation fortfahren", command=lambda: self.start_installation(False))
        self.continue_button.pack(side=tk.LEFT, padx=10)

        self.optimize_button = tk.Button(self.install_window, text="Installieren und System optimieren", command=lambda: self.start_installation(True))
        self.optimize_button.pack(side=tk.RIGHT, padx=10)

    def start_installation(self, optimize):
        self.continue_button.config(state='disabled')
        self.optimize_button.config(state='disabled')
        self.simulate_progress()
        if optimize:
            self.launch_adwareone()

    def simulate_progress(self):
        if self.progress["value"] < 100:
            self.progress["value"] += 5
            self.install_window.after(100, self.simulate_progress)
        else:
            self.install_window.destroy()

    def launch_adwareone(self):
        adware_window = tk.Toplevel(self.master)
        AdwareOne(adware_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
