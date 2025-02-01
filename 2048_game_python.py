import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 500
TILE_SIZE = 100
GRID_SIZE = 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Font
font = pygame.font.SysFont("Times New Roman", 40)
small_font = pygame.font.SysFont("Times New Roman", 30)

# Initializing screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Initializing grid
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Score
score = 0
high_score = 0

# Game state
game_over = False
win = False

def show_welcome_screen():
    screen.fill(WHITE)
    welcome_text = font.render("Welcome to 2048!", True, BLACK)
    start_text = font.render("Click Enter to Start", True, BLACK)
    screen.blit(welcome_text, (WIDTH // 2 - welcome_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 20))
    pygame.display.flip()

def wait_for_enter():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    waiting = False
                    
def add_new_tile():
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4

def draw_grid():
    screen.fill(WHITE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = grid[i][j]
            color = COLORS.get(value, WHITE)
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE + 100, TILE_SIZE, TILE_SIZE))
            if value != 0:
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + 100 + TILE_SIZE // 2))
                screen.blit(text, text_rect)

def draw_score():
    score_text = small_font.render(f"Score: {score}", True, BLACK)
    high_score_text = small_font.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 50))

def draw_restart_button():
    pygame.draw.rect(screen, GRAY, (WIDTH - 120, 10, 110, 40))
    restart_text = small_font.render("Restart", True, BLACK)
    screen.blit(restart_text, (WIDTH - 110, 15))

def move_left():
    global score
    old_grid = [row[:] for row in grid]  # Create a copy of the grid
    for i in range(GRID_SIZE):
        row = grid[i]
        new_row = [cell for cell in row if cell != 0]
        new_row += [0] * (GRID_SIZE - len(new_row))
        for j in range(GRID_SIZE - 1):
            if new_row[j] == new_row[j + 1] and new_row[j] != 0:
                new_row[j] *= 2
                score += new_row[j]
                new_row[j + 1] = 0
        new_row = [cell for cell in new_row if cell != 0]
        new_row += [0] * (GRID_SIZE - len(new_row))
        grid[i] = new_row
    return old_grid != grid  # Returning True if the grid changed

def move_right():
    global score
    old_grid = [row[:] for row in grid]
    for i in range(GRID_SIZE):
        row = grid[i]
        new_row = [cell for cell in row if cell != 0]
        new_row = [0] * (GRID_SIZE - len(new_row)) + new_row
        for j in range(GRID_SIZE - 1, 0, -1):
            if new_row[j] == new_row[j - 1] and new_row[j] != 0:
                new_row[j] *= 2
                score += new_row[j]
                new_row[j - 1] = 0
        new_row = [cell for cell in new_row if cell != 0]
        new_row = [0] * (GRID_SIZE - len(new_row)) + new_row
        grid[i] = new_row
    return old_grid != grid

def move_up():
    global score
    old_grid = [row[:] for row in grid]
    for j in range(GRID_SIZE):
        column = [grid[i][j] for i in range(GRID_SIZE)]
        new_column = [cell for cell in column if cell != 0]
        new_column += [0] * (GRID_SIZE - len(new_column))
        for i in range(GRID_SIZE - 1):
            if new_column[i] == new_column[i + 1] and new_column[i] != 0:
                new_column[i] *= 2
                score += new_column[i]
                new_column[i + 1] = 0
        new_column = [cell for cell in new_column if cell != 0]
        new_column += [0] * (GRID_SIZE - len(new_column))
        for i in range(GRID_SIZE):
            grid[i][j] = new_column[i]
    return old_grid != grid

def move_down():
    global score
    old_grid = [row[:] for row in grid]
    for j in range(GRID_SIZE):
        column = [grid[i][j] for i in range(GRID_SIZE)]
        new_column = [cell for cell in column if cell != 0]
        new_column = [0] * (GRID_SIZE - len(new_column)) + new_column
        for i in range(GRID_SIZE - 1, 0, -1):
            if new_column[i] == new_column[i - 1] and new_column[i] != 0:
                new_column[i] *= 2
                score += new_column[i]
                new_column[i - 1] = 0
        new_column = [cell for cell in new_column if cell != 0]
        new_column = [0] * (GRID_SIZE - len(new_column)) + new_column
        for i in range(GRID_SIZE):
            grid[i][j] = new_column[i]
    return old_grid != grid

def check_game_over():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return False
            if j < GRID_SIZE - 1 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < GRID_SIZE - 1 and grid[i][j] == grid[i + 1][j]:
                return False
    return True

def check_win():
    for row in grid:
        if 2048 in row:
            return True
    return False

def restart_game():
    global grid, score, game_over, win
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    score = 0
    game_over = False
    win = False
    add_new_tile()
    add_new_tile()

show_welcome_screen()
wait_for_enter()

# Add initial tiles
add_new_tile()
add_new_tile()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over and not win:
                moved = False
                if event.key == pygame.K_LEFT:
                    moved = move_left()
                elif event.key == pygame.K_RIGHT:
                    moved = move_right()
                elif event.key == pygame.K_UP:
                    moved = move_up()
                elif event.key == pygame.K_DOWN:
                    moved = move_down()
                if moved:
                    add_new_tile()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if WIDTH - 120 <= x <= WIDTH - 10 and 10 <= y <= 50:
                restart_game()

    draw_grid()
    draw_score()
    draw_restart_button()

    if not win and check_win():
        win = True
        win_text = font.render("You Win!", True, BLACK)
        screen.blit(win_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))

    if not game_over and check_game_over():
        game_over = True
        game_over_text = font.render("Game Over!", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))

    pygame.display.flip()

pygame.quit()