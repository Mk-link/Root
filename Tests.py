import pygame
import sys
import math

# Pygame initialisieren
pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Square")


clock = pygame.time.Clock()

# Quadrat-Eigenschaften
square_size = 100
square_color = (0, 128, 255)
center = (WIDTH // 2, HEIGHT // 2)
new_var = 0
angle = new_var

def draw_rotating_square(surface, center, size, angle, color):
    # Eckpunkte des Quadrats berechnen (vor Rotation)
    half = size // 2
    points = [
        (-half, -half),
        (half, -half),
        (half, half),
        (-half, half)
    ]
    # Rotierte Eckpunkte berechnen
    rotated_points = []
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    for x, y in points:
        rx = x * cos_a - y * sin_a + center[0]
        ry = x * sin_a + y * cos_a + center[1]
        rotated_points.append((rx, ry))
    pygame.draw.polygon(surface, color, rotated_points)

# Haupt-Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))
    draw_rotating_square(screen, center, square_size, angle, square_color)
    angle = (angle + 2) % 360  # Winkel erhöhen

    pygame.display.flip()
    clock.tick(60)