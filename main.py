import tkinter as tk
from tkinter import ttk
import time
import threading

def start_countdown():
    try:
        total_seconds = int(entry_seconds.get())
        if total_seconds <= 0:
            raise ValueError

        start_button.config(state="disabled")
        entry_seconds.config(state="disabled")

        threading.Thread(target=run_countdown, args=(total_seconds,), daemon=True).start()

    except ValueError:
        result_var.set("Please enter a valid positive integer.")

def run_countdown(seconds):
    for x in range(seconds, -1, -1):
        hrs = x // 3600
        mins = (x % 3600) // 60
        secs = x % 60
        result_var.set(f"{hrs:02}:{mins:02}:{secs:02}")
        time.sleep(1)

    result_var.set("⏰ TIME'S UP!")
    start_button.config(state="normal")
    entry_seconds.config(state="normal")

# App setup
app = tk.Tk()
app.title("Countdown Timer Program")
app.geometry("400x300")
app.resizable(True, True)

# Configure root grid to be expandable
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

# Frame setup
main_frame = ttk.Frame(app, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")

# Make the frame itself responsive
for i in range(5):  # 5 rows used
    main_frame.rowconfigure(i, weight=1)
main_frame.columnconfigure(0, weight=1)

# Title
ttk.Label(main_frame, text="Countdown Timer", font=("Calibre", 16, "bold")).grid(row=0, column=0, pady=(0, 10), sticky="n")

# Input Label
ttk.Label(main_frame, text="Enter time (seconds):").grid(row=1, column=0, pady=(10, 5), sticky="ew")

# Entry field
entry_seconds = ttk.Entry(main_frame, justify="center", font=("Arial", 14))
entry_seconds.grid(row=2, column=0, pady=5, sticky="ew")

# Start button
start_button = ttk.Button(main_frame, text="Start Countdown", command=start_countdown)
start_button.grid(row=3, column=0, pady=10, sticky="ew")

# Countdown result
result_var = tk.StringVar(value="00:00:00")
result_label = ttk.Label(main_frame, textvariable=result_var, font=("Courier", 24), anchor="center")
result_label.grid(row=4, column=0, pady=10, sticky="nsew")

app.mainloop()
