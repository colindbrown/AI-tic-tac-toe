import time

EXAMPLE = True

class Board:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.winner = ""

    def to_str(self):
        return (f'\n   |   |   \n {self.board[0]} | {self.board[1]} | {self.board[2]} \n___|___|___' +
                f'\n   |   |   \n {self.board[3]} | {self.board[4]} | {self.board[5]} \n___|___|___' +
                f'\n   |   |   \n {self.board[6]} | {self.board[7]} | {self.board[8]} \n   |   |   \n')

    def positions(self):
        return ('\n    |    |    \n A1 | A2 | A3 \n____|____|____' +
                '\n    |    |    \n B1 | B2 | B3 \n____|____|____' +
                '\n    |    |    \n C1 | C2 | C3 \n    |    |    \n')

    def check(self, pos):
        return self.board[pos]

    def playMove(self, pos, value):
        self.board[pos] = value

        # check for winner
        row = [self.board[pos//3*3], self.board[pos//3*3 + 1], self.board[pos//3*3 + 2]]
        column = [self.board[pos%3], self.board[pos%3 + 3], self.board[pos%3 + 6]]
        if row[0] == row[1] and row[1] == row[2]:
            self.winner = value
        elif column[0] == column[1] and column[1] == column[2]:
            self.winner = value
        elif pos in (0,4,8) and self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            self.winner = value
        elif pos in (2,4,6) and self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            self.winner = value


class Game:
    def __init__(self):
        self.board = Board()
    
    def delay_print(self, lines):
        for line in lines:
            print(line)
            time.sleep(1)

    def intro(self):
        lines = ['Welcome to Tic Tac Toe!', 'These are the positions. Remember them.', 
            self.board.positions(), 'Are you ready? (y/n)']
        self.delay_print(lines)
        return input().lower() in ('yes', 'y')

    def play(self):
        if self.intro():
            print("Ready to go")
        else:
            print("Stop")

if __name__ == '__main__':
    game = Game()
    game.play()