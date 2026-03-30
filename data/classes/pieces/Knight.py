import pygame
from data.classes.Piece import Piece

class Knight(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/imgs/' + color[0] + 'n.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        self.notation = 'N'

    def get_possible_moves(self, board):
        output = []
        moves = [
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
        ]
        for dx, dy in moves:
            x, y = self.x + dx, self.y + dy
            if 0 <= x <= 7 and 0 <= y <= 7:
                square = board.get_square_from_pos((x, y))
                if square.occupying_piece is None or square.occupying_piece.color != self.color:
                    output.append(square)
        return output