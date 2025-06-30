def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-'*5)

def check_win(board, player):
    win_conditions = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)],
    ]
    for condition in win_conditions:
        if all(board[r][c] == player for r,c in condition):
            return True
    return False

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    player = 'X'
    for _ in range(9):
        print_board(board)
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter col (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = player
                if check_win(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    return
                player = 'O' if player == 'X' else 'X'
            else:
                print("Cell occupied! Try again.")
        except:
            print("Invalid input. Try again.")
    print_board(board)
    print("It's a tie!")

tic_tac_toe()
