import tkinter as tk
from tkinter import messagebox

# Main window
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)
window.configure(bg="#1C1C1C")  # dark background

# Game state
xState = [0] * 9
oState = [0] * 9
turn = 1
buttons = []

# Scoreboard
x_score = 0
o_score = 0
draw_score = 0

wins = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

def update_scoreboard():
    score_label.config(
        text=f"X: {x_score}    O: {o_score}    Draw: {draw_score}"
    )

def check_win():
    global x_score, o_score, draw_score
    for win in wins:
        if xState[win[0]] + xState[win[1]] + xState[win[2]] == 3:
            x_score += 1
            update_scoreboard()
            messagebox.showinfo("Game Over", "🎉 X Wins!")
            reset_game()
            return
        if oState[win[0]] + oState[win[1]] + oState[win[2]] == 3:
            o_score += 1
            update_scoreboard()
            messagebox.showinfo("Game Over", "🎉 O Wins!")
            reset_game()
            return
    if sum(xState) + sum(oState) == 9:
        draw_score += 1
        update_scoreboard()
        messagebox.showinfo("Game Over", "😐 Match Draw!")
        reset_game()

def on_button_click(index):
    global turn
    if xState[index] or oState[index]:
        return
    if turn == 1:
        xState[index] = 1
        buttons[index].config(text="X", fg="#1E90FF")  # blue X
    else:
        oState[index] = 1
        buttons[index].config(text="O", fg="#FF4500")  # orange O
    check_win()
    turn = 1 - turn

def reset_game():
    global xState, oState, turn
    xState = [0] * 9
    oState = [0] * 9
    turn = 1
    for btn in buttons:
        btn.config(text="", fg="black")

def reset_score():
    global x_score, o_score, draw_score
    x_score = 0
    o_score = 0
    draw_score = 0
    update_scoreboard()
    reset_game()

# Scoreboard
score_label = tk.Label(
    window,
    text="X: 0    O: 0    Draw: 0",
    font=("Arial", 16, "bold"),
    bg="#1C1C1C",
    fg="white"
)
score_label.pack(pady=10)

# Board frame
board_frame = tk.Frame(window, bg="#1C1C1C")
board_frame.pack(padx=20, pady=20)

# Buttons with grid lines style
for i in range(9):
    btn = tk.Button(
        board_frame,
        text="",
        font=("Arial", 36, "bold"),
        width=4,
        height=2,
        bg="#F0F0F0",
        activebackground="#D3D3D3",
        relief="ridge",
        bd=4,
        command=lambda i=i: on_button_click(i)
    )
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Control buttons frame
control_frame = tk.Frame(window, bg="#1C1C1C")
control_frame.pack(pady=10)

restart_btn = tk.Button(control_frame, text="Restart Game", font=("Arial", 12), width=12, command=reset_game)
restart_btn.grid(row=0, column=0, padx=5)

reset_score_btn = tk.Button(control_frame, text="Reset Score", font=("Arial", 12), width=12, command=reset_score)
reset_score_btn.grid(row=0, column=1, padx=5)

quit_btn = tk.Button(control_frame, text="Quit", font=("Arial", 12), width=12, command=window.destroy)
quit_btn.grid(row=0, column=2, padx=5)

window.mainloop()
