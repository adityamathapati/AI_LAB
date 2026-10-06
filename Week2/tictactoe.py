board = [" "] * 10

def draw_board(b):
    print(b[7] + "|" + b[8] + "|" + b[9])
    print("-+-+-")
    print(b[4] + "|" + b[5] + "|" + b[6])
    print("-+-+-")
    print(b[1] + "|" + b[2] + "|" + b[3])

def check_win(b, mark):
    return ((b[7] == mark and b[8] == mark and b[9] == mark) or
            (b[4] == mark and b[5] == mark and b[6] == mark) or
            (b[1] == mark and b[2] == mark and b[3] == mark) or
            (b[7] == mark and b[4] == mark and b[1] == mark) or
            (b[8] == mark and b[5] == mark and b[2] == mark) or
            (b[9] == mark and b[6] == mark and b[3] == mark) or
            (b[7] == mark and b[5] == mark and b[3] == mark) or
            (b[9] == mark and b[5] == mark and b[1] == mark))

turn = "X"
for i in range(9):
    draw_board(board)
    print("Turn for " + turn + ". Move on which space? (1-9)")
    move = int(input())
    
    if board[move] == " ":
        board[move] = turn
        if check_win(board, turn):
            draw_board(board)
            print("Player " + turn + " wins!")
            break
        turn = "O" if turn == "X" else "X"
    else:
        print("Space filled. Move elsewhere.")
