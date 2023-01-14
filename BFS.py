import sys
from collections import deque

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
class Board:
    def __init__(self, rows, cols, grid):
        self.rows = rows
        self.cols = cols
        self.grid = grid
        self.pieces = []
        
    def addPiecesToBoard(self, enemy_pieces):
        for p in enemy_pieces:
            piece = Piece(p[0], p[1])
            self.pieces.append(piece)
            row = piece.row
            col = piece.col
            self.grid[row][col] = -1 #enemy pos share same value as obstacles since our king cannot travel there
    
    def markThreatenedPos(self):
        for piece in self.pieces:
            name = piece.name
            r = piece.row
            c = piece.col
            if name == "King":
                if r-1 >= 0 and self.grid[r-1][c] >= 0: #N
                    self.grid[r-1][c] = -5
                
                if r-1 >= 0 and c+1 < self.cols and self.grid[r-1][c+1] >= 0: #NE
                    self.grid[r-1][c+1] = -5
                    
                if c+1 < self.cols and self.grid[r][c+1] >= 0: #E
                    self.grid[r][c+1] = -5
                
                if r+1 < self.rows and c+1 < self.cols and self.grid[r+1][c+1] >= 0: #SE
                    self.grid[r+1][c+1] = -5
                
                if r+1 < self.rows and self.grid[r+1][c] >= 0: #S
                    self.grid[r+1][c] = -5
                    
                if r+1 < self.rows and c-1 >= 0 and self.grid[r+1][c-1] >= 0: #SW
                    self.grid[r+1][c-1] = -5
                    
                if c-1 >= 0 and self.grid[r][c-1] >= 0: #W
                    self.grid[r][c-1] = -5
                    
                if r-1 >= 0 and c-1 >= 0 and self.grid[r-1][c-1] >= 0: #NW
                    self.grid[r-1][c-1] = -5
            
            elif name == "Rook":
                if r > 0: #up
                    r = piece.row
                    c = piece.col
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                        
                if r < self.rows - 1: #down
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if c > 0: #left
                    r = piece.row
                    c = piece.col
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if c < self.cols - 1:
                    r = piece.row
                    c = piece.col
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
            
            elif name == "Bishop":
                if r > 0 and c < self.cols - 1: #NE
                    r = piece.row
                    c = piece.col
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5 
                       
                if r < self.rows - 1 and c > 0: #SW
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5
                       
                if r > 0 and c > 0:
                    r = piece.row
                    c = piece.col
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5
                    
            elif name == "Queen":
                ### ROOK PORTION ###
                if r > 0: #up
                    r = piece.row
                    c = piece.col
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                        
                if r < self.rows - 1: #down
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if c > 0: #left
                    r = piece.row
                    c = piece.col
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if c < self.cols - 1:
                    r = piece.row
                    c = piece.col
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                        
                ### BISHOP PORTION ###
                if r > 0 and c < self.cols - 1: #NE
                    r = piece.row
                    c = piece.col
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5 
                       
                if r < self.rows - 1 and c > 0: #SW
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5
                       
                if r > 0 and c > 0:
                    r = piece.row
                    c = piece.col
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5
            
            elif name == "Knight":
                if r-2 >= 0 and c+1 < self.cols and self.grid[r-2][c+1] >= 0:
                    self.grid[r-2][c+1] = -5
                    
                if r-1 >= 0 and c+2 < self.cols and self.grid[r-1][c+2] >= 0:
                    self.grid[r-1][c+2] = -5
                    
                if r+1 < self.rows and c+2 < self.cols and self.grid[r+1][c+2] >= 0:
                    self.grid[r+1][c+2] = -5
                    
                if r+2 < self.rows and c+1 < self.cols and self.grid[r+2][c+1] >= 0:
                    self.grid[r+2][c+1] = -5
                    
                if r+2 < self.rows and c-1 >= 0 and self.grid[r+2][c-1] >= 0:
                    self.grid[r+2][c-1] = -5
                    
                if r+1 < self.rows and c-2 >= 0 and self.grid[r+1][c-2] >= 0:
                    self.grid[r+1][c-2] = -5
                    
                if r-1 >= 0 and c-2 >= 0 and self.grid[r-1][c-2] >= 0:
                    self.grid[r-1][c-2] = -5
                    
                if r-2 >= 0 and c-1 >= 0 and self.grid[r-2][c-1] >= 0:
                    self.grid[r-2][c-1] = -5
            
            elif name == "Ferz":
                if r-1 >= 0 and c+1 < self.cols and self.grid[r-1][c+1] >= 0: #NE
                    self.grid[r-1][c+1] = -5
                    
                if r+1 < self.rows and c+1 < self.cols and self.grid[r+1][c+1] >= 0: #SE
                    self.grid[r+1][c+1] = -5
                    
                if r+1 < self.rows and c-1 >= 0 and self.grid[r+1][c-1] >= 0: #SW
                    self.grid[r+1][c-1] = -5
                    
                if r-1 >= 0 and c-1 >= 0 and self.grid[r-1][c-1] >= 0: #NW
                    self.grid[r-1][c-1] = -5
                    
            elif name == "Princess":
                ### BISHOP PORTION ###
                if r > 0 and c < self.cols - 1: #NE
                    r = piece.row
                    c = piece.col
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5 
                       
                if r < self.rows - 1 and c > 0: #SW
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5
                       
                if r > 0 and c > 0:
                    r = piece.row
                    c = piece.col
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1:
                           break
                        self.grid[r][c] = -5
                
                ### KNIGHT PORTION ###
                if r-2 >= 0 and c+1 < self.cols and self.grid[r-2][c+1] >= 0:
                    self.grid[r-2][c+1] = -5
                    
                if r-1 >= 0 and c+2 < self.cols and self.grid[r-1][c+2] >= 0:
                    self.grid[r-1][c+2] = -5
                    
                if r+1 < self.rows and c+2 < self.cols and self.grid[r+1][c+2] >= 0:
                    self.grid[r+1][c+2] = -5
                    
                if r+2 < self.rows and c+1 < self.cols and self.grid[r+2][c+1] >= 0:
                    self.grid[r+2][c+1] = -5
                    
                if r+2 < self.rows and c-1 >= 0 and self.grid[r+2][c-1] >= 0:
                    self.grid[r+2][c-1] = -5
                    
                if r+1 < self.rows and c-2 >= 0 and self.grid[r+1][c-2] >= 0:
                    self.grid[r+1][c-2] = -5
                    
                if r-1 >= 0 and c-2 >= 0 and self.grid[r-1][c-2] >= 0:
                    self.grid[r-1][c-2] = -5
                    
                if r-2 >= 0 and c-1 >= 0 and self.grid[r-2][c-1] >= 0:
                    self.grid[r-2][c-1] = -5
                    
            elif name == "Empress":
                ### ROOK PORTION ###
                if r > 0: #up
                    r = piece.row
                    c = piece.col
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                        
                if r < self.rows - 1: #down
                    r = piece.row
                    c = piece.col
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if c > 0: #left
                    r = piece.row
                    c = piece.col
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                
                if c < self.cols - 1:
                    r = piece.row
                    c = piece.col
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1:
                            break
                        self.grid[r][c] = -5
                        
                ### KNIGHT PORTION ###
                if r-2 >= 0 and c+1 < self.cols and self.grid[r-2][c+1] >= 0:
                    self.grid[r-2][c+1] = -5
                    
                if r-1 >= 0 and c+2 < self.cols and self.grid[r-1][c+2] >= 0:
                    self.grid[r-1][c+2] = -5
                    
                if r+1 < self.rows and c+2 < self.cols and self.grid[r+1][c+2] >= 0:
                    self.grid[r+1][c+2] = -5
                    
                if r+2 < self.rows and c+1 < self.cols and self.grid[r+2][c+1] >= 0:
                    self.grid[r+2][c+1] = -5
                    
                if r+2 < self.rows and c-1 >= 0 and self.grid[r+2][c-1] >= 0:
                    self.grid[r+2][c-1] = -5
                    
                if r+1 < self.rows and c-2 >= 0 and self.grid[r+1][c-2] >= 0:
                    self.grid[r+1][c-2] = -5
                    
                if r-1 >= 0 and c-2 >= 0 and self.grid[r-1][c-2] >= 0:
                    self.grid[r-1][c-2] = -5
                    
                if r-2 >= 0 and c-1 >= 0 and self.grid[r-2][c-1] >= 0:
                    self.grid[r-2][c-1] = -5

