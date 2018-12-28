OPPOSITE = {"X": "O", "O": "X"}
INDEXDICT = {'a1': 0, 'a2': 1, 'a3': 2, 'b1': 3, 'b2': 4, 'b3': 5, 'c1': 6, 'c2': 7, 'c3': 8}
TRIADS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

class Board:
    def __init__(self):
        self.reset()

    def print(self):
        print(f'\n   |   |   \n {self.board[0]} | {self.board[1]} | {self.board[2]} \n___|___|___' +
              f'\n   |   |   \n {self.board[3]} | {self.board[4]} | {self.board[5]} \n___|___|___' +
              f'\n   |   |   \n {self.board[6]} | {self.board[7]} | {self.board[8]} \n   |   |   ')

    def printPositions(self):
        print('\n    |    |    \n A1 | A2 | A3 \n____|____|____' +
              '\n    |    |    \n B1 | B2 | B3 \n____|____|____' +
              '\n    |    |    \n C1 | C2 | C3 \n    |    |    ')

    def unused(self, pos):
        return self.board[pos] == " "

    def playMove(self, pos, value):
        self.board[pos] = value

    def reset(self):
        self.board = [" " for i in range(9)]

class SmartBoard(Board):
    def playMove(self, pos, value):
        Board.playMove(self, pos, value)
        if " " not in self.board:
            self.winner = "Tie"
        self.proximateCount[pos]["X"] -= 10 # discount squares which have already been used

        for t in TRIADS:
            if pos in t:
                same, opp = (0,0)
                for i in t:
                    if self.board[i] == value:
                        same += 1
                    elif self.board[i] == OPPOSITE[value]:
                        opp += 1
                if same == 3:
                    self.winner = value
                elif value == "O" and same == 2 and opp == 0:
                    self.possibleLosses.append(t)
                elif opp == 0:
                    for i in t:
                        self.proximateCount[i][value] += 1
                else:
                    if t in self.possibleWins:
                        self.possibleWins.remove(t)
                    for i in t:
                        self.proximateCount[i][OPPOSITE[value]] -= 1

    def bestMove(self):
        proximateScores = [0 for i in range(9)]
        for pos in range(9):
            proximateScores[pos] += self.proximateCount[pos]["X"]
            if self.unused(pos):
                if self.proximateCount[pos]["X"] >= 2:
                    return pos
                for t in self.possibleWins:
                    if pos in t:
                        for i in t:
                            if i != pos and self.unused(i):
                                proximateScores[pos] += self.proximateCount[i]["X"] - self.proximateCount[i]["O"]
        if self.possibleLosses:
            for i in self.possibleLosses[0]:
                if self.unused(i):
                    self.possibleLosses.clear()
                    return i
        return proximateScores.index(max(proximateScores))

    def reset(self):
        Board.reset(self)
        self.winner = ""
        self.proximateCount = [{"X": 0, "O": 0} for i in range(9)]
        self.possibleWins = TRIADS.copy()
        self.possibleLosses = []

class Game:
    def __init__(self):
        self.board = SmartBoard()
        self.Xturn = True

    def playRound(self):
        Xturn = input("\nWould you like to go first (y/n): ").lower() not in ('yes', 'y')
        while True:
            if Xturn:
                print("\nMy turn")
                self.board.playMove(self.board.bestMove(), 'X')
            else:
                choice = input("\nYour turn\nWhere would you like to go: ").lower()
                while not (choice in INDEXDICT and self.board.unused(INDEXDICT[choice])):
                    choice = input("\nPlease select another position: ").lower()
                self.board.playMove(INDEXDICT[choice], 'O')
            self.board.print()

            if self.board.winner:
                print("\nIt's a tie!" if self.board.winner == "Tie" else f'\n{self.board.winner} wins!')
                break
            Xturn = not Xturn

    def play(self):
        print('\nWelcome to Tic Tac Toe!\nHere are the positions')
        self.board.printPositions()
        while True:
            self.playRound()
            if input('Would you like to play again (y/n): ').lower() not in ('yes', 'y'):
                break
            else:
                self.board.reset()

if __name__ == '__main__':
    game = Game()
    game.play()