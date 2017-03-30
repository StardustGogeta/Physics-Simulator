#All classes and functions assosciated with bodies
from random import randint, uniform, choice
from pygame import Rect
from Physics import G
from math import sin, cos, pi

class Body():
    def __init__(self,mass,pos,vect,color,rad=-1,collision=True,density=5):
        self.mass = mass
        self.pos = pos
        self.vect = vect
        self.color = color
        if rad == -1:
            #body size scaling (2 => 2D (area); 3 => 3D (volume))    
            D = 3
            self.rad = mass**(1.0/D)*density
        else:
            self.rad = rad
        self.collision = collision
        
    def get_rect(self):
        return Rect(self.pos[0]-self.rad,self.pos[1]-self.rad,self.rad*2,self.rad*2)

    def get_mom(self):
        return (self.mass*self.vect[0],self.mass*self.vect[1])




def rand_bodies(num,minmass,maxmass,minvel,maxvel,collide=True):
    bodies = []
    for i in range(num):
        mass = randint(minmass,maxmass)
        x = randint(0,s_width)
        y = randint(0,s_height)
        x_vect = uniform(minvel,maxvel)
        y_vect = uniform(minvel,maxvel)
        color = (randint(0,255),randint(0,255),randint(0,255))
        bodies.append(Body(mass,(x,y),(x_vect,y_vect),color,-1,collide))
    return bodies

def star_sys(star_mass,planets,minmass,maxmass,mindist,maxdist,circular=True):
    bodies = [Body(star_mass,(1000/2,600/2),(0,0),(255,255,0),-1,True)]
    GM = G*star_mass
    for i in range(planets):
        mass = randint(minmass,maxmass)
        r = randint(mindist,maxdist)
        theta = uniform(0,2*pi)
        pos = (1000/2+r*cos(theta),600/2+r*sin(theta))
        if circular:
            ratio = (GM/r)**0.5
            y_vect = ratio*cos(theta)
            x_vect = ratio*sin(theta)
            vect = (x_vect,y_vect)
        else:
            vect = (choice([-1,1])*uniform(0.5,1.5),choice([-1,1])*uniform(0.5,1.5))
        color = (randint(0,255),randint(0,255),randint(0,255))
        bodies.append(Body(mass,pos,vect,color,-1,True))
    return bodies



