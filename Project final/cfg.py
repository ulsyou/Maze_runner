import os
import pygame

SCREENSIZE = (900, 635)
BGMPATH = os.path.join(os.getcwd(), 'resources/audios/bgm.mp3')
HEROPICPATH = os.path.join(os.getcwd(), 'resources/images/hero.png')
FPS = 120
BLOCKSIZE = 15
MAZESIZE = (35, 50) # num_rows * num_cols
BORDERSIZE = (75, 55) # 75 * 2 + 50 * 15 = 900, 55 * 2 + 35 * 15 = 635
pygame_icon = pygame.image.load('resources/images/icon.jpg')
pygame.display.set_icon(pygame_icon)