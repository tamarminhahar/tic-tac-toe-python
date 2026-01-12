from random import random
class player_info:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol

def create_board():
    board = []
    for i in range(3):
        board.append(["?", "?", "?"])
    return board

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="      ")
        print("\n")

def get_player_info():
    player1=player_info(None,None)
    player2=player_info(None,None)
    player1.name=input("Player 1\nEnter your name: ")
    player2.name=input("Player 2\nEnter your name: ")

    player1.symbol=input("Player 1\nEnter your choice[X/O]: ")
    player2.symbol=input("Player 2\nEnter your choice[X/O]: ")
    if player1.symbol is None:
        player1.symbol= get_random_symbol()
    if  player2.symbol is None:
        player2.symbol = get_random_symbol()
    return player2, player1


def get_random_symbol():
    return random.choice(["X", "O"])







if __name__ == '__main__':

    board=create_board()
    print_board(board)
print(get_player_info())