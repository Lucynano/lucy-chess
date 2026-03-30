import pygame

from data.classes.Piece import Piece

class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/imgs/' + color[0] + 'q.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        self.notation = 'Q'

    # moves like Bishop + Rook
    def get_possible_moves(self, board):
        output = []
        # N, NE, E, SE, S, SW, W, NW
        directions = [
            (0,-1), (1,-1), (1,0), (1,1),
            (0,1), (-1,1), (-1,0), (-1,-1)
        ]
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