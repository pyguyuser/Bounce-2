import pygame,time 

class Player:

    def __init__(self,disp,stand_coords,color="red"):   
        self.screen = disp
        self.color = color

        self.sc = stand_coords
        self.x,self.y = self.sc

        self.t0 = time.time() 

        self.m = 1
        self.g = 1000

        self.v1 = 0
        self.vx = 0
        self.vmax = 0.01

        self.dx=0
        self.dx_max = 10**-2
        self.dt = 0.01

        self.k=10

        self.f1 = self.m*self.g
        self.f2=0
        self.f3=0
    
    @property
    def coords(self):
        return (self.x,self.y,self.dx)
    
    @coords.setter
    def coords(self,new_coords):
        self.x,self.y = new_coords
    
    def update(self):                          
        self.f3=0
        self.f2 = 0
 
        if self.y>=self.sc[1]:
            self.f2 = -self.f1
            self.f3 = -self.k*(self.y-self.sc[1])
            self.v1*=-0.5

        self.f=self.f1+self.f2+self.f3
        v2 = self.v1 +(self.f/self.m)*self.dt
        
        self.dy = int(v2)*self.dt
        self.dx = self.vx*self.dt 
        self.y+=self.dy
        self.x+=self.dx
        
        pygame.draw.circle(self.screen,self.color, (self.x, self.y), 25)

        self.v1=int(v2)