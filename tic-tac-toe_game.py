# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6],  # Diagonal 2
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw(board):
    return all([space != " " for space in board])

# Function to play the game
def play_game():
    # Initialize the board
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get the player's move
        move = input("Choose a position from 1 to 9: ")

        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1

            if board[move] == " ":
                board[move] = current_player

                # Check for a win
                if check_win(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break

                # Check for a draw
                if check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break

                # Switch players
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That position is already taken. Try again.")
        else:
            print("Invalid input. Choose a position from 1 to 9.")

    # Ask if the players want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
