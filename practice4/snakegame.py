import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set default colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set default snake and background colors
snake_color = black
background_color = blue

# Set clock
clock = pygame.time.Clock()

# Set snake speed
snake_speed = 15

# Set snake block size
snake_block = 10

# Define font style and size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(display, color, [x[0], x[1], snake_block, snake_block])

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
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
            display.fill(background_color)
            message("You Lost! Press Q-Quit or C-Play Again", red, y_displace=-50, size="large")
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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
        display.fill(background_color)

        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
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
        display.fill(background_color)
        message("Customize Menu", green, y_displace=-100, size="large")
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
    colors = {
        pygame.K_r: red,
        pygame.K_g: green,
        pygame.K_b: blue,
        pygame.K_w: white,
        pygame.K_y: yellow,
        pygame.K_k: black
    }
    choosing = True
    while choosing:
        display.fill(background_color)
        message(f"Choose {item} Color", green, y_displace=-100, size="large")
        message("R - Red", red, y_displace=-30)
        message("G - Green", green, y_displace=0)
        message("B - Blue", blue, y_displace=30)
        message("W - White", white, y_displace=60)
        message("Y - Yellow", yellow, y_displace=90)
        message("K - Black", black, y_displace=120)
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
        display.fill(background_color)
        message("Snake Game", green, y_displace=-100, size="large")
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
