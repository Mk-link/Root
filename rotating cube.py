import pygame
import sys
import math
import random
import os

# Pygame initialisieren
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Cube (3D Projection) mit Katzenbildern")

clock = pygame.time.Clock()

# 3D-Würfel-Eigenschaften
cube_size = 150
cube_color = (0, 128, 255)
center = [WIDTH // 2, HEIGHT // 2]

# 3D-Koordinaten der Würfelecken
cube_points = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
]

# Flächen des Würfels (jeweils vier Indizes in cube_points)
cube_faces = [
    (0, 1, 2, 3),  # hinten
    (4, 5, 6, 7),  # vorne
    (0, 1, 5, 4),  # unten
    (2, 3, 7, 6),  # oben
    (1, 2, 6, 5),  # rechts
    (0, 3, 7, 4)   # links
]

# Kanten des Würfels (jeweils zwei Indizes in cube_points)
cube_edges = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7)
]

# Rotationswinkel
angle_x = 0
angle_y = 0
angle_z = 0

# Neue Variablen für Drehrichtungsänderung
direction_timer = 0
direction_interval = 120  # Anzahl Frames bis zur nächsten Richtungsänderung (z.B. 2 Sekunden bei 60 FPS)
dx = random.uniform(-0.04, 0.04)
dy = random.uniform(-0.04, 0.04)
dz = random.uniform(-0.04, 0.04)

def rotate_point(point, ax, ay, az):
    x, y, z = point
    # Rotation um X-Achse
    cos_x = math.cos(ax)
    sin_x = math.sin(ax)
    y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x
    # Rotation um Y-Achse
    cos_y = math.cos(ay)
    sin_y = math.sin(ay)
    x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y
    # Rotation um Z-Achse
    cos_z = math.cos(az)
    sin_z = math.sin(az)
    x, y = x * cos_z - y * sin_z, x * sin_z + y * cos_z
    return [x, y, z]

def project_point(point):
    scale = cube_size
    distance = 4
    factor = scale / (distance - point[2])
    x = int(point[0] * factor + center[0])
    y = int(point[1] * factor + center[1])
    return (x, y)

def draw_cube(surface, points, edges, color):
    for edge in edges:
        p1 = project_point(points[edge[0]])
        p2 = project_point(points[edge[1]])
        pygame.draw.line(surface, color, p1, p2, 3)

# Haupt-Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drehrichtung nur alle direction_interval Frames ändern
    direction_timer += 1
    if direction_timer >= direction_interval:
        dx = random.uniform(-0.04, 0.04)
        dy = random.uniform(-0.04, 0.04)
        dz = random.uniform(-0.04, 0.04)
        direction_timer = 0

    # Rotationswinkel anpassen
    angle_x += dx
    angle_y += dy
    angle_z += dz

    # Rotierte Punkte berechnen
    rotated_points = [rotate_point(p, angle_x, angle_y, angle_z) for p in cube_points]

    screen.fill((30, 30, 30))
    draw_cube(screen, rotated_points, cube_edges, cube_color)

    pygame.display.flip()
    clock.tick(60)