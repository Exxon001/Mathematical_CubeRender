import pygame
import sys
from math import sin, cos, tan



vertices = [(-1,-1,-1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1 , 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]

faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
         (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)]

width, height = 1550, 1000

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Something')

fov = 200
focal_length = width / 2 / tan(fov * 2)

running = True


o = 2
held = True
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
    
    for face in faces:
        face_vertices = [rotated_cube_vertices[i] for i in face]
        face_projection = [(x / (z + 3) * focal_length + width / 2, -y / (z + 3) * focal_length + height / 2) for x, y, z in face_vertices]

        print(face_projection)
        pygame.draw.polygon(screen, (55, 55, 55), face_projection)
    
    pygame.display.flip()


pygame.quit()

sys.exit()

