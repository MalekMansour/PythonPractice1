import pygame
import sys
import numpy as np
import random
import time

pygame.init()

# Display
width, height = 1200, 600
line_width = 15
board_rows = 3
board_cols = 3
square_size = height // board_cols
circle_radius = square_size // 3
circle_width = 15
cross_width = 25
space = square_size // 4
grid_offset_x = (width - height) // 2  
grid_offset_y = 0  

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
colors = {
    'GREEN': (13, 124, 102),
    'BLUE': (30, 42, 94),
    'PINK': (247, 181, 202),
    'PURPLE': (103, 65, 136),
    'RED': (128, 0, 0),
    'ORANGE': (255, 131, 67),
    'YELLOW': (255, 218, 118),
    'TURQUOISE': (119, 228, 200),
}
bg_color = colors['BLUE']
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)

# Create display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Board setup
board = np.zeros((board_rows, board_cols))

def draw_lines():
    # Horizontal lines
    pygame.draw.line(display, line_color, (grid_offset_x, square_size), (grid_offset_x + height, square_size), line_width)
    pygame.draw.line(display, line_color, (grid_offset_x, 2 * square_size), (grid_offset_x + height, 2 * square_size), line_width)
    # Vertical lines
    pygame.draw.line(display, line_color, (grid_offset_x + square_size, grid_offset_y), (grid_offset_x + square_size, grid_offset_y + height), line_width)
    pygame.draw.line(display, line_color, (grid_offset_x + 2 * square_size, grid_offset_y), (grid_offset_x + 2 * square_size, grid_offset_y + height), line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.line(display, cross_color, (grid_offset_x + col * square_size + space, row * square_size + square_size - space), (grid_offset_x + col * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line(display, cross_color, (grid_offset_x + col * square_size + space, row * square_size + space), (grid_offset_x + col * square_size + square_size - space, row * square_size + square_size - space), cross_width)
            elif board[row][col] == 2:
                pygame.draw.circle(display, circle_color, (grid_offset_x + int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), circle_radius, circle_width)

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
    posX = grid_offset_x + col * square_size + square_size // 2

    if player == 1:
        color = cross_color
    elif player == 2:
        color = circle_color

    pygame.draw.line(display, color, (posX, 15), (posX, height - 15), line_width)

def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size // 2

    if player == 1:
        color = cross_color
    elif player == 2:
        color = circle_color

    pygame.draw.line(display, color, (grid_offset_x + 15, posY), (grid_offset_x + height - 15, posY), line_width)

def draw_ascending_diagonal(player):
    if player == 1:
        color = cross_color
    elif player == 2:
        color = circle_color

    pygame.draw.line(display, color, (grid_offset_x + 15, height - 15), (grid_offset_x + height - 15, 15), line_width)

def draw_descending_diagonal(player):
    if player == 1:
        color = cross_color
    elif player == 2:
        color = circle_color

    pygame.draw.line(display, color, (grid_offset_x + 15, 15), (grid_offset_x + height - 15, height - 15), line_width)

def restart():
    display.fill(bg_color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

def game_over_screen(bot):
    draw_text_centered("Press R to Restart", 40, white, display, width // 2, height // 2 - 40)
    draw_text_centered("Press M to go back to Main Menu", 40, white, display, width // 2, height // 2)
    draw_text_centered("Press Q to Quit", 40, white, display, width // 2, height // 2 + 40)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    play_game(bot=bot)  # Restart the game in the same mode
                elif event.key == pygame.K_m:
                    main_menu()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main_menu():
    while True:
        display.fill(bg_color)
        draw_text_centered("TIC TAC TOE", 60, white, display, width // 2, height // 4)
        draw_text_centered("Press P to Play", 40, white, display, width // 2, height // 2 - 20)
        draw_text_centered("Press C to Customize", 40, white, display, width // 2, height // 2 + 20)
        draw_text_centered("Press Q to Quit", 40, white, display, width // 2, height // 2 + 60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    choose_play_mode()
                elif event.key == pygame.K_c:
                    customize_background()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def choose_play_mode():
    while True:
        display.fill(bg_color)
        draw_text_centered("Choose Play Mode", 60, white, display, width // 2, height // 4)
        draw_text_centered("Press 1: Play Against Bot", 40, white, display, width // 2, height // 2 - 20)
        draw_text_centered("Press 2: Play Against Player", 40, white, display, width // 2, height // 2 + 20)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    play_game(bot=True)
                elif event.key == pygame.K_2:
                    play_game(bot=False)

def play_game(bot=False):
    restart()
    player = 1  # 'X' starts first
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                if grid_offset_x <= mouseX < grid_offset_x + height and grid_offset_y <= mouseY < grid_offset_y + height:
                    clicked_row = int((mouseY - grid_offset_y) // square_size)
                    clicked_col = int((mouseX - grid_offset_x) // square_size)

                    if available_square(clicked_row, clicked_col):
                        mark_square(clicked_row, clicked_col, player)
                        if check_win(player):
                            game_over = True
                            draw_figures()
                            pygame.display.update()
                            time.sleep(1)
                            game_over_screen(bot=bot)
                        player = 2 if player == 1 else 1  # Switch turns
                        draw_figures()

            if bot and player == 2 and not game_over:
                pygame.display.update()
                time.sleep(2)  # Bot "thinking" time
                bot_move = random.choice([(r, c) for r in range(board_rows) for c in range(board_cols) if available_square(r, c)])
                mark_square(bot_move[0], bot_move[1], player)
                if check_win(player):
                    game_over = True
                    draw_figures()
                    pygame.display.update()
                    time.sleep(1)
                    game_over_screen(bot=bot)
                player = 1  
                draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False

        pygame.display.update()

def customize_background():
    global bg_color
    while True:
        display.fill(bg_color)
        draw_text_centered("Choose Background Color", 40, white, display, width // 2, height // 5)
        for i, color_name in enumerate(colors.keys(), 1):
            draw_text_centered(f"Press {i}: {color_name}", 30, white, display, width // 2, height // 3 + i * 30)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for i, (color_name, color_value) in enumerate(colors.items(), 1):
                    if event.key == pygame.K_1 + (i - 1):
                        bg_color = color_value
                        main_menu()

def draw_text_centered(text, size, color, surface, x, y):
    font = pygame.font.SysFont("bahnschrift", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

# Start the game with the main menu
main_menu()