#############################################################################
######## State
#############################################################################
def convertToLetter(coord):
    r = coord[0]
    c = coord[1]
    return (chr(97+c), r)

class State:
    def __init__(self, position, prev):
        self.position = position
        self.prev = prev
    

    def getPath(self):
        curr = self
        path = []
        while(curr.prev != None):
            move = []
            move.append(convertToLetter(curr.prev.position))
            move.append(convertToLetter(curr.position))
            path.append(move)
            curr = curr.prev
        path.reverse()
        return path
    
    def isGoal(self, goals):
        for i in range(len(goals)):
            if self.position == goals[i]:
                return True
        return False
    
    def getLegalMoves(self, rows, cols, grid):
        moves = []
        r = self.position[0]
        c = self.position[1]
        if r-1 >= 0 and grid[r-1][c] >= 0: #N
            moves.append((r-1, c))
        
        if r-1 >= 0 and c+1 < cols and grid[r-1][c+1] >= 0: #NE
            moves.append((r-1, c+1))
                    
        if c+1 < cols and grid[r][c+1] >= 0: #E
            moves.append((r, c+1))
                
        if r+1 < rows and c+1 < cols and grid[r+1][c+1] >= 0: #SE
            moves.append((r+1, c+1))
                
        if r+1 < rows and grid[r+1][c] >= 0: #S
            moves.append((r+1, c))
                    
        if r+1 < rows and c-1 >= 0 and grid[r+1][c-1] >= 0: #SW
            moves.append((r+1, c-1))
                    
        if c-1 >= 0 and grid[r][c-1] >= 0: #W
            moves.append((r, c-1))
                    
        if r-1 >= 0 and c-1 >= 0 and grid[r-1][c-1] >= 0: #NW
            moves.append((r-1, c-1))
        return moves
        
