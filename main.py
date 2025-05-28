import tkinter as tk
import time
import threading
from tkinter import ttk, font

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

def resize_font(event):
    new_size = max(12, int(event.width / 20))
    responsive_font.configure(size=new_size)
    result_label.config(wraplength=event.width)

def clear():
    entry_seconds.config(state="normal") # Enable to input
    entry_seconds.delete(0, tk.END) # Clear input
    result_var.set("00:00:00") # Reset countdown
    start_button.config(state="normal")   # Enable Start button

# App setup
app = tk.Tk()
app.title("Countdown Timer Program")
app.geometry("400x300")
app.resizable(True, True)
app.bind("<Configure>", resize_font)

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
ttk.Label(main_frame, text="⏳ Countdown Timer ⏳", font=("Calibre", 16, "bold")).grid(row=0, column=0, pady=(0, 10), sticky="n")

# Input Label
ttk.Label(main_frame, text="Enter time (seconds):").grid(row=1, column=0, pady=(10, 5), sticky="ew")

# Entry field
entry_seconds = ttk.Entry(main_frame, justify="center", font=("Arial", 14))
entry_seconds.grid(row=2, column=0, pady=5, sticky="ew")

# Button Frame
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")
button_frame.columnconfigure((0, 1), weight=1)

# Start button
start_button = ttk.Button(button_frame, text="Start Countdown", command=start_countdown)
start_button.grid(row=0, column=0, sticky="ew")

# Clear button
clear_button = ttk.Button(button_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=1, sticky="ew")

# Countdown result
result_var = tk.StringVar(value="00:00:00")
responsive_font = font.Font(family="Courier", size=24) # Responsive font for result display
result_label = tk.Label(main_frame, textvariable=result_var, font=responsive_font, anchor="center", wraplength=app.winfo_width(), justify="center")
result_label.grid(row=4, column=0, pady=10, sticky="nsew")

app.mainloop()
