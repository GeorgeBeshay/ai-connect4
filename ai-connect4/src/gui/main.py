import time
import tkinter as tk
from tkinter import messagebox, ttk
from src.controller.controller import Connect4Controller
from src.algorithms.minimax import *
from src.algorithms.minimax_with_alpha_beta import *
from src.state.state import State
from src.utilities.get_score import *
from typing import *


def toggle_minimax_tree_display():
    """
    Toggle the display of the Minimax tree.
    """
    global display_minimax_tree
    display_minimax_tree = not display_minimax_tree


def create_board_canvas(game_window, rows, cols):
    """
        Create a canvas for the game board.

        :param game_window: The window for the game board.
        :type game_window: tk.Toplevel
        :param rows: Number of rows in the game board.
        :type rows: int
        :param cols: Number of columns in the game board.
        :type cols: int

        :return: The created canvas for the game board.
        :rtype: tk.Canvas
    """
    cell_size = 4620 / (rows * cols)
    canvas = tk.Canvas(game_window, width=cell_size * cols, height=cell_size * rows, bg="#3498db")
    canvas.pack(padx=20, pady=20)
    return canvas


def update_game_board(canvas, controller, cell_size):
    """
        Update the game board displayed on the canvas.

        :param canvas: The canvas displaying the game board.
        :type canvas: tk.Canvas
        :param controller: The game controller.
        :type controller: Connect4Controller
        :param cell_size: Size of each cell on the board.
        :type cell_size: int
    """
    board_2d = controller.get_board()
    canvas.delete("all")  # Clear the canvas before updating

    rows = len(board_2d)
    cols = len(board_2d[0])

    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            # Map the integer values to colors
            if board_2d[row][col] == 2:
                fill_color = "blue"
            elif board_2d[row][col] == 1:
                fill_color = "red"
            else:
                fill_color = "white"

            canvas.create_oval(x1, y1, x2, y2, fill=fill_color, outline="black")


def column_click(event, canvas, controller, cell_size):
    """
        Handle the click event on the game board column.

        First, it applies the human player move, specified by the mouse click position, after that
        the chosen Ai agent method is being called, and the state is updated further by the created one from
        the Ai method.

        :param event: The click event.
        :param canvas: The canvas displaying the game board.
        :type canvas: tk.Canvas
        :param controller: The game controller.
        :type controller: Connect4Controller
        :param cell_size: Size of each cell on the board.
        :type cell_size: int
    """
    # Apply the user click
    controller.play(event.x // cell_size)
    update_game_board(canvas, controller, cell_size)

    canvas.update()

    # Apply the Ai agent move
    controller.set_state(ai_agent_play(controller.get_state()))
    update_game_board(canvas, controller, cell_size)

    # Change the displayed score
    update_score_label(controller)


def update_score_label(controller):
    global game_label, score_value

    score_value = get_game_score(controller.get_state().to_2d(), 1, 2)
    selected_option = var.get()  # Get the selected option (A or B)
    k_value = entry_k.get()  # Get the value of k
    rows = int(entry_rows.get())  # Get the value of rows
    cols = int(entry_cols.get())  # Get the value of columns

    game_label.config(text=f"Selected Option: {selected_option}\t"
                           f"Value of k: {k_value}\t"
                           f"Rows: {rows}\t"
                           f"Columns: {cols}\t"
                           f"Ai Agent VS. Player = ({score_value[0]}, {score_value[1]})",
                      font=(font_style, 14),
                      bg="#34495e", fg="white")


total_time = 0
counter = 0


def ai_agent_play(state: State) -> State:
    """
        Simulate the AI agent's move.

        :param state: The current state of the game.
        :type state: State

        :return: The updated state after the AI agent's move.
        :rtype: State
    """
    global total_time, counter
    approach = var.get()
    if approach == "Pure Minimax":
        minimax_solver = Minimax(int(entry_k.get()))
        start_time = time.time()
        new_state = minimax_solver.run_minimax(state)[1]
        end_time = time.time()
        if display_minimax_tree:
            minimax_solver.tree.display_tree()

        elapsed_time = end_time - start_time
        total_time += elapsed_time
        counter += 1
        # print(f"AI move took {elapsed_time} seconds")
        # print(f"Counter = {counter}")
        print(f"Average time = {total_time / counter} seconds")
        return new_state
    else:
        minimax_ab_solver = MinimaxWithAlphaBeta(int(entry_k.get()))
        start_time = time.time()
        new_state = minimax_ab_solver.run_minimax_with_alpha_beta(state)[1]
        end_time = time.time()
        if display_minimax_tree:
            minimax_ab_solver.tree.display_tree()

        elapsed_time = end_time - start_time
        total_time += elapsed_time
        counter += 1
        # print(f"AI move took {elapsed_time} seconds")
        print(f"Average time = {total_time / counter} seconds")
        # print(f"Counter = {counter}")
        return new_state


game_label: tk.Label
score_value = (0, 0)


def start_game():
    """
        Start the Connect 4 game.
    """
    global game_label, score_value
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

    # Create the game board controller
    controller = Connect4Controller(cols, rows)
    canvas = create_board_canvas(game_window, rows, cols)
    update_game_board(canvas, controller, cell_size=4620 // (rows * cols))  # Initial board setup

    # Bind the event for column click
    canvas.bind("<Button-1>",
                lambda event, p1=canvas, p2=controller, p3=4620 // (rows * cols): column_click(event, p1, p2, p3))

    # Example: Label showing game information
    game_label = tk.Label(game_window,
                          text=f"Selected Option: {selected_option}\t"
                               f"Value of k: {k_value}\t"
                               f"Rows: {rows}\t"
                               f"Columns: {cols}\t"
                               f"Ai Agent VS. Player = ({score_value[0]}, {score_value[1]})",
                          font=(font_style, 14),
                          bg="#34495e", fg="white")  # Change label background and text color
    game_label.pack(padx=20, pady=20)

    # Button to exit the game
    exit_game_button = tk.Button(game_window, text="Exit Game", command=exit_game, bg=button_color, fg=text_color,
                                 font=(font_style, 16, "bold"), relief=tk.GROOVE)
    exit_game_button.pack(pady=10)


def select_option(option):
    """
       Select an Ai agent method for the game that to be played.

       :param option: The selected option.
       :type option: str
   """
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

display_minimax_tree = False
tree_display_checkbox = tk.Checkbutton(
    bottom_frame, text="Display Minimax Tree", command=toggle_minimax_tree_display,
    bg=button_color, fg=text_color, font=(font_style, 22)
)
tree_display_checkbox.pack(pady=10)

start_button = tk.Button(bottom_frame, text="Start Game", command=start_game, bg=button_color, fg=text_color,
                         font=(font_style, 28, "bold"), relief=tk.GROOVE)
start_button.pack(pady=30)

exit_button = tk.Button(bottom_frame, text="Exit Game", command=exit_game, bg=button_color, fg=text_color,
                        font=(font_style, 28, "bold"), relief=tk.GROOVE)
exit_button.pack(pady=10)

root.attributes('-fullscreen', True)
root.mainloop()
