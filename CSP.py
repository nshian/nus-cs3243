from cmath import inf
import sys

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self, name):
        self.name = name
        if name == "Queen":
            self.degree = 0
        elif name == "Empress":
            self.degree = 1
        elif name == "Princess":
            self.degree = 2
        elif name == "Rook":
            self.degree = 3
        elif name == "Bishop":
            self.degree = 4
        elif name == "Knight":
            self.degree = 5
        elif name == "King":
            self.degree = 6
        elif name == "Ferz":
            self.degree = 7
        self.row = None
        self.col = None
        self.domain = []

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

    def addPieceToBoard(self, piece):
        self.pieces.append(piece)

    def solution(self):
        soln = dict()
        for p in self.pieces:
            coord = convertToLetter((p.row, p.col))
            soln[coord] = p.name
        return soln
    
    def findInitialDomain(self):
        d = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 0:
                    d.append((0, (r,c)))
        return d

    def initialiseDomain(self, domain):
        for i in range(len(self.pieces)):
            self.pieces[i].domain = domain
    
    def isInvalid(self, piece):
        name = piece.name
        r = piece.row
        c = piece.col
        if name == "King":
            if r-1 >= 0: #N
                if self.grid[r-1][c] == -2:
                    return True
            
            if r-1 >= 0 and c+1 < self.cols: #NE
                if self.grid[r-1][c+1] == -2:
                    return True
                
            if c+1 < self.cols: #E
                if self.grid[r][c+1] == -2:
                    return True
            
            if r+1 < self.rows and c+1 < self.cols: #SE
                if self.grid[r+1][c+1] == -2:
                    return True
            
            if r+1 < self.rows: #S
                if self.grid[r+1][c] == -2:
                    return True
                
            if r+1 < self.rows and c-1 >= 0: #SW
                if self.grid[r+1][c-1] == -2:
                    return True
                
            if c-1 >= 0: #W
                if self.grid[r][c-1] == -2:
                    return True
                
            if r-1 >= 0 and c-1 >= 0: #NW
                if self.grid[r-1][c-1] == -2:
                    return True
        
        elif name == "Rook":
            if r > 0: #up
                while r > 0:
                    r -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1: #down
                while r < self.rows - 1:
                    r += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if c > 0: #left
                while c > 0:
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if c < self.cols - 1:
                while c < self.cols - 1:
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
        
        elif name == "Bishop":
            if r > 0 and c < self.cols - 1: #NE
                while r > 0 and c < self.cols - 1:
                    r -= 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1 and c < self.cols - 1: #SE
                while r < self.rows - 1 and c < self.cols - 1:
                    r += 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if r < self.rows - 1 and c > 0: #SW
                while r < self.rows - 1 and c > 0:
                    r += 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if r > 0 and c > 0:
                while r > 0 and c > 0: #NW
                    r -= 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                
        elif name == "Queen":
            ### ROOK PORTION ###
            if r > 0: #up
                while r > 0:
                    r -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1: #down
                while r < self.rows - 1:
                    r += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if c > 0: #left
                while c > 0:
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col
                
            if c < self.cols - 1:
                while c < self.cols - 1:
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
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
                        return True
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1 and c < self.cols - 1: #SE
                while r < self.rows - 1 and c < self.cols - 1:
                    r += 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if r < self.rows - 1 and c > 0: #SW
                while r < self.rows - 1 and c > 0:
                    r += 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if r > 0 and c > 0:
                while r > 0 and c > 0: #NW
                    r -= 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
        
        elif name == "Knight":
            if r-2 >= 0 and c+1 < self.cols:
                if self.grid[r-2][c+1] == -2:
                    return True
                
            if r-1 >= 0 and c+2 < self.cols:
                if self.grid[r-1][c+2] == -2:
                    return True
                
            if r+1 < self.rows and c+2 < self.cols:
                if self.grid[r+1][c+2] == -2:
                    return True
                
            if r+2 < self.rows and c+1 < self.cols:
                if self.grid[r+2][c+1] == -2:
                    return True
                
            if r+2 < self.rows and c-1 >= 0:
                if self.grid[r+2][c-1] == -2:
                    return True
                
            if r+1 < self.rows and c-2 >= 0:
                if self.grid[r+1][c-2] == -2:
                    return True
                
            if r-1 >= 0 and c-2 >= 0:
                if self.grid[r-1][c-2] == -2:
                    return True
                
            if r-2 >= 0 and c-1 >= 0:
                if self.grid[r-2][c-1] == -2:
                    return True
        
        elif name == "Ferz":
            if r-1 >= 0 and c+1 < self.cols: #NE
                if self.grid[r-1][c+1] == -2:
                    return True
                
            if r+1 < self.rows and c+1 < self.cols: #SE
                if self.grid[r+1][c+1] == -2:
                    return True
                
            if r+1 < self.rows and c-1 >= 0: #SW
                if self.grid[r+1][c-1] == -2:
                    return True
                
            if r-1 >= 0 and c-1 >= 0: #NW
                if self.grid[r-1][c-1] == -2:
                    return True
                
        elif name == "Princess":
            ### KNIGHT PORTION ###
            if r-2 >= 0 and c+1 < self.cols:
                if self.grid[r-2][c+1] == -2:
                    return True
                
            if r-1 >= 0 and c+2 < self.cols:
                if self.grid[r-1][c+2] == -2:
                    return True
                
            if r+1 < self.rows and c+2 < self.cols:
                if self.grid[r+1][c+2] == -2:
                    return True
                
            if r+2 < self.rows and c+1 < self.cols:
                if self.grid[r+2][c+1] == -2:
                    return True
                
            if r+2 < self.rows and c-1 >= 0:
                if self.grid[r+2][c-1] == -2:
                    return True
                
            if r+1 < self.rows and c-2 >= 0:
                if self.grid[r+1][c-2] == -2:
                    return True
                
            if r-1 >= 0 and c-2 >= 0:
                if self.grid[r-1][c-2] == -2:
                    return True
                
            if r-2 >= 0 and c-1 >= 0:
                if self.grid[r-2][c-1] == -2:
                    return True
            ### BISHOP PORTION ###
            if r > 0 and c < self.cols - 1: #NE
                while r > 0 and c < self.cols - 1:
                    r -= 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1 and c < self.cols - 1: #SE
                while r < self.rows - 1 and c < self.cols - 1:
                    r += 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if r < self.rows - 1 and c > 0: #SW
                while r < self.rows - 1 and c > 0:
                    r += 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if r > 0 and c > 0:
                while r > 0 and c > 0: #NW
                    r -= 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                
        elif name == "Empress":
            ### KNIGHT PORTION ###
            if r-2 >= 0 and c+1 < self.cols:
                if self.grid[r-2][c+1] == -2:
                    return True
                
            if r-1 >= 0 and c+2 < self.cols:
                if self.grid[r-1][c+2] == -2:
                    return True
                
            if r+1 < self.rows and c+2 < self.cols:
                if self.grid[r+1][c+2] == -2:
                    return True
                
            if r+2 < self.rows and c+1 < self.cols:
                if self.grid[r+2][c+1] == -2:
                    return True
                
            if r+2 < self.rows and c-1 >= 0:
                if self.grid[r+2][c-1] == -2:
                    return True
                
            if r+1 < self.rows and c-2 >= 0:
                if self.grid[r+1][c-2] == -2:
                    return True
                
            if r-1 >= 0 and c-2 >= 0:
                if self.grid[r-1][c-2] == -2:
                    return True
                
            if r-2 >= 0 and c-1 >= 0:
                if self.grid[r-2][c-1] == -2:
                    return True

            ### ROOK PORTION ###
            if r > 0: #up
                while r > 0:
                    r -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1: #down
                while r < self.rows - 1:
                    r += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col

            if c > 0: #left
                while c > 0:
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
                r = piece.row
                c = piece.col
                
            if c < self.cols - 1:
                while c < self.cols - 1:
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == -2:
                        return True
        return False

    def countThreatenedPos(self, piece):
        count = 0
        name = piece.name
        r = piece.row
        c = piece.col
        if name == "King":
            if r-1 >= 0: #N
                if self.grid[r-1][c] == 0:
                    count += 1
            
            if r-1 >= 0 and c+1 < self.cols: #NE
                if self.grid[r-1][c+1] == 0:
                    count += 1
                
            if c+1 < self.cols: #E
                if self.grid[r][c+1] == 0:
                    count += 1
            
            if r+1 < self.rows and c+1 < self.cols: #SE
                if self.grid[r+1][c+1] == 0:
                    count += 1
            
            if r+1 < self.rows: #S
                if self.grid[r+1][c] == 0:
                    count += 1
                
            if r+1 < self.rows and c-1 >= 0: #SW
                if self.grid[r+1][c-1] == 0:
                    count += 1
                
            if c-1 >= 0: #W
                if self.grid[r][c-1] == 0:
                    count += 1
                
            if r-1 >= 0 and c-1 >= 0: #NW
                if self.grid[r-1][c-1] == 0:
                    count += 1
        
        elif name == "Rook":
            if r > 0: #up
                while r > 0:
                    r -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1: #down
                while r < self.rows - 1:
                    r += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if c > 0: #left
                while c > 0:
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if c < self.cols - 1:
                while c < self.cols - 1:
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
        
        elif name == "Bishop":
            if r > 0 and c < self.cols - 1: #NE
                while r > 0 and c < self.cols - 1:
                    r -= 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1 and c < self.cols - 1: #SE
                while r < self.rows - 1 and c < self.cols - 1:
                    r += 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if r < self.rows - 1 and c > 0: #SW
                while r < self.rows - 1 and c > 0:
                    r += 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if r > 0 and c > 0:
                while r > 0 and c > 0: #NW
                    r -= 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                
        elif name == "Queen":
            ### ROOK PORTION ###
            if r > 0: #up
                while r > 0:
                    r -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1: #down
                while r < self.rows - 1:
                    r += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if c > 0: #left
                while c > 0:
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col
                
            if c < self.cols - 1:
                while c < self.cols - 1:
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
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
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1 and c < self.cols - 1: #SE
                while r < self.rows - 1 and c < self.cols - 1:
                    r += 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if r < self.rows - 1 and c > 0: #SW
                while r < self.rows - 1 and c > 0:
                    r += 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if r > 0 and c > 0:
                while r > 0 and c > 0: #NW
                    r -= 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
        
        elif name == "Knight":
            if r-2 >= 0 and c+1 < self.cols:
                if self.grid[r-2][c+1] == 0:
                    count += 1
                
            if r-1 >= 0 and c+2 < self.cols:
                if self.grid[r-1][c+2] == 0:
                    count += 1
                
            if r+1 < self.rows and c+2 < self.cols:
                if self.grid[r+1][c+2] == 0:
                    count += 1
                
            if r+2 < self.rows and c+1 < self.cols:
                if self.grid[r+2][c+1] == 0:
                    count += 1
                
            if r+2 < self.rows and c-1 >= 0:
                if self.grid[r+2][c-1] == 0:
                    count += 1
                
            if r+1 < self.rows and c-2 >= 0:
                if self.grid[r+1][c-2] == 0:
                    count += 1
                
            if r-1 >= 0 and c-2 >= 0:
                if self.grid[r-1][c-2] == 0:
                    count += 1
                
            if r-2 >= 0 and c-1 >= 0:
                if self.grid[r-2][c-1] == 0:
                    count += 1
        
        elif name == "Ferz":
            if r-1 >= 0 and c+1 < self.cols: #NE
                if self.grid[r-1][c+1] == 0:
                    count += 1
                
            if r+1 < self.rows and c+1 < self.cols: #SE
                if self.grid[r+1][c+1] == 0:
                    count += 1
                
            if r+1 < self.rows and c-1 >= 0: #SW
                if self.grid[r+1][c-1] == 0:
                    count += 1
                
            if r-1 >= 0 and c-1 >= 0: #NW
                if self.grid[r-1][c-1] == 0:
                    count += 1
                
        elif name == "Princess":
            ### KNIGHT PORTION ###
            if r-2 >= 0 and c+1 < self.cols:
                if self.grid[r-2][c+1] == 0:
                    count += 1
                
            if r-1 >= 0 and c+2 < self.cols:
                if self.grid[r-1][c+2] == 0:
                    count += 1
                
            if r+1 < self.rows and c+2 < self.cols:
                if self.grid[r+1][c+2] == 0:
                    count += 1
                
            if r+2 < self.rows and c+1 < self.cols:
                if self.grid[r+2][c+1] == 0:
                    count += 1
                
            if r+2 < self.rows and c-1 >= 0:
                if self.grid[r+2][c-1] == 0:
                    count += 1
                
            if r+1 < self.rows and c-2 >= 0:
                if self.grid[r+1][c-2] == 0:
                    count += 1
                
            if r-1 >= 0 and c-2 >= 0:
                if self.grid[r-1][c-2] == 0:
                    count += 1
                
            if r-2 >= 0 and c-1 >= 0:
                if self.grid[r-2][c-1] == 0:
                    count += 1
            ### BISHOP PORTION ###
            if r > 0 and c < self.cols - 1: #NE
                while r > 0 and c < self.cols - 1:
                    r -= 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1 and c < self.cols - 1: #SE
                while r < self.rows - 1 and c < self.cols - 1:
                    r += 1
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if r < self.rows - 1 and c > 0: #SW
                while r < self.rows - 1 and c > 0:
                    r += 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if r > 0 and c > 0:
                while r > 0 and c > 0: #NW
                    r -= 1
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                
        elif name == "Empress":
            ### KNIGHT PORTION ###
            if r-2 >= 0 and c+1 < self.cols:
                if self.grid[r-2][c+1] == 0:
                    count += 1
                
            if r-1 >= 0 and c+2 < self.cols:
                if self.grid[r-1][c+2] == 0:
                    count += 1
                
            if r+1 < self.rows and c+2 < self.cols:
                if self.grid[r+1][c+2] == 0:
                    count += 1
                
            if r+2 < self.rows and c+1 < self.cols:
                if self.grid[r+2][c+1] == 0:
                    count += 1
                
            if r+2 < self.rows and c-1 >= 0:
                if self.grid[r+2][c-1] == 0:
                    count += 1
                
            if r+1 < self.rows and c-2 >= 0:
                if self.grid[r+1][c-2] == 0:
                    count += 1
                
            if r-1 >= 0 and c-2 >= 0:
                if self.grid[r-1][c-2] == 0:
                    count += 1
                
            if r-2 >= 0 and c-1 >= 0:
                if self.grid[r-2][c-1] == 0:
                    count += 1

            ### ROOK PORTION ###
            if r > 0: #up
                while r > 0:
                    r -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col
            
            if r < self.rows - 1: #down
                while r < self.rows - 1:
                    r += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col

            if c > 0: #left
                while c > 0:
                    c -= 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
                r = piece.row
                c = piece.col
                
            if c < self.cols - 1:
                while c < self.cols - 1:
                    c += 1
                    if self.grid[r][c] == -1:
                        break
                    if self.grid[r][c] == 0:
                        count += 1
        return count
    
    def markThreatenedPos(self, var):
        piece = self.pieces[var]
        r = piece.row
        c = piece.col
        name = piece.name
        if r != None and c != None:
            self.grid[r][c] = -2
            if name == "King":
                if r-1 >= 0: #N
                    if self.grid[r-1][c] != -1 and self.grid[r-1][c] != -2:
                        self.grid[r-1][c] += 1
                
                if r-1 >= 0 and c+1 < self.cols: #NE
                    if self.grid[r-1][c+1] != -1 and self.grid[r-1][c+1] != -2:
                        self.grid[r-1][c+1] += 1
                    
                if c+1 < self.cols: #E
                    if self.grid[r][c+1] != -1 and self.grid[r][c+1] != -2:
                        self.grid[r][c+1] += 1
                
                if r+1 < self.rows and c+1 < self.cols: #SE
                    if self.grid[r+1][c+1] != -1 and self.grid[r+1][c+1] != -2:
                        self.grid[r+1][c+1] += 1
                
                if r+1 < self.rows: #S
                    if self.grid[r+1][c] != -1 and self.grid[r+1][c] != -2:
                        self.grid[r+1][c] += 1
                    
                if r+1 < self.rows and c-1 >= 0: #SW
                    if self.grid[r+1][c-1] != -1 and self.grid[r+1][c-1] != -2:
                        self.grid[r+1][c-1] += 1
                    
                if c-1 >= 0: #W
                    if self.grid[r][c-1] != -1 and self.grid[r][c-1] != -2:
                        self.grid[r][c-1] += 1
                    
                if r-1 >= 0 and c-1 >= 0: #NW
                    if self.grid[r-1][c-1] != -1 and self.grid[r-1][c-1] != -2:
                        self.grid[r-1][c-1] += 1
            
            elif name == "Rook":
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
            
            elif name == "Bishop":
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
                    
            elif name == "Queen":
                ### ROOK PORTION ###
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                ### BISHOP PORTION ###
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
            
            elif name == "Knight":
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] != -1 and self.grid[r-2][c+1] != -2:
                        self.grid[r-2][c+1] += 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] != -1 and self.grid[r-1][c+2] != -2:
                        self.grid[r-1][c+2] += 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] != -1 and self.grid[r+1][c+2] != -2:
                        self.grid[r+1][c+2] += 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] != -1 and self.grid[r+2][c+1] != -2:
                        self.grid[r+2][c+1] += 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] != -1 and self.grid[r+2][c-1] != -2:
                        self.grid[r+2][c-1] += 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] != -1 and self.grid[r+1][c-2] != -2:
                        self.grid[r+1][c-2] += 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] != -1 and self.grid[r-1][c-2] != -2:
                        self.grid[r-1][c-2] +=1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] != -1 and self.grid[r-2][c-1] != -2:
                        self.grid[r-2][c-1] += 1
            
            elif name == "Ferz":
                if r-1 >= 0 and c+1 < self.cols: #NE
                    if self.grid[r-1][c+1] != -1 and self.grid[r-1][c+1] != -2:
                        self.grid[r-1][c+1] += 1
                    
                if r+1 < self.rows and c+1 < self.cols: #SE
                    if self.grid[r+1][c+1] != -1 and self.grid[r+1][c+1] != -2:
                        self.grid[r+1][c+1] += 1
                    
                if r+1 < self.rows and c-1 >= 0: #SW
                    if self.grid[r+1][c-1] != -1 and self.grid[r+1][c-1] != -2:
                        self.grid[r+1][c-1] += 1 
                    
                if r-1 >= 0 and c-1 >= 0: #NW
                    if self.grid[r-1][c-1] != -1 and self.grid[r-1][c-1] != -2:
                        self.grid[r-1][c-1] += 1
                    
            elif name == "Princess":
                ### KNIGHT PORTION ###
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] != -1 and self.grid[r-2][c+1] != -2:
                        self.grid[r-2][c+1] += 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] != -1 and self.grid[r-1][c+2] != -2:
                        self.grid[r-1][c+2] += 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] != -1 and self.grid[r+1][c+2] != -2:
                        self.grid[r+1][c+2] += 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] != -1 and self.grid[r+2][c+1] != -2:
                        self.grid[r+2][c+1] += 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] != -1 and self.grid[r+2][c-1] != -2:
                        self.grid[r+2][c-1] += 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] != -1 and self.grid[r+1][c-2] != -2:
                        self.grid[r+1][c-2] += 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] != -1 and self.grid[r-1][c-2] != -2:
                        self.grid[r-1][c-2] +=1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] != -1 and self.grid[r-2][c-1] != -2:
                        self.grid[r-2][c-1] += 1
                ### BISHOP PORTION ###
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
                    
            elif name == "Empress":
                ### KNIGHT PORTION ###
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] != -1 and self.grid[r-2][c+1] != -2:
                        self.grid[r-2][c+1] += 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] != -1 and self.grid[r-1][c+2] != -2:
                        self.grid[r-1][c+2] += 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] != -1 and self.grid[r+1][c+2] != -2:
                        self.grid[r+1][c+2] += 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] != -1 and self.grid[r+2][c+1] != -2:
                        self.grid[r+2][c+1] += 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] != -1 and self.grid[r+2][c-1] != -2:
                        self.grid[r+2][c-1] += 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] != -1 and self.grid[r+1][c-2] != -2:
                        self.grid[r+1][c-2] += 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] != -1 and self.grid[r-1][c-2] != -2:
                        self.grid[r-1][c-2] +=1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] != -1 and self.grid[r-2][c-1] != -2:
                        self.grid[r-2][c-1] += 1

                ### ROOK PORTION ###
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] += 1
                    r = piece.row
                    c = piece.col

    def unmarkThreatenedPos(self, var):
        piece = self.pieces[var]
        r = piece.row
        c = piece.col
        name = piece.name
        if r != None and c != None:
            self.grid[r][c] = 0
            if name == "King":
                if r-1 >= 0: #N
                    if self.grid[r-1][c] != -1 and self.grid[r-1][c] != -2:
                        self.grid[r-1][c] -= 1
                
                if r-1 >= 0 and c+1 < self.cols: #NE
                    if self.grid[r-1][c+1] != -1 and self.grid[r-1][c+1] != -2:
                        self.grid[r-1][c+1] -= 1
                    
                if c+1 < self.cols: #E
                    if self.grid[r][c+1] != -1 and self.grid[r][c+1] != -2:
                        self.grid[r][c+1] -= 1
                
                if r+1 < self.rows and c+1 < self.cols: #SE
                    if self.grid[r+1][c+1] != -1 and self.grid[r+1][c+1] != -2:
                        self.grid[r+1][c+1] -= 1
                
                if r+1 < self.rows: #S
                    if self.grid[r+1][c] != -1 and self.grid[r+1][c] != -2:
                        self.grid[r+1][c] -= 1
                    
                if r+1 < self.rows and c-1 >= 0: #SW
                    if self.grid[r+1][c-1] != -1 and self.grid[r+1][c-1] != -2:
                        self.grid[r+1][c-1] -= 1
                    
                if c-1 >= 0: #W
                    if self.grid[r][c-1] != -1 and self.grid[r][c-1] != -2:
                        self.grid[r][c-1] -= 1
                    
                if r-1 >= 0 and c-1 >= 0: #NW
                    if self.grid[r-1][c-1] != -1 and self.grid[r-1][c-1] != -2:
                        self.grid[r-1][c-1] -= 1
            
            elif name == "Rook":
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
            
            elif name == "Bishop":
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
                    
            elif name == "Queen":
                ### ROOK PORTION ###
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                ### BISHOP PORTION ###
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
            
            elif name == "Knight":
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] != -1 and self.grid[r-2][c+1] != -2:
                        self.grid[r-2][c+1] -= 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] != -1 and self.grid[r-1][c+2] != -2:
                        self.grid[r-1][c+2] -= 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] != -1 and self.grid[r+1][c+2] != -2:
                        self.grid[r+1][c+2] -= 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] != -1 and self.grid[r+2][c+1] != -2:
                        self.grid[r+2][c+1] -= 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] != -1 and self.grid[r+2][c-1] != -2:
                        self.grid[r+2][c-1] -= 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] != -1 and self.grid[r+1][c-2] != -2:
                        self.grid[r+1][c-2] -= 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] != -1 and self.grid[r-1][c-2] != -2:
                        self.grid[r-1][c-2] -=1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] != -1 and self.grid[r-2][c-1] != -2:
                        self.grid[r-2][c-1] -= 1
            
            elif name == "Ferz":
                if r-1 >= 0 and c+1 < self.cols: #NE
                    if self.grid[r-1][c+1] != -1 and self.grid[r-1][c+1] != -2:
                        self.grid[r-1][c+1] -= 1
                    
                if r+1 < self.rows and c+1 < self.cols: #SE
                    if self.grid[r+1][c+1] != -1 and self.grid[r+1][c+1] != -2:
                        self.grid[r+1][c+1] -= 1
                    
                if r+1 < self.rows and c-1 >= 0: #SW
                    if self.grid[r+1][c-1] != -1 and self.grid[r+1][c-1] != -2:
                        self.grid[r+1][c-1] -= 1 
                    
                if r-1 >= 0 and c-1 >= 0: #NW
                    if self.grid[r-1][c-1] != -1 and self.grid[r-1][c-1] != -2:
                        self.grid[r-1][c-1] -= 1
                    
            elif name == "Princess":
                ### KNIGHT PORTION ###
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] != -1 and self.grid[r-2][c+1] != -2:
                        self.grid[r-2][c+1] -= 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] != -1 and self.grid[r-1][c+2] != -2:
                        self.grid[r-1][c+2] -= 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] != -1 and self.grid[r+1][c+2] != -2:
                        self.grid[r+1][c+2] -= 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] != -1 and self.grid[r+2][c+1] != -2:
                        self.grid[r+2][c+1] -= 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] != -1 and self.grid[r+2][c-1] != -2:
                        self.grid[r+2][c-1] -= 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] != -1 and self.grid[r+1][c-2] != -2:
                        self.grid[r+1][c-2] -= 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] != -1 and self.grid[r-1][c-2] != -2:
                        self.grid[r-1][c-2] -= 1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] != -1 and self.grid[r-2][c-1] != -2:
                        self.grid[r-2][c-1] -= 1
                ### BISHOP PORTION ###
                if r > 0 and c < self.cols - 1: #NE
                    while r > 0 and c < self.cols - 1:
                        r -= 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1 and c < self.cols - 1: #SE
                    while r < self.rows - 1 and c < self.cols - 1:
                        r += 1
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if r < self.rows - 1 and c > 0: #SW
                    while r < self.rows - 1 and c > 0:
                        r += 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if r > 0 and c > 0:
                    while r > 0 and c > 0: #NW
                        r -= 1
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
                    
            elif name == "Empress":
                ### KNIGHT PORTION ###
                if r-2 >= 0 and c+1 < self.cols:
                    if self.grid[r-2][c+1] != -1 and self.grid[r-2][c+1] != -2:
                        self.grid[r-2][c+1] -= 1
                    
                if r-1 >= 0 and c+2 < self.cols:
                    if self.grid[r-1][c+2] != -1 and self.grid[r-1][c+2] != -2:
                        self.grid[r-1][c+2] -= 1
                    
                if r+1 < self.rows and c+2 < self.cols:
                    if self.grid[r+1][c+2] != -1 and self.grid[r+1][c+2] != -2:
                        self.grid[r+1][c+2] -= 1
                    
                if r+2 < self.rows and c+1 < self.cols:
                    if self.grid[r+2][c+1] != -1 and self.grid[r+2][c+1] != -2:
                        self.grid[r+2][c+1] -= 1
                    
                if r+2 < self.rows and c-1 >= 0:
                    if self.grid[r+2][c-1] != -1 and self.grid[r+2][c-1] != -2:
                        self.grid[r+2][c-1] -= 1
                    
                if r+1 < self.rows and c-2 >= 0:
                    if self.grid[r+1][c-2] != -1 and self.grid[r+1][c-2] != -2:
                        self.grid[r+1][c-2] -= 1
                    
                if r-1 >= 0 and c-2 >= 0:
                    if self.grid[r-1][c-2] != -1 and self.grid[r-1][c-2] != -2:
                        self.grid[r-1][c-2] -= 1
                    
                if r-2 >= 0 and c-1 >= 0:
                    if self.grid[r-2][c-1] != -1 and self.grid[r-2][c-1] != -2:
                        self.grid[r-2][c-1] -= 1

                ### ROOK PORTION ###
                if r > 0: #up
                    while r > 0:
                        r -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
                
                if r < self.rows - 1: #down
                    while r < self.rows - 1:
                        r += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if c > 0: #left
                    while c > 0:
                        c -= 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col

                if c < self.cols - 1:
                    while c < self.cols - 1:
                        c += 1
                        if self.grid[r][c] == -1 or self.grid[r][c] == -2:
                            break
                        self.grid[r][c] -= 1
                    r = piece.row
                    c = piece.col
    
    def chooseVar(self): #variable-order heuristic
        min_idx = -10
        min_val = inf
        for i in range(len(self.pieces)):
            if self.pieces[i].row == None and self.pieces[i].col == None:
                if(len(self.pieces[i].domain) < min_val or self.pieces[i].degree < self.pieces[min_idx].degree):
                    min_val = len(self.pieces[i].domain)
                    min_idx = i
        return min_idx

    def refreshDomain(self, idx):
        new = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 0:
                    self.pieces[idx].row = r
                    self.pieces[idx].col = c
                    if not self.isInvalid(self.pieces[idx]):
                        new.append((0, (r,c)))
                    self.pieces[idx].row = None
                    self.pieces[idx].col = None
        self.pieces[idx].domain = new

    def sortDomain(self, idx): #value-order heuristic
        sorted = []
        for i in self.pieces[idx].domain:
            self.pieces[idx].row = i[1][0]
            self.pieces[idx].col = i[1][1]
            count = self.countThreatenedPos(self.pieces[idx])
            sorted.append((count, i[1]))
            self.pieces[idx].row = None
            self.pieces[idx].col = None
        sorted.sort()
        self.pieces[idx].domain = sorted
    
    def isFailure(self): #forward checking
        for i in range(len(self.pieces)):
            if self.pieces[i].row == None and self.pieces[i].col == None:
                self.refreshDomain(i)
                if len(self.pieces[i].domain) == 0:
                    return True
        return False

