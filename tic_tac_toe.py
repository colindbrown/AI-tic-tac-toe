import time

EXAMPLE = True

class Board:
    def __init__(self):
        self.reset()

    def toStr(self):
        return (f'\n   |   |   \n {self.board[0]} | {self.board[1]} | {self.board[2]} \n___|___|___' +
                f'\n   |   |   \n {self.board[3]} | {self.board[4]} | {self.board[5]} \n___|___|___' +
                f'\n   |   |   \n {self.board[6]} | {self.board[7]} | {self.board[8]} \n   |   |   ')

    def positions(self):
        return ('\n    |    |    \n A1 | A2 | A3 \n____|____|____' +
                '\n    |    |    \n B1 | B2 | B3 \n____|____|____' +
                '\n    |    |    \n C1 | C2 | C3 \n    |    |    ')

    def unused(self, pos):
        return self.board[pos] == " "

    def playMove(self, pos, value):
        self.board[pos] = value
        self.played += 1

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

    def bestMove(self): # to be rewritten
        for i in range(9):
            if self.board[i] == " ":
                return i

    def reset(self):
        self.board = [" " for i in range(9)]
        self.winner = ""
        self.played = 0


class Game:
    def __init__(self):
        self.board = Board()
        self.Xturn = True
    
    def intro(self):
        lines = ['Welcome to Tic Tac Toe!', 'Here are the positions', 
                  self.board.positions(), '\nAre you ready? (y/n)']
        for line in lines:
            print(line)
            time.sleep(1)
        return input().lower() in ('yes', 'y')

    def playerTurn(self):
        moveList = {'a1': 0, 'a2': 1, 'a3': 2, 'b1': 3, 'b2': 4, 'b3': 5, 'c1': 6, 'c2': 7, 'c3': 8}

        print("\nYour turn\nWhere would you like to go?")
        choice = input().lower()
        while not (choice in moveList and self.board.unused(moveList[choice])):
            print("\nPlease select another position")
            choice = input().lower()
        self.board.playMove(moveList[choice], 'O')
        print(self.board.toStr())

    def playRound(self):
        while True:
            if self.Xturn:
                print("\nMy turn")
                self.board.playMove(self.board.bestMove(), 'X')
                print(self.board.toStr())
            else:
                self.playerTurn()

            if self.board.winner:
                print(f'\n{self.board.winner} wins!')
                break
            elif self.board.played == 9:
                print('\nIts a tie!')
                break
            self.Xturn = not self.Xturn

    def play(self):
        if self.intro():
            while True:
                self.playRound()
                print('Would you like to play again?')
                if input().lower() not in ('yes', 'y'):
                    break
                else:
                    self.board.reset()


if __name__ == '__main__':
    game = Game()
    game.play()