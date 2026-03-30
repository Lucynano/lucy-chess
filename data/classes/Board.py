import pygame

from data.classes.Square import Square
from data.classes.pieces.Rook import Rook
from data.classes.pieces.Bishop import Bishop
from data.classes.pieces.Knight import Knight
from data.classes.pieces.Queen import Queen
from data.classes.pieces.King import King
from data.classes.pieces.Pawn import Pawn

# Game state checker
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        self.selected_piece = None
        self.turn = 'white'
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ] # represents the chessboard configuration with a 2D list having our pieces with their default position
        self.squares = self.generate_squares() # for making chess tiles and putting them all in a list
        self.setup_board()

    def generate_squares(self):
        output = {}
        for y in range(8):
            for x in range(8):
                square = Square(x, y, self.tile_width, self.tile_height)
                output[(x, y)] = square
        return output
    
    def get_square_from_pos(self, pos):
        return self.squares.get(pos)
            
    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x, y))
                    # looking inside contents, what piece does it have
                    if piece[1] == 'R':
                        square.occupying_piece = Rook(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'N':
                        square.occupying_piece = Knight(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'B':
                        square.occupying_piece = Bishop(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'Q':
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'K':
                        square.occupying_piece = King(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'P':
                        square.occupying_piece = Pawn(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
    
    def handle_click(self, mx, my):
        x = mx // self.tile_width
        y = my // self.tile_height
        
        square = self.get_square_from_pos((x, y))

        if self.selected_piece is None:
            if square.occupying_piece and square.occupying_piece.color == self.turn:
                self.selected_piece = square.occupying_piece
        else:
            if self.selected_piece.move(self, square):
                self.turn = 'white' if self.turn == 'black' else 'black'
            elif square.occupying_piece and square.occupying_piece.color == self.turn:
                self.selected_piece = square.occupying_piece

    # check state checker
    def is_in_check(self, color, board_change=None): # board_change = [(x1, y1), (x2, y2)]
        output = False
        king_pos = None
        changing_piece = None
        old_square = None
        new_square = None
        new_square_old_piece = None
        if board_change is not None:
            for square in self.squares.values():
                if square.pos == board_change[0]:
                    changing_piece = square.occupying_piece
                    old_square = square
                    old_square.occupying_piece = None
            for square in self.squares.values():
                if square.pos == board_change[1]:
                    new_square = square
                    new_square_old_piece = new_square.occupying_piece
                    new_square.occupying_piece = changing_piece
        pieces = [
            i.occupying_piece for i in self.squares.values() if i.occupying_piece is not None
        ]
        if changing_piece is not None:
            if changing_piece.notation == 'K':
                king_pos = new_square.pos
        if king_pos == None:
                for piece in pieces:
                    if piece.notation == 'K' and piece.color == color:
                        king_pos = piece.pos
        for piece in pieces:
                if piece.color != color:
                    for square in piece.attacking_squares(self):
                        if square.pos == king_pos:
                            output = True
        if board_change is not None:
            old_square.occupying_piece = changing_piece
            new_square.occupying_piece = new_square_old_piece
        return output
            
    # checkmate state checker
    def is_in_checkmate(self, color):
        output = False
        for piece in [i.occupying_piece for i in self.squares.values()]:
            if piece != None:
                if piece.notation == 'K' and piece.color == color:
                    king = piece
        if king.get_valid_moves(self) == []:
            if self.is_in_check(color):
                output = True
        return output

    def clear_highlights(self):
        for square in self.squares.values():
            square.highlight = False

    def get_king(self, color):
        for square in self.squares.values():
            piece = square.occupying_piece
            if piece and piece.notation == 'K' and piece.color == color:
                return piece
        return None

    # highlights all the possible moves of a piece once selected while it is its color's turn
    def draw(self, display):
        self.clear_highlights()

        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            for square in self.selected_piece.get_valid_moves(self):
                square.highlight = True
        for square in self.squares.values():
            square.draw(display)
        if self.is_in_check(self.turn):
            king = self.get_king(self.turn)
            if king:
                square = self.get_square_from_pos(king.pos)
                pygame.draw.rect(
                    display,
                    (255, 0, 0),
                    square.rect,
                    4
                )


    def is_stalemate(self, color):
        if self.is_in_check(color):
            return False
        
        for square in self.squares.values():
            piece = square.occupying_piece

            if piece and piece.color == color:
                if piece.get_valid_moves(self):
                    return False
        return True