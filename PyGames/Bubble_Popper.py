import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Popper")

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Bubble class
class Bubble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.max_radius = 50
        self.growth_rate = (self.max_radius - self.radius) / 3  # Grow to max size in 3 seconds

    def grow(self, dt):
        self.radius += self.growth_rate * dt
        return self.radius >= self.max_radius

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), int(self.radius))

    def is_clicked(self, pos):
        return ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) <= self.radius ** 2

# Game variables
bubbles = []
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
clock = pygame.time.Clock()
bubble_spawn_timer = 0
running = True

while running:
    dt = clock.tick(60) / 1000.0  # Delta time in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for bubble in bubbles[:]:
                if bubble.is_clicked(event.pos):
                    bubbles.remove(bubble)
                    score += 1

    # Spawn new bubbles
    bubble_spawn_timer += dt
    if bubble_spawn_timer >= 0.3:
        bubble_spawn_timer = 0
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        bubbles.append(Bubble(x, y))

    # Update and draw bubbles
    screen.fill(WHITE)
    for bubble in bubbles[:]:
        if bubble.grow(dt):
            bubbles.remove(bubble)
        bubble.draw()

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()