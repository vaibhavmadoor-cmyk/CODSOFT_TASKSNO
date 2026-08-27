# CodSoft AI Internship - Task 2
# Tic-Tac-Toe AI using Minimax


def print_board(board):
    print()
    print("-------------")

    for i in range(3):
        print(
            "| " + board[i][0] + " | " +
            board[i][1] + " | " +
            board[i][2] + " |"
        )
        print("-------------")

    print()


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def minimax(board, depth, is_maximizing):
    # AI wins
    if check_winner(board, "O"):
        return 10 - depth

    # Human wins
    if check_winner(board, "X"):
        return depth - 10

    # Draw
    if board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"

                    score = minimax(board, depth + 1, False)

                    board[row][col] = " "

                    best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"

                    score = minimax(board, depth + 1, True)

                    board[row][col] = " "

                    best_score = min(best_score, score)

        return best_score


def best_move(board):
    best_score = -float("inf")
    move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"

                score = minimax(board, 0, False)

                board[row][col] = " "

                if score > best_score:
                    best_score = score
                    move = (row, col)

    return move


def play_game():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print("\n================================")
    print("       TIC-TAC-TOE AI")
    print("================================")
    print("You are X")
    print("Computer is O")
    print("Enter row and column numbers from 1 to 3.")

    while True:
        print_board(board)

        # Human move
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("Please enter numbers between 1 and 3.")
                continue

            if board[row][col] != " ":
                print("That position is already occupied.")
                continue

            board[row][col] = "X"

        except ValueError:
            print("Please enter numbers only.")
            continue

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 You win!")
            break

        if board_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # AI move
        print("Computer is thinking...")

        move = best_move(board)

        if move:
            board[move[0]][move[1]] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("🤖 Computer wins!")
            break

        if board_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break


while True:
    play_game()

    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break