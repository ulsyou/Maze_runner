import pygame

# Kích thước cửa sổ
WIDTH = 1280
HEIGHT = 720
FPS = 60

# Màu
WHITE = (0, 0, 0, 0.1)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
LOAD = (255, 255, 255)
TITLE = (255, 0, 255)

# Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

# Vector
x = 0
y = 0
w = 20                   # chiều rộng
grid = []
visited = []
stack = []
solution = {}