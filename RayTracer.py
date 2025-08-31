import pygame
import random
from gl import *
from BMP_Writer import GenerateBMP
from model import Model
from OBJLoader import OBJ
from figures import *
from lights import *
from material import Material

width = 256
height = 256

screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

rend = Renderer(screen)

brick = Material(diffuse = [1, 0, 0])
grass = Material(diffuse = [0, 1, 0])


rend.scene.append(Sphere(position=[0, 0, -5], radius=1.5, material=brick))


rend.lights.append(AmbientLight())
rend.lights.append(DirectionalLight(direction = [-1, -1, -1]))

rend.glRender()

isRunning = True
while isRunning:
    deltaTime = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rend.camera.translation[0] += 0.1
            elif event.key == pygame.K_LEFT:
                rend.camera.translation[0] -= 0.1

            elif event.key == pygame.K_UP:
                rend.camera.translation[1] += 0.1
            elif event.key == pygame.K_DOWN:
                rend.camera.translation[1] -= 0.1


            elif event.key == pygame.K_q:
                rend.camera.translation[2] += 2 * deltaTime  
            elif event.key == pygame.K_e:
                rend.camera.translation[2] -= 2 * deltaTime


            elif event.key == pygame.K_a:
                rend.camera.rotation[1] -= 45 * deltaTime
            elif event.key == pygame.K_d:
                rend.camera.rotation[1] += 45 * deltaTime
            elif event.key == pygame.K_w:
                rend.camera.rotation[0] -= 45 * deltaTime
            elif event.key == pygame.K_s:
                rend.camera.rotation[0] += 45 * deltaTime
        

    

    #rend.glClearBackground()
    rend.glRender()
    pygame.display.flip()


GenerateBMP("output.bmp", width, height, 3, rend.frameBuffer)
pygame.quit()