#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, enemy_pieces, own_pieces, goals):
    board = Board(rows, cols, grid)
    board.addPiecesToBoard(enemy_pieces)
    board.markThreatenedPos()
    q = deque()
    reached = {}
    initial = State(own_pieces[0][1], None)
    q.append(initial)
    reached[initial.position] = 0
    while q:
        curr = q.popleft()
        for a in curr.getLegalMoves(rows, cols, board.grid):
            successor = State(a, curr)
            if successor.isGoal(goals):
                ans = successor.getPath()
                return ans #early goal test
            if successor.position not in reached.keys():
                q.append(successor)
                reached[successor.position] = 1 #dummy value
    return []

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
    grid = [[1 for j in range(cols)] for i in range(rows)] # Dictionary, label empty spaces as 1 (Default Step Cost)
    enemy_pieces = [] # List
    own_pieces = [] # List
    goals = [] # List

    handle.readline()  # Ignore number of obstacles
    for ch_coord in get_par(handle.readline()).split():  # Init obstacles
        r, c = from_chess_coord(ch_coord)
        grid[r][c] = -1 # Label Obstacle as -1

    handle.readline()  # Ignore Step Cost header
    line = handle.readline()
    while line.startswith("["):
        line = line[1:-2].split(",")
        r, c = from_chess_coord(line[0])
        grid[r][c] = int(line[1]) if grid[r][c] == 1 else grid[r][c] #Reinitialize step cost for coordinates with different costs
        line = handle.readline()
    
    line = handle.readline() # Read Enemy Position
    while line.startswith("["):
        line = line[1:-2]
        piece = add_piece(line)
        enemy_pieces.append(piece)
        line = handle.readline()

    # Read Own King Position
    line = handle.readline()[1:-2]
    piece = add_piece(line)
    own_pieces.append(piece)

    # Read Goal Positions
    for ch_coord in get_par(handle.readline()).split():
        r, c = from_chess_coord(ch_coord)
        goals.append((r, c))
    
    return rows, cols, grid, enemy_pieces, own_pieces, goals

def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [piece, (r,c)]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

#############################################################################
######## Main function to be called
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# To return: List of moves
# Return Format Example: [[('a', 0), ('a', 1)], [('a', 1), ('c', 3)], [('c', 3), ('d', 5)]]
def run_BFS():    
    testcase = sys.argv[1]
    rows, cols, grid, enemy_pieces, own_pieces, goals = parse(testcase)
    moves = search(rows, cols, grid, enemy_pieces, own_pieces, goals)
    return moves
    