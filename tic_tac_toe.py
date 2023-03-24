import tkinter as tk

game_dico = {
    "player": 'X',
    "game": True,
    "board": [" "]*9,
    "buttonList": []
}

WINCOND = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


def swap_player(game_dico, index):
    if check_position(game_dico, index):
        game_dico["board"][index] = game_dico["player"]
        game_dico["buttonList"][index].config(text=game_dico["player"])
        if game_dico["player"] == "O":
            game_dico["player"] = "X"
        else:
            game_dico["player"] = "O"


def win_condition(game_dico):
    for i in WINCOND:
        if game_dico["board"][i[0]] == game_dico["board"][i[1]] == game_dico["board"][i[2]] != " ":
            return game_dico["board"][i[0]]
    return None


def check_position(game_dico, index):
    return game_dico["board"][index] == " "


def reset_game(game_dico, game_label):
    game_dico["player"] = "X"
    game_dico["game"] = True
    game_dico["board"] = [" "]*9
    game_label.config(text="Player X turn")
    for button in game_dico["buttonList"]:
        button.config(text=" ")


def button_click(game_dico, game_label, index):
    if game_dico["game"]:
        if check_position(game_dico, index):
            swap_player(game_dico, index)
            winner = win_condition(game_dico)
            text_player = game_dico["player"]
            if winner:
                game_label.config(text=f"Player {winner} wins!")
                game_dico["game"] = False
            elif " " not in game_dico["board"]:
                game_label.config(text="Draw!")
                game_dico["game"] = False
            else:
                game_label.config(text=f"Player {text_player} turn")


window = tk.Tk()
window.title("Tic Tac Toe")


for i in range(9):
    button = tk.Button(window, text=" ", width=10, height=5,
                       command=lambda index=i: button_click(game_dico, game_label, index))
    button.grid(row=i//3, column=i % 3)
    game_dico["buttonList"].append(button)

label_player = game_dico["player"]
game_label = tk.Label(window, text=f"Player {label_player} turn")
game_label.grid(row=3, column=0, columnspan=2)

reset_button = tk.Button(window, text="Reset",
                         command=lambda: reset_game(game_dico, game_label))
reset_button.grid(row=3, column=2)


window.mainloop()
