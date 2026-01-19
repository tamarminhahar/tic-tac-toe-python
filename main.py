import random
class PlayerInfo:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol
        self.is_computer = False

def create_board():
    board = []
    for i in range(9):
        cell={
            "key":i,
            "valid":True,
            "sign": None
        }
        board.append(cell)
    return board
def print_board(board):
    for i in range(9):
        cell = board[i]
        if cell["sign"] is None:
            print(cell["key"], end="   ")
        else:
            print(cell["sign"], end="   ")

        if (i + 1) % 3 == 0:
            print("\n")
def get_random_symbol():
    return random.choice(["X", "O"])
def get_player_info(mode):
    player1=PlayerInfo(None,None)
    player2=PlayerInfo(None,None)

    while True:
        player1.name = input("Player 1 - Enter your name: ").strip()
        if player1.name:
            break
        print("Name cannot be empty. Try again.")

    if mode == "PVC":
        player2.name = "Computer"
        player2.is_computer = True
    else:
        while True:
            player2.name = input("Player 2 - Enter your name: ").strip()
            if player2.name:
                break
            print("Name cannot be empty. Try again.")


    choice = input("Player 1 - Choose symbol [X/O] (press Enter for random): ").strip().upper()

    if choice in ("X", "O"):
        player1.symbol = choice
    else:
        player1.symbol = get_random_symbol()
        print(f"No valid symbol chosen. Randomly selected: {player1.symbol}")

    player2.symbol = "O" if player1.symbol == "X" else "X"
    print(f"{player2.name} gets: {player2.symbol}")
    return player1, player2
def apply_move(board, player, move):
    if move < 0 or move > 8:
        raise Exception("Move out of range")
    if not board[move]["valid"]:
        raise Exception("Cell is occupied")
    board[move]["sign"] = player.symbol
    board[move]["valid"] = False
def get_player_move(board):
    while True:
        try:
            num = input("Enter number of move(0-8): ").strip()
            move = int(num)

            if move < 0 or move > 8:
                print("Invalid move: number must be between 0 and 8.")
                continue

            if not board[move]["valid"]:
                print("Invalid move: this cell is already occupied. Try again.")
                continue
            return move
        except ValueError:
            print("Invalid input: please enter a number (0-8).")
        except Exception:
            print("Unexpected input error. Try again.")
def get_signs(board):
    return [cell["sign"] for cell in board]
def check_winner(board, symbol):
    signs = get_signs(board)
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in winning_lines:
        if signs[a] == symbol and signs[b] == symbol and signs[c] == symbol:
            return True
    return False
def is_tie(board):
    return all(cell["sign"] is not None for cell in board)
def ask_play_again():
    while True:
        ans = input("Play again? (Y/N): ").strip().upper()
        if ans in ("Y", "YES"):
            return True
        if ans in ("N", "NO"):
            return False
        print("Invalid choice. Enter Y or N.")
def get_computer_move(board):
    available = [cell["key"] for cell in board if cell["valid"]]
    move = random.choice(available)
    return move
def select_game_mode():
    while True:
        choice = input("Choose mode: 1) Player vs Player  2) Player vs Computer : ").strip()
        if choice == "1":
            return "PVP"
        if choice == "2":
            return "PVC"
        print("Invalid choice. Enter 1 or 2.")
def play_game():
    board = create_board()
    mode = select_game_mode()
    player1, player2 = get_player_info(mode)
    current_player = player1
    while True:
        print_board(board)
        print(f"{current_player.name}'s turn ({current_player.symbol})")
        try:
          if current_player.is_computer:
              move = get_computer_move(board)
              print(f"Computer chose: {move}")
          else: move = get_player_move(board)
          apply_move(board,current_player, move)
        except Exception as e:
            print(f"Invalid move:{e} Try again.")
            continue
        if check_winner(board, current_player.symbol):
            print_board(board)
            print(f"{current_player.name} wins!")
            break
        if is_tie(board):
            print_board(board)
            print("Game ended with a tie.")
            break
        current_player = player2 if current_player == player1 else player1

if __name__ == '__main__':
    print("Welcome to Tic Tac Toe game")
    while True:
        play_game()
        if not ask_play_again():
            break