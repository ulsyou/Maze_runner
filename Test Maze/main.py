import pygame
import random
from setting import *
from control import *
from maze import *

x, y = 20, 20                   # vị trí tạo lưới
build_grid(40, 0, 20)
create_maze(x, y)               # gọi hàm tạo mê cung
solving(1240, 680)               # gọi hàm solve

# main
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
