import pygame
import sys
from math import sin, cos, pi, sqrt, tan

width, height = 800, 600

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('3D Sphere Renderer')

def generate_sphere(radius, num_segments):
    vertices = []
    for i in range(num_segments + 1):
        phi = 2 * pi * i / num_segments
        for j in range(num_segments // 2 + 1): 
            theta = pi * j / (num_segments // 2)
            x = radius * sin(theta) * cos(phi)
            y = radius * sin(theta) * sin(phi)
            z = radius * cos(theta)
            vertices.extend([(x, y, z), (x, -y, z)])
    return vertices

def generate_sphere_indices(num_segments):
    indices = []
    for i in range(num_segments):
        for j in range(num_segments // 2):
            p1 = i * (num_segments // 2 + 1) + j
            p2 = p1 + 1
            p3 = (i + 1) * (num_segments // 2 + 1) + j
            p4 = p3 + 1
            indices.extend([p1, p2, p3, p2, p4, p3])
    return indices

running = True

radius = 0.3
num_segments = 50

vertices = generate_sphere(radius, num_segments)
indices = generate_sphere_indices(num_segments)

o = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    for index in indices:
        x, y, z = vertices[index]

        # Apply perspective projection
        if z + radius != 0:
            # Apply perspective projection
            focal_length = width / o / tan(pi / 4)
            x = x / (z + radius) * focal_length + width / 2
            y = -y / (z + radius) * focal_length + height / 2

            pygame.draw.polygon(screen, (255, 255, 255), (int(x), int(y)), o)
    o += 1
    if o == 100:
        o = 1

    pygame.display.flip()

pygame.quit()
sys.exit()