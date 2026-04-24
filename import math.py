import math

# تعريف اللوحة
board = [" " for _ in range(9)]

# طباعة البورد
def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

# التحقق من الفوز
def check_winner(b, player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    for state in win_states:
        if b[state[0]] == b[state[1]] == b[state[2]] == player:
            return True
    return False

# التحقق من التعادل
def is_draw(b):
    return " " not in b

# Minimax + Alpha-Beta
def minimax(b, depth, is_maximizing, alpha, beta):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                eval = minimax(b, depth+1, False, alpha, beta)
                b[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                eval = minimax(b, depth+1, True, alpha, beta)
                b[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# أفضل حركة للكمبيوتر
def best_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    return move

# اللعبة
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, Computer is O")
    
    print_board()

    while True:
        # دور اللاعب
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("Invalid move!")
                continue
        except:
            print("Enter a number between 0 and 8")
            continue

        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("You Win!")
            break
        if is_draw(board):
            print("Draw!")
            break

        # دور الكمبيوتر
        print("Computer is thinking...")
        comp_move = best_move()
        board[comp_move] = "O"
        print_board()

        if check_winner(board, "O"):
            print("Computer Wins!")
            break
        if is_draw(board):
            print("Draw!")
            break

# تشغيل اللعبة
if name == "main":
    play_game()