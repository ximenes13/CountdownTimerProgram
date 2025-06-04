# ⏳ Countdown Timer App with Python + Tkinter

This project is a sleek, responsive desktop application built using Python and Tkinter, designed to function as a countdown timer. Simply input a time in seconds and hit "Start Countdown" to begin. The app updates in real-time and alerts the user when the countdown hits zero.

---

## 🚀 Features

🕒 Countdown from any number of seconds to zero (formatted as HH:MM:SS) <br>
🧮 Real-time updates with a dynamic label <br>
🚦 "Start Countdown" button that disables during the countdown <br>
🧹 "Clear" button to reset timer and input <br>
🔁 Multithreaded countdown logic to keep the UI responsive <br>
📏 Responsive layout with auto-scaling font size <br>
🧠 Error handling for invalid or non-positive inputs <br>
🪟 Built entirely with native Tkinter widgets — no third-party dependencies <br>

---

## 🖥️ Technologies Used

- Python 3.x
- Tkinter (for GUI interface)
- PyCharm (recommended IDE)

---

## 📂 Project Structure

- **main.py**:  Core application script. Handles both UI and logic.

💡 Uses threading.Thread to run the countdown in the background <br>
⌨️ Accepts input for total countdown seconds via an Entry widget <br>
🧭 Converts raw seconds to HH:MM:SS format on each tick <br>
🎨 Implements responsive font resizing using .bind("<Configure>") <br>
🧹 Reset logic clears the display and input field <br>
🛡️ Input validation ensures only positive integers are accepted <br>

---

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

`git clone https://github.com/your-username/CountdownTimerProgram.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:

`python3 --version`

### Step 3: Run the project

Once you've installed the dependencies, you can run the main Python script to generate and interact with the calculator app.

`python3 main.py`

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/ximenes13/Calculator/issues).
