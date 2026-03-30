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

def show_modal(display, message):
    width, height = display.get_size()
    
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))  
    
    font = pygame.font.SysFont(None, 60)
    text = font.render(message, True, (255, 255, 255))  # texte blanc
    text_rect = text.get_rect(center=(width // 2, height // 2))
    
    display.blit(overlay, (0, 0))
    display.blit(text, text_rect)
    
    pygame.display.update()

if __name__ == '__main__':
    running = True
    game_over = False
    winner = None

    while running:
        mx, my = pygame.mouse.get_pos()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if event.button == 1:
                    board.handle_click(mx, my)
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                running = False
    
        if not game_over:
            if board.is_in_checkmate('black'):
                winner = 'White'
                game_over = True
            elif board.is_in_checkmate('white'):
                winner = 'Black'
                game_over = True
        
        draw(screen)
        
        if game_over:
            show_modal(screen, f'{winner} wins!')