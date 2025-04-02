import pygame
import sys

# Initialize PyGame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)

# Fonts
TITLE_FONT = pygame.font.Font(None, 80)
SUBTITLE_FONT = pygame.font.Font(None, 50)
BUTTON_FONT = pygame.font.Font(None, 40)

# Draw a button with centered text
def draw_button(text, x, y, width, height, color, text_color=BLACK):
    pygame.draw.rect(SCREEN, color, (x, y, width, height), border_radius=8)
    pygame.draw.rect(SCREEN, BLACK, (x, y, width, height), 3, border_radius=8)  # Add border
    label = BUTTON_FONT.render(text, True, text_color)
    SCREEN.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))
    return pygame.Rect(x, y, width, height)

def start_screen():
    SCREEN.fill(WHITE)

    title = TITLE_FONT.render("Welcome to Sudoku", True, BLACK)
    SCREEN.blit(title, ((WIDTH - title.get_width()) // 2, 100))

    subtitle = SUBTITLE_FONT.render("Select Game Mode:", True, BLACK)
    SCREEN.blit(subtitle, ((WIDTH - subtitle.get_width()) // 2, 200))

    # Buttons with more spacing
    easy_btn = draw_button("EASY", 100, 350, 120, 60, ORANGE)
    medium_btn = draw_button("MEDIUM", 240, 350, 120, 60, ORANGE)
    hard_btn = draw_button("HARD", 380, 350, 120, 60, ORANGE)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_btn.collidepoint(event.pos):
                    return 30
                elif medium_btn.collidepoint(event.pos):
                    return 40
                elif hard_btn.collidepoint(event.pos):
                    return 50

# Game screen
def game_screen(difficulty):
    SCREEN.fill(WHITE)

    for i in range(10):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(SCREEN, BLACK, (50, 50 + i * 50), (500, 50 + i * 50), thickness)
        pygame.draw.line(SCREEN, BLACK, (50 + i * 50, 50), (50 + i * 50, 500), thickness)

    reset_btn = draw_button("RESET", 100, 550, 100, 50, ORANGE)
    restart_btn = draw_button("RESTART", 250, 550, 100, 50, ORANGE)
    exit_btn = draw_button("EXIT", 400, 550, 100, 50, ORANGE)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if reset_btn.collidepoint(event.pos):
                    print("Reset button pressed!")
                elif restart_btn.collidepoint(event.pos):
                    return "restart"
                elif exit_btn.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# End screen
def end_screen(win):
    SCREEN.fill(WHITE)

    if win:
        message = TITLE_FONT.render("Game Won!", True, BLACK)
        button_text = "EXIT"
    else:
        message = TITLE_FONT.render("Game Over :(", True, BLACK)
        button_text = "RESTART"

    SCREEN.blit(message, ((WIDTH - message.get_width()) // 2, 200))

    restart_btn = draw_button(button_text, 250, 350, 100, 50, ORANGE)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.collidepoint(event.pos):
                    if win:
                        pygame.quit()
                        sys.exit()
                    else:
                        return "restart"

# Main function to tie everything together
def main():
    while True:
        difficulty = start_screen()
        result = game_screen(difficulty)
        if result == "restart":
            continue
        win = True  # Replace with actual game state logic
        result = end_screen(win)
        if result == "restart":
            continue

if __name__ == "__main__":
    main()
