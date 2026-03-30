import pygame
from data.classes.Piece import Piece

class Rook(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/imgs/' + color[0] + 'r.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        self.notation = 'R'

    def get_possible_moves(self, board):
        output = []
        # 4 directions: N, E, S, W
        directions = [(0,-1), (1,0), (0,1), (-1,0)]
        for dx, dy in directions:
            x, y = self.x, self.y
            while True:
                x += dx
                y += dy
                if x < 0 or x > 7 or y < 0 or y > 7:
                   break
                square = board.get_square_from_pos((x, y))
                if square.occupying_piece is None:
                    output.append(square)
                elif square.occupying_piece.color != self.color:
                   output.append(square)
                   break
                else:
                   break
        return output
       
       