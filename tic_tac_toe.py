class Board:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.winner = ""

    def print(self):
        print('   |   |   \n %s | %s | %s \n___|___|___' % (self.board[0], self.board[1], self.board[2]))
        print('   |   |   \n %s | %s | %s \n___|___|___' % (self.board[3], self.board[4], self.board[5]))
        print('   |   |   \n %s | %s | %s \n   |   |   ' % (self.board[6], self.board[7], self.board[8]))

    def check(self, pos):
        return self.board[pos]

    def set(self, pos, value):
        self.board[pos] = value

        # check for winner
        row = [self.board[pos//3*3], self.board[pos//3*3 + 1], self.board[pos//3*3 + 2]]
        column = [self.board[pos%3], self.board[pos%3 + 3], self.board[pos%3 + 6]]
        if (row[0] == row[1] and row[1] == row[2]):
            self.winner = value
        elif (column[0] == column[1] and column[1] == column[2]):
            self.winner = value
        elif (pos in (0,4,8) and self.board[0] == self.board[4] and self.board[4] == self.board[8]):
            self.winner = value
        elif (pos in (2,4,6) and self.board[2] == self.board[4] and self.board[4] == self.board[6]):
            self.winner = value


if __name__ == '__main__':
    board = Board()
    board.print()
    board.set(2, 'X')
    board.print()
    print(board.winner)
    board.set(5, 'X')
    board.print()
    print(board.winner)
    board.set(8, 'X')
    board.print()
    print(board.winner)