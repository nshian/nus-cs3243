from cmath import inf
from copy import deepcopy
import sys

### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    pass

#############################################################################
######## Board
#############################################################################
def convertToNumber(coord):
    r = coord[1]
    c = coord[0]
    return (r, ord(c)-97)

def convertToLetter(coord):
    r = coord[0]
    c = coord[1]
    return (chr(97+c), r)

def convertBoard(gameboard):
    board = dict()
    for key, val in gameboard.items():
        board[convertToNumber(key)] = val
    return board

valueOfKing = 900
valueOfQueen = 150
valueOfBishop = 40
valueOfRook = 50
valueOfKnight = 35
valueOfFerz = 15
valueOfPrincess = 60
valueOfEmpress = 70
valueOfPawn = 10

def makeMove(board, move):
    oldPos = move[0]
    newPos = move[1]
    new = deepcopy(board)
    new.board[newPos] = new.board[oldPos]
    del new.board[oldPos]
    if new.board[newPos][0] == "King":
        if new.board[newPos][1] == "White":
            new.playerKing = newPos
        else:
            new.enemyKing = newPos
    return new

class Board:
    def __init__(self, board):
        self.rows = 7
        self.cols = 7
        self.board = board
        self.playerKing = (0,3)
        self.enemyKing = (6,3)
    
    def hasKingChecked(self, moves, isPlayer):
        if isPlayer:
            pos = self.enemyKing
        else:
            pos = self.playerKing
        for move in moves:
            if move[1] == pos:
                return True
        return False
    
    def calcValues(self, isPlayer):
        total = 0
        identity = "White" if isPlayer else "Black"
        for piece in self.board.values():
            if piece[1] == identity:
                if piece[0] == "King":
                    total += valueOfKing
                if piece[0] == "Queen":
                    total += valueOfQueen
                if piece[0] == "Bishop":
                    total += valueOfBishop
                if piece[0] == "Rook":
                    total += valueOfRook
                if piece[0] == "Knight":
                    total += valueOfKnight
                if piece[0] == "Ferz":
                    total += valueOfFerz
                if piece[0] == "Princess":
                    total += valueOfPrincess
                if piece[0] == "Empress":
                    total += valueOfEmpress
                if piece[0] == "Pawn":
                    total += valueOfPawn
        return total

    def generateMovesForPawn(self, pos, isPlayer, target):
        moves = []
        r, c = pos[0], pos[1]
        if isPlayer:
            if r < self.rows-1 and (r+1, c) not in self.board.keys():
                moves.append((pos, (r+1, c)))
            if r < self.rows-1 and c > 0:
                if (r+1, c-1) in self.board.keys() and self.board[(r+1, c-1)][1] == target:
                    moves.append((pos, (r+1, c-1)))
            if r < self.rows-1 and c < self.cols-1:
                if (r+1, c+1) in self.board.keys() and self.board[(r+1, c+1)][1] == target:
                    moves.append((pos, (r+1, c+1)))
        else:
            if r > 0 and (r-1, c) not in self.board.keys():
                moves.append((pos, (r-1, c)))
            if r > 0 and c > 0:
                if (r-1, c-1) in self.board.keys() and self.board[(r-1, c-1)][1] == target:
                    moves.append((pos, (r-1, c-1)))
            if r > 0 and c < self.cols-1:
                if (r-1, c+1) in self.board.keys() and self.board[(r-1, c+1)][1] == target:
                    moves.append((pos, (r-1, c+1)))
        return moves
    
    def generateMovesForKnight(self, pos, target):
        moves = []
        r, c = pos[0], pos[1]
        if r-2 >= 0 and c+1 < self.cols:
            if (r-2, c+1) not in self.board.keys() or self.board[(r-2, c+1)][1] == target:
                moves.append((pos, (r-2, c+1)))
        if r-1 >= 0 and c+2 < self.cols:
            if (r-1, c+2) not in self.board.keys() or self.board[(r-1, c+2)][1] == target:
                moves.append((pos, (r-1, c+2)))
        if r+1 < self.rows and c+2 < self.cols:
            if (r+1, c+2) not in self.board.keys() or self.board[(r+1, c+2)][1] == target:
                moves.append((pos, (r+1, c+2)))
        if r+2 < self.rows and c+1 < self.cols:
            if (r+2, c+1) not in self.board.keys() or self.board[(r+2, c+1)][1] == target:
                moves.append((pos, (r+2, c+1)))
        if r+2 < self.rows and c-1 >= 0:
            if (r+2, c-1) not in self.board.keys() or self.board[(r+2, c-1)][1] == target:
                moves.append((pos, (r+2, c-1)))
        if r+1 < self.rows and c-2 >= 0:
            if (r+1, c-2) not in self.board.keys() or self.board[(r+1, c-2)][1] == target:
                moves.append((pos, (r+1, c-2)))
        if r-1 >= 0 and c-2 >= 0:
            if (r-1, c-2) not in self.board.keys() or self.board[(r-1, c-2)][1] == target:
                moves.append((pos, (r-1, c-2)))
        if r-2 >= 0 and c-1 >= 0:
            if (r-2, c-1) not in self.board.keys() or self.board[(r-2, c-1)][1] == target:
                moves.append((pos, (r-2, c-1)))
        return moves

    def generateMovesForFerz(self, pos, target):
        moves = []
        r, c = pos[0], pos[1]
        if r-1 >= 0 and c+1 < self.cols:
            if (r-1, c+1) not in self.board.keys() or self.board[(r-1, c+1)][1] == target:
                moves.append((pos, (r-1, c+1)))
        if r+1 < self.rows and c+1 < self.cols:
            if (r+1, c+1) not in self.board.keys() or self.board[(r+1, c+1)][1] == target:
                moves.append((pos, (r+1, c+1)))
        if r+1 < self.rows and c-1 >= 0:
            if (r+1, c-1) not in self.board.keys() or self.board[(r+1, c-1)][1] == target:
                moves.append((pos, (r+1, c-1)))
        if r-1 >= 0 and c-1 >= 0:
            if (r-1, c-1) not in self.board.keys() or self.board[(r-1, c-1)][1] == target:
                moves.append((pos, (r-1, c-1)))
        return moves

    def generateMovesForKing(self, pos, target):
        moves = []
        r, c = pos[0], pos[1]
        if r-1 >= 0:
            if (r-1, c) not in self.board.keys() or self.board[(r-1, c)][1] == target:
                moves.append((pos, (r-1, c)))
        if r-1 >= 0 and c+1 < self.cols:
            if (r-1, c+1) not in self.board.keys() or self.board[(r-1, c+1)][1] == target:
                moves.append((pos, (r-1, c+1)))
        if c+1 < self.cols:
            if (r, c+1) not in self.board.keys() or self.board[(r, c+1)][1] == target:
                moves.append((pos, (r, c+1)))
        if r+1 < self.rows and c+1 < self.cols:
            if (r+1, c+1) not in self.board.keys() or self.board[(r+1, c+1)][1] == target:
                moves.append((pos, (r+1, c+1)))
        if r+1 < self.rows:
            if (r+1, c) not in self.board.keys() or self.board[(r+1, c)][1] == target:
                moves.append((pos, (r+1, c)))
        if r+1 < self.rows and c-1 >= 0:
            if (r+1, c-1) not in self.board.keys() or self.board[(r+1, c-1)][1] == target:
                moves.append((pos, (r+1, c-1)))
        if c-1 >= 0:
            if (r, c-1) not in self.board.keys() or self.board[(r, c-1)][1] == target:
                moves.append((pos, (r, c-1)))
        if r-1 >= 0 and c-1 >= 0:
            if (r-1, c-1) not in self.board.keys() or self.board[(r-1, c-1)][1] == target:
                moves.append((pos, (r-1, c-1)))
        return moves

    def generateMovesForBishop(self, pos, target):
        moves = []
        r, c = pos[0], pos[1]
        while r > 0 and c < self.cols - 1:
                r -= 1
                c += 1
                if (r,c) in self.board.keys():
                    if self.board[(r,c)][1] == target:
                        moves.append((pos, (r,c)))
                    break
                else:
                    moves.append((pos, (r,c)))
        r, c = pos[0], pos[1]

        while r < self.rows - 1 and c < self.cols - 1:
            r += 1
            c += 1
            if (r,c) in self.board.keys():
                if self.board[(r,c)][1] == target:
                    moves.append((pos, (r,c)))
                break
            else:
                moves.append((pos, (r,c)))
        r, c = pos[0], pos[1]

        while r < self.rows - 1 and c > 0:
            r += 1
            c -= 1
            if (r,c) in self.board.keys():
                if self.board[(r,c)][1] == target:
                    moves.append((pos, (r,c)))
                break
            else:
                moves.append((pos, (r,c)))
        r, c = pos[0], pos[1]

        while r > 0 and c > 0:
            r -= 1
            c -= 1
            if (r,c) in self.board.keys():
                if self.board[(r,c)][1] == target:
                    moves.append((pos, (r,c)))
                break
            else:
                moves.append((pos, (r,c)))
        return moves

    def generateMovesForRook(self, pos, target):
        moves = []
        r, c = pos[0], pos[1]
        while r > 0:
            r -= 1
            if (r,c) in self.board.keys():
                if self.board[(r,c)][1] == target:
                    moves.append((pos, (r,c)))
                break
            else:
                moves.append((pos, (r,c)))
        r, c = pos[0], pos[1]
                
        while r < self.rows - 1:
            r += 1
            if (r,c) in self.board.keys():
                if self.board[(r,c)][1] == target:
                    moves.append((pos, (r,c)))
                break
            else:
                moves.append((pos, (r,c)))
        r, c = pos[0], pos[1]

        while c > 0:
            c -= 1
            if (r,c) in self.board.keys():
                if self.board[(r,c)][1] == target:
                    moves.append((pos, (r,c)))
                break
            else:
                moves.append((pos, (r,c)))
        r, c = pos[0], pos[1]
                    
        while c < self.cols - 1:
            c += 1
            if (r,c) in self.board.keys():
                if self.board[(r,c)][1] == target:
                    moves.append((pos, (r,c)))
                break
            else:
                moves.append((pos, (r,c)))
        return moves

    def generateMoves(self, isPlayer):
        moves = []
        target = "Black" if isPlayer else "White"
        for pos, piece in self.board.items():
            if piece[1] == ("White" if isPlayer else "Black"):
                if piece[0] == "King":
                    moves.extend(self.generateMovesForKing(pos, target))
                elif piece[0] == "Queen":
                    moves.extend(self.generateMovesForBishop(pos, target))
                    moves.extend(self.generateMovesForRook(pos, target))
                elif piece[0] == "Bishop":
                    moves.extend(self.generateMovesForBishop(pos, target))
                elif piece[0] == "Rook":
                    moves.extend(self.generateMovesForRook(pos, target))
                elif piece[0] == "Knight":
                    moves.extend(self.generateMovesForKnight(pos, target))
                elif piece[0] == "Ferz":
                    moves.extend(self.generateMovesForFerz(pos, target))
                elif piece[0] == "Princess":
                    moves.extend(self.generateMovesForBishop(pos, target))
                    moves.extend(self.generateMovesForKnight(pos, target))
                elif piece[0] == "Empress":
                    moves.extend(self.generateMovesForRook(pos, target))
                    moves.extend(self.generateMovesForKnight(pos, target))
                else:
                    moves.extend(self.generateMovesForPawn(pos, isPlayer, target))
        return moves
    
    def getVal(self):
        playerMoves = self.generateMoves(isPlayer=True)
        enemyMoves = self.generateMoves(isPlayer=False)
        playerVal = self.calcValues(isPlayer=True)
        enemyVal = self.calcValues(isPlayer=False)
        finalVal = playerVal - enemyVal
        if self.hasKingChecked(playerMoves, isPlayer=True):
            finalVal += 80
        if self.hasKingChecked(enemyMoves, isPlayer=False):
            finalVal -= 80
        return finalVal

