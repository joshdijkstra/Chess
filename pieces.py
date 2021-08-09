import pygame

def coord_converter(pos):
    return [30+pos[1]*60,30+pos[0]*60]

class Pieces():
    def __init__(self,team,pos):
        self.white = team
        self.pos = pos
        self.coords = coord_converter(pos)
        self.rectangle_draging = False
        self.selected = False
        self.hasMoved = False

    def load_image(self,piece):
        if self.white:
            file_name = "ChessPieces/Chess_" + piece +  "lt60.png"
        else:
            file_name = "ChessPieces/Chess_" + piece +  "dt60.png"
        image = pygame.image.load(file_name)
        rect = pygame.Rect(image.get_rect(center=(self.coords[0],self.coords[1])))
        return image , rect

    def move_image(self,x,y):
        self.pos = [x,y]
        self.coords =  [y*60,x*60]
        self.rect.x = self.coords[1]
        self.rect.y = self.coords[0]



    def load_legal_squares(self,wt,bl):
        rects = []
        image = pygame.image.load("ChessPieces/board3.png")
        moves = self.find_moves()
        squares = self.find_legal(moves,wt,bl)
        for x in range(len(squares)):
            coord = coord_converter(squares[x])
            rect = pygame.Rect(image.get_rect(center=(coord[1],coord[0])))
            rects.append(rect)
        return image , rects

    def snap_to_grid(self,mx,my,wt,bl):
        x = mx // 60
        y = my // 60
        moves = self.find_moves()
        legal_moves = self.find_legal(moves,wt,bl)
        if [x,y] in legal_moves:
            self.move(x,y)
            self.hasMoved = True
        else:
            print("Illegal Move")
            self.move(self.pos[0],self.pos[1])
        return self

    def find_legal(self,moves,white_pieces,black_pieces):
        legal_moves = []
        black_loc = []
        white_loc = []
        true_moves = []
        for move in moves:
            if move[0] >= 0 and move[0] < 8:
                if move[1] >= 0 and move[1] < 8:
                    legal_moves.append(move)
        for piece in white_pieces:
            white_loc.append(piece.pos)
        for piece in black_pieces:
            black_loc.append(piece.pos)

        #print(legal_moves)
        #print(white_loc)
        for move in legal_moves:
            #print(move)
            if self.white:
                if move in white_loc:
                    legal_moves.remove(move)
        return legal_moves

    def move(self,x,y):
        self.move_image(x,y)

class Pawn(Pieces):
    def __init__(self,team,pos):
        Pieces.__init__(self,team,pos)
        self.image , self.rect = self.load_image("p")

    def find_moves(self):
        moves = []
        if self.white:

        return moves

class King(Pieces):
    def __init__(self,team,pos):
        Pieces.__init__(self,team,pos)
        self.image , self.rect = self.load_image("k")

class Queen(Pieces):
    def __init__(self,team,pos):
        Pieces.__init__(self,team,pos)
        self.image , self.rect = self.load_image("q")

class Knight(Pieces):
    def __init__(self,team,pos):
        Pieces.__init__(self,team,pos)
        self.image , self.rect = self.load_image("n")

    def find_moves(self):
        moves = []
        moves.append([self.pos[0]-2 , self.pos[1]+1])
        moves.append([self.pos[0]-1 , self.pos[1]+2])
        moves.append([self.pos[0]+1 , self.pos[1]+2])
        moves.append([self.pos[0]+2 , self.pos[1]+1])
        moves.append([self.pos[0]+2 , self.pos[1]-1])
        moves.append([self.pos[0]+1 , self.pos[1]-2])
        moves.append([self.pos[0]-1 , self.pos[1]-2])
        moves.append([self.pos[0]-2 , self.pos[1]-1])
        return moves

class Bishop(Pieces):
    def __init__(self,team,pos):
        Pieces.__init__(self,team,pos)
        self.image , self.rect = self.load_image("b")

class Rook(Pieces):
    def __init__(self,team,pos):
        Pieces.__init__(self,team,pos)
        self.image , self.rect = self.load_image("r")

    def find_moves(self):
        moves = []
        moves.append([self.pos[0] , self.pos[1]+1])
        moves.append([self.pos[0] , self.pos[1]+2])
        moves.append([self.pos[0] , self.pos[1]+3])
        moves.append([self.pos[0] , self.pos[1]+4])
        moves.append([self.pos[0] , self.pos[1]+5])
        moves.append([self.pos[0] , self.pos[1]+6])
        moves.append([self.pos[0] , self.pos[1]+7])

        moves.append([self.pos[0] , self.pos[1]-1])
        moves.append([self.pos[0] , self.pos[1]-2])
        moves.append([self.pos[0] , self.pos[1]-3])
        moves.append([self.pos[0] , self.pos[1]-4])
        moves.append([self.pos[0] , self.pos[1]-5])
        moves.append([self.pos[0] , self.pos[1]-6])
        moves.append([self.pos[0] , self.pos[1]-7])

        moves.append([self.pos[0]+1 , self.pos[1]])
        moves.append([self.pos[0]+2 , self.pos[1]])
        moves.append([self.pos[0]+3 , self.pos[1]])
        moves.append([self.pos[0]+4 , self.pos[1]])
        moves.append([self.pos[0]+5 , self.pos[1]])
        moves.append([self.pos[0]+6 , self.pos[1]])
        moves.append([self.pos[0]+7 , self.pos[1]])

        moves.append([self.pos[0]-1 , self.pos[1]])
        moves.append([self.pos[0]-2 , self.pos[1]])
        moves.append([self.pos[0]-3 , self.pos[1]])
        moves.append([self.pos[0]-4 , self.pos[1]])
        moves.append([self.pos[0]-5 , self.pos[1]])
        moves.append([self.pos[0]-6 , self.pos[1]])
        moves.append([self.pos[0]-7 , self.pos[1]])

        return moves
