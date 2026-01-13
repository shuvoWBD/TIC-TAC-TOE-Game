# TIC-TAC-TOE-Game
A desktop Tic Tac Toe application developed using Python’s Tkinter library. It provides a clean, interactive interface with features like:  X/O turn management  Win and draw detection with pop-up alerts  Live scoreboard for X, O, and draws  Restart game, reset score, and quit buttons  Technologies used:  Python 3  Tkinter



Key Features:

1.Two-Player Local Gameplay:
The game supports two players playing on the same system, alternating turns between X and O.

2.Interactive 3×3 Game Board:
The board is built using Tkinter buttons arranged in a 3×3 grid. Each button responds instantly to user clicks.

3.Turn-Based Logic:
The game automatically switches turns after each valid move, ensuring fair gameplay.

4.Win and Draw Detection:
The program checks all possible winning combinations and correctly identifies:

. X win

. O win

. Draw condition when the board is full.

5.Scoreboard System
A live scoreboard tracks:

. Total wins for X

. Total wins for O

. Total draws:
   Scores persist across rounds until manually reset.

6.Visual Feedback:

. X and O are displayed in different colors for better clarity.

. Message pop-ups announce game results immediately.

7.Game and Score Controls:

. Restart Game resets only the board.

. Reset Score clears both the board and scoreboard.

. Quit button safely closes the application.



Technical Architecture:

1.Programming Language and Library:

. Language: Python

. GUI Framework: Tkinter

2.State Management:

. xState and oState arrays track board positions

. Each index represents one cell of the grid

. Binary values are used to simplify win detection

3. Game Logic Layer:

. Predefined wins list stores all winning index combinations

. check_win() evaluates the current game state after every move

4.Event-Driven Architecture:

.Each button click triggers on_button_click()

.Tkinter handles events without blocking the main loop

5.Separation of Responsibilities:

. UI rendering handled by Tkinter widgets

. Game rules and scoring handled by dedicated functions

. Control logic separated from display logic

6.Reset and Lifecycle Management

. reset_game() clears the board while keeping scores

. reset_score() resets both board and scoreboard

. Application lifecycle managed by window.mainloop()

7.User Feedback and Dialog System
Tkinter’s messagebox module is used to notify players of game outcomes without interrupting application flow.
