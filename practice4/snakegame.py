import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define default colors
white = (255, 255, 255)
black = (0, 0, 0)
background_color = (30, 30, 60)  # Default background color

# Set default snake and background colors (using the provided hex colors)
snake_color = (13, 124, 102)  # Green Snake
background_color = (30, 42, 94)  # Blue Background

# Set clock
clock = pygame.time.Clock()

# Set snake speed
snake_speed = 15

# Set snake block size
snake_block = 10

# Define font style and size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def draw_rounded_rect(surface, color, rect, radius=0.5):
    """ Draws a rounded rectangle. """
    rect = pygame.Rect(rect)
    color = pygame.Color(*color)
    radius = min(rect.width, rect.height) * radius
    shape_surf = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, (0, 0, *rect.size), border_radius=int(radius))
    surface.blit(shape_surf, rect.topleft)

def draw_gradient_background(color_top, color_bottom):
    """ Draws a gradient background from top to bottom. """
    for y in range(height):
        color = [
            color_top[i] + (color_bottom[i] - color_top[i]) * y // height
            for i in range(3)
        ]
        pygame.draw.line(display, color, (0, y), (width, y))

def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        draw_rounded_rect(display, color, [x[0], x[1], snake_block, snake_block], radius=0.2)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    display.blit(value, [0, 0])

def message(msg, color, y_displace=0, size="small"):
    if size == "small":
        text_surface = font_style.render(msg, True, color)
    elif size == "large":
        text_surface = score_font.render(msg, True, color)
    
    text_rect = text_surface.get_rect(center=(width / 2, height / 2 + y_displace))
    display.blit(text_surface, text_rect)

def gameLoop():  # Main function
    global snake_color, background_color

    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Generate food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            draw_gradient_background(background_color, (10, 10, 30))
            message("You Lost!", white, y_displace=-50, size="large")
            message("Press M to return to Main Menu", white, y_displace=0, size="small")
            message("Press Q to Quit", white, y_displace=30, size="small")
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_m:
                        game_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        draw_gradient_background(background_color, (10, 10, 30))

        draw_rounded_rect(display, (255, 218, 118), [foodx, foody, snake_block, snake_block], radius=0.5)  # Food color (Yellow)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list, snake_color)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def customize_menu():
    global snake_color, background_color
    customizing = True
    while customizing:
        draw_gradient_background(background_color, (10, 10, 30))
        message("Customize Menu", white, y_displace=-100, size="large")
        message("Press 1 to Change Snake Color", white, y_displace=-30)
        message("Press 2 to Change Background Color", white, y_displace=0)
        message("Press B to go Back", white, y_displace=30)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Change snake color
                    snake_color = choose_color("snake")
                elif event.key == pygame.K_2:
                    # Change background color
                    background_color = choose_color("background")
                elif event.key == pygame.K_b:
                    customizing = False

def choose_color(item):
    # Define the provided hex colors
    colors = {
        pygame.K_1: (13, 124, 102),   # Green
        pygame.K_2: (30, 42, 94),     # Blue
        pygame.K_3: (247, 181, 202),  # Pink
        pygame.K_4: (103, 65, 136),   # Purple
        pygame.K_5: (128, 0, 0),      # Red
        pygame.K_6: (255, 131, 67),   # Orange
        pygame.K_7: (255, 218, 118),  # Yellow
        pygame.K_8: (119, 228, 200),  # Turquoise
    }
    color_names = {
        pygame.K_1: "Snake Green",
        pygame.K_2: "Sea Blue",
        pygame.K_3: "Cuty Pink",
        pygame.K_4: "Lover Purple",
        pygame.K_5: "Killer Red",
        pygame.K_6: "Hacker Orange",
        pygame.K_7: "Sunshine Yellow",
        pygame.K_8: "Pearl Turquoise",
    }
    choosing = True
    while choosing:
        draw_gradient_background(background_color, (10, 10, 30))
        message(f"Choose {item} Color", white, y_displace=-100, size="large")
        for key, color in color_names.items():
            message(f"{pygame.key.name(key)} - {color}", white, y_displace=-100 + 30 * list(color_names.keys()).index(key) + 30)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in colors:
                    choosing = False
                    return colors[event.key]

def game_menu():
    menu = True
    while menu:
        draw_gradient_background(background_color, (10, 10, 30))
        message("Snake Game", white, y_displace=-100, size="large")
        message("Press S to Start", white, y_displace=-10)
        message("Press C to Customize", white, y_displace=20)
        message("Press Q to Quit", white, y_displace=50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameLoop()
                elif event.key == pygame.K_c:
                    customize_menu()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Run the game menu
game_menu()
