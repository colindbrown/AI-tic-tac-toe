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

class MinimaxTBBoard(Board):
    def detectWinner(self, board):
        for t in TRIADS:
            if board[t[0]] != " " and board[t[0]] == board[t[1]] and board[t[1]] == board[t[2]]:
                return board[t[0]]
        if " " not in board:
            return "Tie"
        return ""

    def playMove(self, pos, value):
        Board.playMove(self, pos, value)
        self.winner = self.detectWinner(self.board)

    def minimax(self, board, Xturn):
        positionScores = [(-20 if Xturn else 20) for i in range(9)]
        for i in range(9):
            if board[i] == " ":
                newBoard = board.copy()
                newBoard[i] = "X" if Xturn else "O"
                winner = self.detectWinner(newBoard)
                if winner == "Tie":
                    return (0,i)
                elif winner:
                    return (10, i) if winner == "X" else (-10,i)
                positionScores[i] = self.minimax(newBoard, not Xturn)[0]
        tiebreakBias = sum(positionScores)/(100)
        for t in TRIADS: # remove bias if "O" has no choice
            if sorted([board[t[0]], board[t[1]], board[t[2]]]) == sorted(["X", "X", " "]):
                tiebreakBias = 0
        if Xturn:
            return (round(max(positionScores),-1), positionScores.index(max(positionScores)))
        else:
            return (min(positionScores) + tiebreakBias, positionScores.index(min(positionScores)))

    def bestMove(self):
        return self.minimax(self.board, True)[1]

    def reset(self):
        Board.reset(self)
        self.winner = ""

class Game:
    def __init__(self):
        self.board = MinimaxTBBoard()

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