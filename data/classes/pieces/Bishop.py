import pygame
from data.classes.Piece import Piece

class Bishop(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/images' + color[0] + 'b.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'B'

    def get_possible_moves(self, board):
        output = []
        # moves north east
        moves_ne = []
        for i in range(1, 8):
            if self.x + 1 > 7 or self.y - i < 0:
                break
            moves_ne.append(board.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        output.append(moves_ne)
        # moves south east
        moves_se = []
        for i in range(1, 8):
            if self.x + 1 > 7 or self.y + i > 7:
                break
            moves_se.append(board.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        output.append(moves_se)
        # moves south west
        moves_sw = []
        for i in range(1, 8):
            if self.x - 1 < 0 or self.y + i > 7:
                break
            moves_sw.append(board.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        output.append(moves_sw)
        # moves north west
        moves_nw = []
        for i in range(1, 8):
            if self.x - 1 < 0 or self.y - i < 7:
                break
            moves_nw.append(board.get_square_from_pos(
                (self.x - i, self.y - i)
            ))
        output.append(moves_nw)