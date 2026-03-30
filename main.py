import pygame

from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()

if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # quit the game if the user presses the close btn
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked
                if event.button == 1:
                    board.handle_click(mx, my)
        if board.is_in_checkmate('black'): # if black is in checkmate
            print('White wins!')
            running = False
        elif board.is_in_checkmate('white'): # idem for white
            print('Black wins!')
            running = False
        # draw the board
        draw(screen)