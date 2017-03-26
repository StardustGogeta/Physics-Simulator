import pygame,sys,os
from pygame import *
from pygame.locals import *
from Colors import *
from math import hypot

# Gravitational constant
global G
G = 3

from Body import *


def display(screen,bodies):
    screen.fill(white)
    for body in bodies:
        pygame.draw.ellipse(screen,body.color,body.get_rect())
    screen.blit(tick_text,(s_width-70,0))
    pygame.display.update()

def shift_camera(bodies,x,y):
    for body in bodies:
        body.pos = (body.pos[0]-x,body.pos[1]-y)

def physics(bodies):
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    #start pygame window and init screen
    pygame.init()
    global s_width,s_height
    s_width = 1000
    s_height = 600
    screen = pygame.display.set_mode((s_width,s_height))
    pygame.display.set_caption('Physics Simulator')

    #fonts
    monospace = pygame.font.SysFont("monospace",15)


    #init camera vars
    x_shift = 0
    y_shift = 0
    shift_factor = 15


    #set up clock
    clock = pygame.time.Clock()
    tick = 60
    global tick_text
    tick_text = monospace.render(str(tick) + "fps",1,black)
    
    done = False
    while not done:
        clock.tick(tick)

        # User input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    tick += 1
                    tick_text = monospace.render(str(tick) + "fps",1,black)
                if event.button == 5 and tick > 1:
                    tick -= 1
                    tick_text = monospace.render(str(tick) + "fps",1,black)
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    y_shift = -1
                elif event.key == K_DOWN:
                    y_shift = 1
                elif event.key == K_LEFT:
                    x_shift = -1
                elif event.key == K_RIGHT:
                    x_shift = 1
            elif event.type == KEYUP:
                if event.key == K_UP:
                    y_shift = 0
                elif event.key == K_DOWN:
                    y_shift = 0
                elif event.key == K_LEFT:
                    x_shift = 0
                elif event.key == K_RIGHT:
                    x_shift = 0

        shift_camera(bodies,shift_factor*x_shift,shift_factor*y_shift)


        # Physics engine
        for body in bodies:
            GM = G*body.mass
            for body_1 in bodies:
                if body_1 != body:
                    # Check collisions
                    if body.get_rect().collidepoint(body_1.pos) and body.collision and body_1.collision:
                        print(str(len(bodies)-1)+" bodies remaining")
                        rel = float(body.mass)/(body.mass+body_1.mass)
                        pos = ((body.pos[0]*rel+body_1.pos[0]*(1-rel)),(body.pos[1]*rel+body_1.pos[1]*(1-rel)))
                        x_vect = (body.get_mom()[0]+body_1.get_mom()[0])/(body.mass+body_1.mass)
                        y_vect = (body.get_mom()[1]+body_1.get_mom()[1])/(body.mass+body_1.mass)
                        vect = (x_vect,y_vect)
                        color = ((body.color[0]*rel+body_1.color[0]*(1-rel)),(body.color[1]*rel+body_1.color[1]*(1-rel)),(body.color[2]*(1-rel)+body_1.color[2]*(1-rel)))
                        if max(color) > 255: color = (255,255,255)
                        bodies.remove(body)
                        bodies.remove(body_1)
                        bodies.append(Body(body.mass+body_1.mass,pos,vect,color))
                        break
                        
                    # Gravity
                    x = body_1.pos[0]-body.pos[0]
                    y = body_1.pos[1]-body.pos[1]
                    acc = -GM/hypot(x,y)**3
                    x_acc = acc * x
                    y_acc = acc * y
                    body_1.vect = (body_1.vect[0]+x_acc,body_1.vect[1]+y_acc)
        
            # Apply motion
            body.pos = (body.pos[0]+body.vect[0],body.pos[1]+body.vect[1])

        #display room
        display(screen,bodies)

    pygame.quit()
    quit()
    sys.exit(0)




