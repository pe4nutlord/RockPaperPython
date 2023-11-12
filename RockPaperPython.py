import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == '🪨' and computer_choice == '✂️') or \
         (user_choice == '📄' and computer_choice == '🪨') or \
         (user_choice == '✂️' and computer_choice == '📄'):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    computer_choice = random.choice(['🪨', '📄', '✂️'])
    result = determine_winner(user_choice, computer_choice)
    update_result_label(user_choice, computer_choice, result)

def update_result_label(user_choice, computer_choice, result):
    result_label.config(text=f"You chose {user_choice}   |   Computer chose {computer_choice}\n{result}")

# Function to create custom rounded buttons with emojis
def create_rounded_button(root, text, emoji, command):
    button = tk.Button(root, text=emoji, font=('Arial', 18), width=4, height=2, command=command, borderwidth=5, relief=tk.GROOVE)
    button.config(bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white")
    button.pack(side=tk.LEFT, padx=10)
    return button

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Python")

# Set fixed window size
root.geometry("400x200")

# Function to create and set up the GUI
def setup_gui():
    label = tk.Label(root, text="Rock-Paper-Python", font=('Arial', 24), pady=10)
    label.config(fg="#3498db")
    label.pack()

    global result_label
    result_label = tk.Label(root, text="", font=('Arial', 16), justify="center")
    result_label.pack(pady=20)

    # Buttons with emojis and commands
    create_rounded_button(root, "Rock", "🪨", lambda: play_game("🪨"))
    create_rounded_button(root, "Paper", "📄", lambda: play_game("📄"))
    create_rounded_button(root, "Scissors", "✂️", lambda: play_game("✂️"))

# Set up the GUI
setup_gui()

# Run the Tkinter event loop
root.mainloop()
