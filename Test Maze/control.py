import pygame
import time
from setting import *


def push_up(x, y):
    pygame.draw.rect(screen, GRAY, (x + 1, y - w + 1, 19, 39), 0)         # vẽ ô gấp đôi kích thước cũ
    pygame.display.update()                                               # xóa tường


def push_down(x, y):
    pygame.draw.rect(screen, GRAY, (x + 1, y + 1, 19, 39), 0)
    pygame.display.update()


def push_left(x, y):
    pygame.draw.rect(screen, GRAY, (x - w + 1, y + 1, 39, 19), 0)
    pygame.display.update()


def push_right(x, y):
    pygame.draw.rect(screen, GRAY, (x + 1, y + 1, 39, 19), 0)
    pygame.display.update()


def single_cell(x, y):
    pygame.draw.rect(screen, GREEN, (x + 1, y + 1, 18, 18), 0)          # tạo con chạy
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, GRAY, (x + 1, y + 1, 18, 18), 0)        # đè màu, xóa đường đi của con chạy
    pygame.display.update()


def solution_cell(x, y):
    pygame.draw.rect(screen, YELLOW, (x + 8, y + 8, 5, 5), 0)             # đường giải
    pygame.display.update()


def solving(x, y):
    solution_cell(x, y)                                          # list solve chứa ô để quay lại vị trí bắt đầu
    while (x, y) != (20, 20):                                    # lặp đến khi vị trí ô -> vị trí bắt đầu
        x, y = solution[x, y]
        solution_cell(x, y)                                      # đường quay lui
        time.sleep(.05)                                          # giới hạn tốc độ vẽ đường giải
