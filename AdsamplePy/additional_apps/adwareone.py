import tkinter as tk
from tkinter import ttk
import random
import time

class AdwareOne:
    def __init__(self, master):
        self.master = master
        master.title("AdwareOne")
        master.geometry("400x300")
        master.configure(bg='yellow')

        self.label = tk.Label(master, text="Willkommen bei AdwareOne!", bg='yellow', font=("Arial", 14))
        self.label.pack(pady=20)

        self.button = tk.Button(master, text="Klick mich!", command=self.start_fake_install)
        self.button.pack()

        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        self.status_label = tk.Label(master, text="", bg='yellow')
        self.status_label.pack()

    def start_fake_install(self):
        self.button.config(state='disabled')
        self.progress["value"] = 0
        self.fake_install()

    def fake_install(self):
        if self.progress["value"] < 100:
            self.progress["value"] += 5
            self.update_status()
            self.master.after(250, self.fake_install)
        else:
            self.show_completion_message()
            self.show_ad()
            self.button.config(state='normal')

    def update_status(self):
        fake_actions = [
            "Downloading additional components...",
            "Updating system registry...",
            "Installing browser extensions...",
            "Configuring startup items...",
            "Optimizing system performance...",
            "Integrating with operating system...",
            "Bypassing security measures...",
            "Establishing remote connections...",
            "Injecting code into system processes...",
            "Hiding installation traces..."
        ]
        self.status_label.config(text=random.choice(fake_actions))

    def show_completion_message(self):
        completion_messages = [
            "Installation complete! You now have premium access!",
            "Congratulations! Your system is now optimized!",
            "Thank you for installing AdwareOne! Enjoy your new features!",
            "Setup finished successfully. Prepare for a better internet experience!",
            "AdwareOne is now protecting your system. Click for amazing offers!"
        ]
        self.status_label.config(text=random.choice(completion_messages))

    def show_ad(self):
        ad_window = tk.Toplevel(self.master)
        ad_window.title("Special Offer!")
        ad_window.geometry("300x200")
        ad_window.configure(bg='light green')

        ads = [
            "Kaufen Sie jetzt! Nur für kurze Zeit!",
            "Sie sind der 1.000.000 Besucher! Gewinnen Sie einen Preis!",
            "Unglaubliches Angebot! Nicht verpassen!",
            "Verdienen Sie Geld von zu Hause aus!",
            "Kostenlose Geschenke warten auf Sie!"
        ]
        ad_text = random.choice(ads)

        ad_label = tk.Label(ad_window, text=ad_text, bg='light green', font=("Arial", 12), wraplength=250)
        ad_label.pack(expand=True)

        close_button = tk.Button(ad_window, text="Schließen", command=ad_window.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdwareOne(root)
    root.mainloop()
