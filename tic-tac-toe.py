player = "O"
game = True
board = [" "]*9
turn = 0
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


def printBoard(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print("---|---|---")
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print("---|---|---")
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def tic_tac_toe(board):
    global player
    golemTier = 0
    while True:  
        try:
            userinput = input("entrer votre position :")
            if check_position(board, int(userinput)):
                board[int(userinput) - 1] = player
                break
            else:
                if golemTier > 0:
                    print("change de case !!!")
                else:
                    print("La case est deja prise")
                    golemTier += 1
        except KeyboardInterrupt:
            print("\nReviens quand tu veut")
            exit()
        except:
            golemTier += 1
            print("c'est pas un nombre")


def swap_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def check_position(array, p):
    if array[p-1] == " ":
        return True
    return False


def checkwin(board):
    for i in WINCOND:
        if board[i[0]]==board[i[1]]==board[i[2]]!=' ':
            return board[i[0]]
    return None


def checkdraw(board):
    return ' ' not in board


while game:
    if checkwin(board):
        print(f'Player {checkwin(board)} Wins!')
        break
    if checkdraw(board):
        print('Draw!')
        break
    tic_tac_toe(board)
    printBoard(board)
    swap_player()