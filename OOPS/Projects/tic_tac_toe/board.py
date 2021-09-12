from player import Player

class Board:
    EMPTY = 0 #Constant variables should be in UPPER Case
    COLUMN = {"A":0, "B":1, "C":2}
    ROW = [0,1,2]

    def __init__(self, game_board=None):
        if game_board:
            self._game_board = game_board
        else:
            self._game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def print_board(self):
        print("    A    B    C")
        for i, row in enumerate(self._game_board, 1):
            print(i, end=" | ")
            for col in row:
                if col != Board.EMPTY:
                    print(col, end="  |  ")
                else:
                    print("  |  ", end="")
            print("\n-----------------")

    def get_row_column(self, move):
        row = int(move[0]) - 1
        column = Board.COLUMN[move[1]]
        return row, column

    def submit_move(self, move, player):
        if self.is_move_valid(move):
            row, column = self.get_row_column(move)
            value_from_board = self._game_board[row][column]
            if value_from_board == Board.EMPTY:
                self._game_board[row][column] = player.marker
            else:
                print("This location is already taken")
                if not player.is_human:
                    print("Computer getting posting in a new location")
                    new_move = player.get_player_move()
                    self.submit_move(new_move, player)
        else:
            print("Please enter a valid position")

    def is_move_valid(self, move):
        if len(move) == 2 and int(move[0]) - 1 in Board.ROW and move[1] in Board.COLUMN.keys():
            return True
        else:
            return False
        
    def is_winner(self, move, player):
        row, column = self.get_row_column(move)
        print("This is for PLayer") if player._is_human else print("This is for Computer")
        print("Column check : ", self.check_col(column, player))
        print("Row check : ", self.check_row(row, player))
        print("Diagonal Check : ", self.check_diagonal(player))
        print("Anti Diagonal check : ", self.check_antidiagonal(player))
        if self.check_col(column, player) or self.check_row(row, player) or self.check_diagonal(player) or self.check_antidiagonal(player):
            return True
        else:
            return False

    def check_col(self, col, player):
        marker = player.marker
        col_item = [item[col] for item in self._game_board]
        for item in col_item:
            if str(item) != marker:
                return False
        return True

    def check_row(self, row, player):
        marker = player.marker
        row_item = self._game_board[row]
        for item in row_item:
            if str(item) != marker:
                return False
        return True

    def check_diagonal(self, player):
        marker = player.marker
        for i in range(0, len(self._game_board)):
            if str(self._game_board[i][i]) != marker:
                return False
        return True

    def check_antidiagonal(self, player):
        marker = player.marker
        board_length = len(self._game_board) - 1
        for i in range(0, len(self._game_board)):
            if str(self._game_board[i][board_length-i]) != marker:
                return False
        return True

    def check_tie(self):
        count = 0
        for item_row in self._game_board:
            if Board.EMPTY not in item_row:
                count += 1
        if count == len(self._game_board):
            value = True
        else:
            value = False
        return value
              

print("*****************")
print("  Tic-Tac-Toe!")
print("*****************")

board = Board()
player = Player()
computer = Player("O", False)
board.print_board()

while True:

    move = player.get_player_move()
    board.submit_move(move, player)
    board.print_board()

    if board.is_winner(move, player):
        print("You win!")
        break

    if board.check_tie():
        print("The Game is a Tie. Please restart!")
        break

    computer_move = computer.get_player_move()
    board.submit_move(computer_move, computer)
    board.print_board()

    if board.is_winner(computer_move, computer):
        print("Computer won!")
        break