#############################################################################
######## State
#############################################################################
class State:
    pass

#############################################################################
######## Implement Search Algorithm
#############################################################################
def backtrack(board):
    var = board.chooseVar()
    if var == -10:
        return board #everything assigned already
    board.refreshDomain(var)
    board.sortDomain(var)
    for pos in board.pieces[var].domain:
        board.pieces[var].row = pos[1][0]
        board.pieces[var].col = pos[1][1]
        board.markThreatenedPos(var)
        if not board.isFailure():
            result = backtrack(board)
            if result != None:
                return result
        board.unmarkThreatenedPos(var)
        board.pieces[var].row = None
        board.pieces[var].col = None
    return None

def createPiece(i):
    if i == 0:
        name = "King"
    elif i == 1:
        name = "Queen"
    elif i == 2:
        name = "Bishop"
    elif i == 3:
        name = "Rook"
    elif i == 4:
        name = "Knight"
    elif i == 5:
        name = "Ferz"
    elif i == 6:
        name = "Princess"
    else:
        name = "Empress"
    piece = Piece(name)
    return piece

def search(rows, cols, grid, num_pieces):
    board = Board(rows, cols, grid)
    for i in range(len(num_pieces)):
        for j in range(num_pieces[i]):
            board.addPieceToBoard(createPiece(i))
    initial_domain = board.findInitialDomain()
    board.initialiseDomain(initial_domain)
    final = backtrack(board)
    if final != None:
        return final.solution()

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

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()
    
    piece_nums = get_par(handle.readline()).split()
    num_pieces = [int(x) for x in piece_nums] #List in the order of King, Queen, Bishop, Rook, Knight

    return rows, cols, grid, num_pieces

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
def run_CSP():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    rows, cols, grid, num_pieces = parse(testcase)
    goalstate = search(rows, cols, grid, num_pieces)
    return goalstate #Format to be returned
