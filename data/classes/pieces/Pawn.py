import pygame

from data.classes.Piece import Piece

class Pawn(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/imgs/' + color[0] + 'p.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        self.notation = ' '

    def get_possible_moves(self, board):
        output = []
        moves = []

        # move forward
        if self.color == 'white':
            moves.append((0, -1)) # the pawn can move 1 step forward at a time
            if not self.has_moved: 
                moves.append((0, -2)) # can move up to 2 tiles from its starting position only
        elif self.color == 'black':
            moves.append((0, 1))
            if not self.has_moved:
                moves.append((0, 2))
        for move in moves:
            new_pos = (self.x, self.y + move[1])
            if new_pos[1] < 8 and new_pos[1] >= 0:
                output.append(
                    board.get_square_from_pos(new_pos)
                )
        return output
    
    def get_moves(self, board):
        output = []

        # moves forward
        step = -1 if self.color == 'white' else 1
        front_square = board.get_square_from_pos((self.x, self.y + step))
        if front_square and front_square.occupying_piece is None:
            output.append(front_square)
            # moves 2 steps forward
            if not self.has_moved:
                double_square = board.get_square_from_pos((self.x, self.y + 2*step))
                if double_square.occupying_piece is None:
                    output.append(double_square)
    
        # moves diagonal
        for dx in [-1, 1]:
            diag_square = board.get_square_from_pos((self.x + dx, self.y + step))
            if diag_square and diag_square.occupying_piece is not None:
                if diag_square.occupying_piece.color != self.color:
                    output.append(diag_square)

        return output
    
    def attacking_squares(self, board):
        return self.get_moves(board)