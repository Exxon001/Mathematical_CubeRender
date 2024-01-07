import pygame
import sys
from math import sin, cos, tan


vertices = [(-1,-1,-1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1 , 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), ( 1, 5), (2, 6), (3, 7)]



width, height = 1550, 1000

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Something')

fov = 200
focal_length = width / 2 / tan(fov * 2)

running = True


o = 2
held = False
angle_y = 0
angle_x = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                held = False
        elif event.type == pygame.MOUSEWHEEL:
            if o == 1:
                o = 2
            else:
                o += event.y * 0.0001
        
    focal_length = width / 2 / tan(fov * o)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = pygame.mouse.get_rel()
    if held == True:
        angle_y += rel_x * 0.007
        angle_x += rel_y * -0.007
    rotated_cube_vertices = [(cos(angle_y) * x - sin(angle_y) * z,
                         sin(angle_x) * y + cos(angle_x) * (sin(angle_y) * x + cos(angle_y) * z),
                         cos(angle_x) * y - sin(angle_x) * (sin(angle_y) * x + cos(angle_y) * z)) for x, y, z in vertices]
    
    
    screen.fill((0, 0, 0))
    for edge in edges:
        for i in range(2):
            x1, y1, z1 = rotated_cube_vertices[edge[i]]
            x2, y2, z2 = rotated_cube_vertices[edge[(i + 1) %2]] 

            x1 = x1 / (z1 + 3) * focal_length + width / 2
            y1 = -y1 / (z1 + 3) * focal_length + height / 2 
            x2 = x2 / (z2 + 3) * focal_length + width / 2
            y2 = -y2 / (z2 + 3) * focal_length + height / 2

            pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2))
        
    
    pygame.display.flip()


pygame.quit()

sys.exit()



