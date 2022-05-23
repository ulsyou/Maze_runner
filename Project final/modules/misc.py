import sys
import pygame


def showText(screen, font, text, color, position):
    text_render = font.render(text, True, color)
    rect = text_render.get_rect()
    rect.left, rect.top = position
    screen.blit(text_render, rect)
    return rect.right


def Button(screen, position, text, font, button_color=(120, 120, 120), linecolor=(20, 20, 20), textcolor=(255, 255, 255), b_width=200, b_height=50):
    left, top = position
    pygame.draw.line(screen, linecolor, (left, top), (left + b_width, top), 5)
    pygame.draw.line(screen, linecolor, (left, top-2), (left, top + b_height), 5)
    pygame.draw.line(screen, linecolor, (left, top + b_height), (left + b_width, top + b_height), 5)
    pygame.draw.line(screen, linecolor, (left + b_width, top + b_height), (left + b_width, top), 5)
    pygame.draw.rect(screen, button_color, (left, top, b_width, b_height))
    text_render = font.render(text, 1, textcolor)
    rect = text_render.get_rect()
    rect.centerx, rect.centery = left + b_width / 2, top + b_height / 2
    return screen.blit(text_render, rect)


def Interface(screen, cfg, mode='game_start'):
    pygame.display.set_mode(cfg.SCREENSIZE)
    font = pygame.font.SysFont('Consolas', 30)
    if mode == 'game_start':
        clock = pygame.time.Clock()
        while True:
            screen.fill((192, 192, 192))
            button_1 = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//3), 'Bắt đầu', font)
            button_2 = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//2), 'Thoát', font)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(-1)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_1.collidepoint(pygame.mouse.get_pos()):
                        return True
                    elif button_2.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit(-1)
            pygame.display.update()
            clock.tick(cfg.FPS)
    elif mode == 'game_switch':
        clock = pygame.time.Clock()
        while True:
            screen.fill((192, 192, 192))
            button_1 = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//3), 'Màn kế', font)
            button_2 = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//2), 'Thoát', font)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(-1)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_1.collidepoint(pygame.mouse.get_pos()):
                        return True
                    elif button_2.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit(-1)
            pygame.display.update()
            clock.tick(cfg.FPS)

