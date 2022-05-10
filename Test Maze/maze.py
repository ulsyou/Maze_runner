import pygame
import random
import time
from setting import *
from control import *


# Tạo lưới

def build_grid(x, y, w):
    for i in range(1, 35):
        x = 20                                                            # Vị trí khởi đầu
        y = y + 20                                                        # Hàng mới
        for j in range(1, 63):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           # left
            grid.append((x, y))                                           # đưa ô vào ds grid
            x = x + 20                                                    # dịch chuyển ô sang vị trí mới


def create_maze(x, y):
    single_cell(x, y)                                              # vị trí tạo bảng
    stack.append((x, y))                                            # đưa ô đầu tiên vào stack
    visited.append((x, y))                                          # đưa ô đã visited vào stack
    while len(stack) > 0:                                          # lặp đến khi rỗng
        time.sleep(.05)                                          # giới hạn tốc độ tạo mê cung
        cell = []                                                  # khởi tạo ds cell
        if (x + w, y) not in visited and (x + w, y) in grid:       # check đã duyệt hay chưa
            cell.append("right")                                   # nếu đã duyệt, đưa vào list

        if (x - w, y) not in visited and (x - w, y) in grid:
            cell.append("left")

        if (x, y + w) not in visited and (x, y + w) in grid:
            cell.append("down")

        if (x, y - w) not in visited and (x, y - w) in grid:
            cell.append("up")

        if len(cell) > 0:                                          # check list rỗng hay ko
            cell_chosen = (random.choice(cell))                    # random chọn ô kế tiếp

            if cell_chosen == "right":                             # Nếu đã chọn
                push_right(x, y)                                   # gọi hàm push
                solution[(x + w, y)] = x, y                        # giải = ô mới -> ô hiện tại
                x = x + w                                          # chuyển ô hiện tại đến vị trí mới -> cập nhật thành ô hiện tại
                visited.append((x, y))                             # đưa vào visited list
                stack.append((x, y))                               # đưa ô hiện tại vào stack

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x, y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x, y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    # Nếu không có ô nào trống -> đưa 1 ô ra khỏi stack
            single_cell(x, y)                                     # dùng hàm single_cell gọi đường quay lui
            time.sleep(.01)                                     # giới hạn tốc độ nháy con chạy
            backtracking_cell(x, y)
