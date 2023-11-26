import tkinter as tk
from tkinter import messagebox

def start_game():
    selected_option = var.get()  # Get the selected option (A or B)
    k_value = entry.get()  # Get the value of k
    messagebox.showinfo("Game Start", f"Selected Option: {selected_option}\nValue of k: {k_value}")

# Create the main window
root = tk.Tk()
root.title("Connect 4 Game")
root.geometry("500x400")  # Set a larger window size

# Configure background color to a darker gray
root.configure(bg="#222222")  # Darker gray background

# Entry for k value
entry_label = tk.Label(root, text="Enter k value:", fg="white", bg="#444444", font=("Arial", 12), justify='center')
entry_label.pack()

entry = tk.Entry(root, bg="white", justify='center')
entry.pack()

# Radio buttons for options A and B
var = tk.StringVar()
option_label = tk.Label(root, text="Choose an option:", fg="white", bg="#444444", font=("Arial", 12), justify='center')
option_label.pack()

radio_button_a = tk.Radiobutton(root, text="Option A", variable=var, value="A", fg="white", bg="#444444", font=("Arial", 10))
radio_button_a.pack()

radio_button_b = tk.Radiobutton(root, text="Option B", variable=var, value="B", fg="white", bg="#444444", font=("Arial", 10))
radio_button_b.pack()

# Button to start the game
start_button = tk.Button(root, text="Start Game", command=start_game, bg="#007bff", fg="white", font=("Arial", 14), relief=tk.GROOVE)
start_button.pack()

root.mainloop()
