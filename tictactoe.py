import random

def game():
    board = [' '] * 9

    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("---------")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("---------")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    rows = [[0, 1, 2], [3, 4, 5],[6, 7, 8]]
    columns = [[0, 3, 6],[1, 4, 7],[2, 5, 8]]
    diagonals = [[0, 4, 8],[2, 4, 6]]

    while True:
        print('Your Turn')
        while True:
            user = int(input('Enter a position (1-9): ')) - 1
            if 0 <= user <= 8 and board[user] == ' ':
                board[user] = 'X'
                break
            else:
                print('Invalid or filled position. Try again.')

        print_board()

        user_wins = False
        for i in rows:
            if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
                user_wins = True
                break
        for i in columns:
            if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
                user_wins = True
                break
        for i in diagonals:
            if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
                user_wins = True
                break
        if user_wins:
            print("You win!")
            break
        if ' ' not in board:
            print("It's a draw!")
            break
        print('Computer Turn')
        while True:
            comp = random.randint(0, 8)
            if board[comp] == ' ':
                board[comp] = 'O'
                break
        print_board()
        computer_wins = False
        for i in rows:
            if board[i[0]] == 'O' and board[i[1]] == 'O' and board[i[2]] == 'O':
                computer_wins = True
                break
        for i in columns:
            if board[i[0]] == 'O' and board[i[1]] == 'O' and board[i[2]] == 'O':
                computer_wins = True
                break
        for i in diagonals:
            if board[i[0]] == 'O' and board[i[1]] == 'O' and board[i[2]] == 'O':
                computer_wins = True
                break
        if computer_wins:
            print("Computer wins!")
            break

        if ' ' not in board:
            print("It's a draw!")
            break

game()
