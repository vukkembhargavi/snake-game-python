import pygame
import time
import random

# Ask player for their name
player_name = input("Enter your name: ")

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Fonts
font_game = pygame.font.SysFont('Arial', 36, bold=True)
font_user = pygame.font.SysFont('Arial', 24, bold=True)
font_score = pygame.font.SysFont('Arial', 24, bold=True)

# Load and scale images
bg_img = pygame.image.load(r'c:/kannaya/python_practise/snake game/snake garden.png')
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

food_img = pygame.image.load(r'c:/kannaya/python_practise/snake game/snake food.png')
food_img = pygame.transform.scale(food_img, (36, 36))

snake_img = pygame.image.load(r'c:/kannaya/python_practise/snake game/snake.png')
snake_img = pygame.transform.scale(snake_img, (36, 36))

# Snake settings
snake_block = 36  # Large/medium size
snake_speed = 5   # Slow/medium speed
clock = pygame.time.Clock()

def draw_snake(snake_list):
    for x in snake_list:
        screen.blit(snake_img, (x[0], x[1]))

def message(msg, color, font, pos):
    text = font.render(msg, True, color)
    screen.blit(text, pos)

def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, HEIGHT - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close:
            screen.blit(bg_img, (0, 0))
            # Centered game over message
            over_text = font_game.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            over_rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(over_text, over_rect)
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
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.blit(bg_img, (0, 0))

        # Draw food
        screen.blit(food_img, (food_x, food_y))

        # Draw snake
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_List)

        # Draw centered game name
        game_name_text = font_game.render("SNAKE GAME", True, RED)
        game_name_rect = game_name_text.get_rect(center=(WIDTH // 2, 30))
        screen.blit(game_name_text, game_name_rect)

        # Draw player name below game name
        player_text = font_user.render(f"Player: {player_name}", True, BLACK)
        player_rect = player_text.get_rect(center=(WIDTH // 2, 70))
        screen.blit(player_text, player_rect)

        # Draw score below player name
        score_text = font_score.render("Score: " + str(Length_of_snake - 1), True, BLUE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(score_text, score_rect)

        pygame.display.update()

        # Check if snake eats food (using rectangle collision)
        snake_rect = pygame.Rect(x1, y1, snake_block, snake_block)
        food_rect = pygame.Rect(food_x, food_y, snake_block, snake_block)
        if snake_rect.colliderect(food_rect):
            food_x = round(random.randrange(0, WIDTH - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, HEIGHT - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()