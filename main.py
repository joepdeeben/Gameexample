import pygame
from math import *
import numpy as np
import keyboard
pygame.init()


x2 = 0
y2 = 0
WIDTH = 1280
HEIGHT = 960

fov_v = np.pi/4
fov_h = fov_v* HEIGHT/WIDTH
nearfrustum = 0.1
farfrustum = 100




screen = pygame.display.set_mode((WIDTH, HEIGHT))

white = (255,255,255)
black = (0,0,0)


scale = 100
circle_pos = [WIDTH/ 2, HEIGHT/ 2]
points = []
for x in (-1, 1):
    for y in (-1, 1):
        for z in (-1, 1):
            points.append(np.matrix([x, y, z]))

print(points)

trans = np.matrix([[1, 0, 0], [0, 1, 0], [0,0,0]])


print(trans)
angle = 0
angley = 0



run = True


clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if keyboard.is_pressed('up arrow'):
        for x, y  in enumerate(points):
           points[x] = np.dot(y, 1.1)
    elif keyboard.is_pressed('down arrow'):
        for x, y  in enumerate(points):
           points[x] = np.dot(y, 0.9)

    if keyboard.is_pressed('a'):
        angley += 0.1
    elif keyboard.is_pressed('d'):
        angley += -0.1
    if keyboard.is_pressed('w'):
        angle += 0.1
    elif keyboard.is_pressed('s'):
        angle += -0.1
    if keyboard.is_pressed('r'):
        angley = 0
        angle = 0

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]

    ])

    rotation_y = np.matrix([
        [cos(angley), 0, sin(angley)],
        [0, 1, 0],
        [-sin(angley), 0, cos(angley)]

    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]

    ])

    print(angle)
    screen.fill(white)
    for x in points:
        pointrot = np.dot(x, rotation_y)
        pointrot = np.dot(pointrot, rotation_x)
        point = np.dot(pointrot, trans)
        x = int(point[0, 0] * scale) + circle_pos[0]
        y = int(point[0, 1] * scale) + circle_pos[1]
        pygame.draw.circle(screen, black, (x, y), 5)
        if x2 > 0:
           pygame.draw.line(screen, black, (x, y), (x2, y2))
        else:
            pass
        x2 = int(point[0, 0] * scale) + circle_pos[0]
        y2 = int(point[0, 1] * scale) + circle_pos[1]
    pygame.display.update()

