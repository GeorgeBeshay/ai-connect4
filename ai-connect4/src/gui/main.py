import tkinter as tk
from tkinter import messagebox


def create_game_board(game_window, rows, cols):
    game_window.configure(bg="#34495e")  # Change game window background color
    canvas = tk.Canvas(game_window, width=110 * cols, height=110 * rows, bg="#3498db")  # Change canvas size and background color
    canvas.pack(padx=20, pady=20)

    cell_size = 110  # Increase cell size for a larger board
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_oval(x1, y1, x2, y2, fill="white", outline="black")


def start_game():
    selected_option = var.get()  # Get the selected option (A or B)
    k_value = entry_k.get()  # Get the value of k
    rows = int(entry_rows.get())  # Get the value of rows
    cols = int(entry_cols.get())  # Get the value of columns

    # Close the initial window
    root.withdraw()

    # Create a new window for the game board
    game_window = tk.Toplevel(root)
    game_window.title("Connect 4 Game Board")
    game_window.attributes('-fullscreen', True)  # Set the new window to fullscreen mode
    game_window.configure(bg="#34495e")  # Change game window background color

    # Create the game board
    create_game_board(game_window, rows, cols)

    # Example: Label showing game information
    game_label = tk.Label(game_window,
                          text=f"Selected Option: {selected_option}\tValue of k: {k_value}\tRows: {rows}\tColumns: {cols}",
                          font=(font_style, 16),
                          bg="#34495e", fg="white")  # Change label background and text color
    game_label.pack(padx=20, pady=20)

    # Button to exit the game
    exit_game_button = tk.Button(game_window, text="Exit Game", command=exit_game, bg=button_color, fg=text_color,
                                 font=(font_style, 16, "bold"), relief=tk.GROOVE)
    exit_game_button.pack(pady=10)


def select_option(option):
    var.set(option)
    if option == "Pure Minimax":
        option_pure_minimax.config(bg="#27ae60", relief=tk.SUNKEN, fg="white")
        option_minimax_with.config(bg=button_color, relief=tk.RAISED, fg=text_color)
    else:
        option_minimax_with.config(bg="#27ae60", relief=tk.SUNKEN, fg="white")
        option_pure_minimax.config(bg=button_color, relief=tk.RAISED, fg=text_color)


def exit_game():
    root.destroy()


root = tk.Tk()
root.title("Connect 4 Game")
root.geometry("800x600")  # Set the window size

# Define new colors
bg_color = "#34495e"
button_color = "#2ecc71"
text_color = "#0a4854"
white_color = "white"
font_style = "Lucida Handwriting"

root.configure(bg=bg_color)

top_frame = tk.Frame(root, bg=bg_color)
top_frame.pack(expand=True, pady=(50, 20))

bottom_frame = tk.Frame(root, bg=bg_color)
bottom_frame.pack(expand=True, pady=(0, 50))

var = tk.StringVar()

option_label = tk.Label(bottom_frame, text="Choose an option:", fg=white_color, bg=bg_color, font=(font_style, 26))
option_label.pack(pady=10)

option_frame = tk.Frame(bottom_frame, bg=bg_color)
option_frame.pack(pady=10)

option_pure_minimax = tk.Button(option_frame, text="Pure Minimax", command=lambda: select_option("Pure Minimax"),
                                bg=button_color, fg=text_color, font=(font_style, 22, "bold"), relief=tk.SUNKEN)
option_pure_minimax.grid(row=0, column=0, padx=20, pady=5)

option_minimax_with = tk.Button(option_frame, text="Minimax with Alpha-Beta Pruning",
                                command=lambda: select_option("Minimax with Alpha-Beta Pruning"), bg=button_color,
                                fg=text_color, font=(font_style, 22, "bold"), relief=tk.RAISED)
option_minimax_with.grid(row=1, column=0, padx=20, pady=5)

entry_label_k = tk.Label(top_frame, text="K:", fg=white_color, bg=bg_color, font=(font_style, 26))
entry_label_k.pack(pady=10, side=tk.LEFT, padx=20)

entry_k = tk.Entry(top_frame, font=(font_style, 22), justify='center', width=5, fg="black")
entry_k.pack(side=tk.LEFT, padx=10)
entry_k.insert(0, "2")

entry_label_rows = tk.Label(top_frame, text="Rows:", fg=white_color, bg=bg_color, font=(font_style, 26))
entry_label_rows.pack(pady=10, side=tk.LEFT, padx=20)

entry_rows = tk.Entry(top_frame, font=(font_style, 22), justify='center', width=5, fg="black")
entry_rows.pack(side=tk.LEFT, padx=10)
entry_rows.insert(0, "6")

entry_label_cols = tk.Label(top_frame, text="Cols:", fg=white_color, bg=bg_color, font=(font_style, 26))
entry_label_cols.pack(pady=10, side=tk.LEFT, padx=20)

entry_cols = tk.Entry(top_frame, font=(font_style, 22), justify='center', width=5, fg="black")
entry_cols.pack(side=tk.LEFT, padx=10)
entry_cols.insert(0, "7")

select_option("Pure Minimax")

start_button = tk.Button(bottom_frame, text="Start Game", command=start_game, bg=button_color, fg=text_color,
                         font=(font_style, 28, "bold"), relief=tk.GROOVE)
start_button.pack(pady=30)

exit_button = tk.Button(bottom_frame, text="Exit Game", command=exit_game, bg=button_color, fg=text_color,
                        font=(font_style, 28, "bold"), relief=tk.GROOVE)
exit_button.pack(pady=10)

root.attributes('-fullscreen', True)
root.mainloop()