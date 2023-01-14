from math import inf
import sys
import random
import copy

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self, name, position):
        self.name = name
        self.row = position[0]
        self.col = position[1]

#############################################################################
######## Board
#############################################################################
def convertToLetter(coord):
    r = coord[0]
    c = coord[1]
    return (chr(97+c), r)

class Board:
    def __init__(self, rows, cols, grid):
        self.rows = rows
        self.cols = cols
        self.grid = grid
        self.pieces = []
        
    def addPiecesToBoard(self, pieces):
        for key, value in pieces.items():
            piece = Piece(value, key)
            self.pieces.append(piece)
            row = piece.row
            col = piece.col
            self.grid[row][col] = -2 #enemy piece is -2 as it should be distinguished from an obstacle
    
    
    def solution(self):
        soln = dict()
        for p in self.pieces:
            coord = convertToLetter((p.row, p.col))
            soln[coord] = p.name
        return soln

    def countThreatenedPieces(self, i=None):
        count = 0
        candidate = None
        if i != None:
            candidate = self.pieces[i]
            self.grid[candidate.row][candidate.col] = 0
            del self.pieces[i]
        for piece in self.pieces:
            name = piece.name
            r = piece.row
            c = piece.col
            if name == "King":
                if r-1 >= 0: #N
                    if self.grid[r-1][c] == -2:
                        count += 1
                
                if r-1 >= 0 and c+1 < self.cols: #NE
                    if self.grid[r-1][c+1] == -2:
                        count += 1
                    
                if c+1 < self.cols: #E
                    if self.grid[r][c+1] == -2:
                        count += 1
                
                if r+1 < self.rows and c+1 < self.cols: #SE
                    if self.grid[r+1][c+1] == -2:
                        count += 1
                
                if r+1 < self.rows: #S
                    if self.grid[r+1][c] == -2:
                        count += 1
                    
                if r+1 < self.rows and c-1 >= 0: #SW
                    if self.grid[r+1][c-1] == -2:
                        count += 1
                    
                if c-1 >= 0: #W
                    if self.grid[r][c-1] == -2:
                        count += 1
                    
                if r-1 >= 0 and c-1 >= 0: #NW
                    if self.grid[r-1][c-1] == -2:
                        count += 1
            
            elif name == "Rook":
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
            
            elif name == "Bishop":
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    
            elif name == "Queen":
                ### ROOK PORTION ###
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col
                    
                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                ### BISHOP PORTION ###
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
            
            elif name == "Knight":
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] == -2:
                        count += 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] == -2:
                        count += 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] == -2:
                        count += 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] == -2:
                        count += 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] == -2:
                        count += 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] == -2:
                        count += 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] == -2:
                        count += 1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] == -2:
                        count += 1
            
            elif name == "Ferz":
                if r-1 >= 0 and c+1 < self.cols: #NE
                    if self.grid[r-1][c+1] == -2:
                        count += 1
                    
                if r+1 < self.rows and c+1 < self.cols: #SE
                    if self.grid[r+1][c+1] == -2:
                        count += 1
                    
                if r+1 < self.rows and c-1 >= 0: #SW
                    if self.grid[r+1][c-1] == -2:
                        count += 1
                    
                if r-1 >= 0 and c-1 >= 0: #NW
                    if self.grid[r-1][c-1] == -2:
                        count += 1
                    
            elif name == "Princess":
                ### KNIGHT PORTION ###
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] == -2:
                        count += 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] == -2:
                        count += 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] == -2:
                        count += 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] == -2:
                        count += 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] == -2:
                        count += 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] == -2:
                        count += 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] == -2:
                        count += 1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] == -2:
                        count += 1
                ### BISHOP PORTION ###
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    
            elif name == "Empress":
                ### KNIGHT PORTION ###
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] == -2:
                        count += 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] == -2:
                        count += 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] == -2:
                        count += 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] == -2:
                        count += 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] == -2:
                        count += 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] == -2:
                        count += 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] == -2:
                        count += 1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] == -2:
                        count += 1

                ### ROOK PORTION ###
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1
                    r = piece.row
                    c = piece.col
                    
                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        if self.grid[r][c] == -2:
                            count += 1

        if i != None:
            self.pieces.insert(i, candidate)
            self.grid[candidate.row][candidate.col] = -2
        
        return count


#############################################################################
######## State
#############################################################################

class State:
    pass

#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, pieces, k):
    originalBoard = Board(rows, cols, grid)
    originalBoard.addPiecesToBoard(pieces) #board now at initial state
    total = len(originalBoard.pieces)
    while True:
        remaining = total - 1
        workingBoard = copy.deepcopy(originalBoard)
        start = random.randint(0, len(workingBoard.pieces)-1) #random restart
        candidate = workingBoard.pieces[start] 
        workingBoard.grid[candidate.row][candidate.col] = 0
        del workingBoard.pieces[start]
        while remaining > int(k):
            min = inf
            neighbour_idx = None
            curr = workingBoard.countThreatenedPieces()
            for i in range(len(workingBoard.pieces)):
                h_value = workingBoard.countThreatenedPieces(i)
                if h_value <= min:
                    min = h_value
                    neighbour_idx = i
            if min >= curr:
                break
            else:
                neighbour_piece = workingBoard.pieces[neighbour_idx]
                workingBoard.grid[neighbour_piece.row][neighbour_piece.col] = 0
                workingBoard.pieces.remove(neighbour_piece)
                remaining -= 1
        if workingBoard.countThreatenedPieces() == 0:
            return workingBoard.solution()

#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline()))
    cols = int(get_par(handle.readline()))
    grid = [[0 for j in range(cols)] for i in range(rows)]
    k = 0
    pieces = {}

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()
    
    k = handle.readline().split(":")[1].strip() # Read in value of k

    piece_nums = get_par(handle.readline()).split()
    num_pieces = 0
    for num in piece_nums:
        num_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        pieces[coords] = piece    

    return rows, cols, grid, pieces, k

def add_piece( comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]

#Returns row and col index in integers respectively
def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: Goal State which is a dictionary containing a mapping of the position of the grid to the chess piece type.
# Chess Pieces (String): King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Goal State to return example: {('a', 0) : Queen, ('d', 10) : Knight, ('g', 25) : Rook}
def run_local():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    rows, cols, grid, pieces, k = parse(testcase)
    goalstate = search(rows, cols, grid, pieces, k)
    return goalstate #Format to be returned