#############################################################################
######## State
#############################################################################
class State:
    pass

#Implement your minimax with alpha-beta pruning algorithm here.
maxDepth = 2

def ab(gameboard):
    board = Board(convertBoard(gameboard))
    move = getMaxVal(board, -inf, inf, maxDepth)[0]
    return (convertToLetter(move[0]), convertToLetter(move[1]))

def getMaxVal(board, a, b, depth):
    if depth == 0:
        val = board.getVal()
        return None, val
    nextMove = None
    curr = -inf
    for move in board.generateMoves(isPlayer=True):
        next = makeMove(board, move)
        min = getMinVal(next, a, b, depth - 1)[1]
        if min > curr:
            a = max(curr, a)
            nextMove, curr = move, min
        if curr >= b:
            return nextMove, curr
    return nextMove, curr

def getMinVal(board, a, b, depth):
    if depth == 0:
        val = board.getVal()
        return None, val
    nextMove = None
    curr = inf
    for move in board.generateMoves(isPlayer=False):
        next = makeMove(board, move)
        max = getMaxVal(next, a, b, depth - 1)[1]
        if max < curr:
            b = min(curr, b)
            nextMove, curr = move, max
        if curr <= a:
            return nextMove, curr
    return nextMove, curr

#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline())) # Integer
    cols = int(get_par(handle.readline())) # Integer
    gameboard = {}
    
    enemy_piece_nums = get_par(handle.readline()).split()
    num_enemy_pieces = 0 # Read Enemy Pieces Positions
    for num in enemy_piece_nums:
        num_enemy_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_enemy_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "Black")    

    own_piece_nums = get_par(handle.readline()).split()
    num_own_pieces = 0 # Read Own Pieces Positions
    for num in own_piece_nums:
        num_own_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_own_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "White")    

    return rows, cols, gameboard

def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

# You may call this function if you need to set up the board
def setUpBoard():
    config = sys.argv[1]
    rows, cols, gameboard = parse(config)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook, Princess, Empress, Ferz, Pawn (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new ending position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))

def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    move = ab(gameboard)
    return move #Format to be returned (('a', 0), ('b', 3))

