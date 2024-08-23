import pygame
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Set up display
width, height = 300, 300
line_width = 10
board_rows = 3
board_cols = 3
square_size = width // board_cols
circle_radius = square_size // 3
circle_width = 15
cross_width = 25
space = square_size // 4

# Define colors
bg_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)

# Create display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
display.fill(bg_color)

# Board setup
board = np.zeros((board_rows, board_cols))

def draw_lines():
    # Horizontal lines
    pygame.draw.line(display, line_color, (0, square_size), (width, square_size), line_width)
    pygame.draw.line(display, line_color, (0, 2 * square_size), (width, 2 * square_size), line_width)
    # Vertical lines
    pygame.draw.line(display, line_color, (square_size, 0), (square_size, height), line_width)
    pygame.draw.line(display, line_color, (2 * square_size, 0), (2 * square_size, height), line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(display, circle_color, (int(col * square_size + square_size//2), int(row * square_size + square_size//2)), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(display, cross_color, (col * square_size + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line(display, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    return not np.any(board == 0)

def check_win(player):
    # Vertical win check
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # Horizontal win check
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # Ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_ascending_diagonal(player)
        return True

    # Descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_descending_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * square_size + square_size//2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(display, color, (posX, 15), (posX, height - 15), line_width)

def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size//2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(display, color, (15, posY), (width - 15, posY), line_width)

def draw_ascending_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(display, color, (15, height - 15), (width - 15, 15), line_width)

def draw_descending_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(display, color, (15, 15), (width - 15, height - 15), line_width)

def restart():
    display.fill(bg_color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

draw_lines()

# Main loop
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // square_size)
            clicked_col = int(mouseX // square_size)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = 3 - player  # Switch player
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()
