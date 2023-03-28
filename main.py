import pygame,time

W,H = (750,500)
disp = pygame.display.set_mode((W,H))

# sw,sh = (100,100)
sw,sh = (10,10)
x,y = (200,100)
fps = 60

g = 10
m = 1
t0 = time.time()
years = t0/(24*3600*365)

v0 = 0
t1 = 0
run = True
f0 = 0
f1 = m*g
f2=0
k=100
dx=0
jump = False
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            SPEED = 1

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                dx = -5
            elif i.key == pygame.K_RIGHT:
                dx = 5
            
            if i.key == pygame.K_SPACE:
                v0 = v0-2000
                # f2 = f2-1
                # jump = True
        elif i.type == pygame.KEYUP:
            dx = 0
            
            


    t2 = time.time() - t0
    dt = t2-t1
    # v = v0 + 0.5*g*(t2**2)
    # p=m*v

    # dy = v*dt
    # dx=1

    # y+=dy
    # x+=dx

    f = f0+f1+f2
    # f1 = -dl * 11
    a = f/m
    v = v0 + 0.5*a*(t2**2)

    dy = v*dt

    y+=dy
    x+=dx
    if y>400:
        # v0-=v0*0.7
        dl = min(y-400,0)
        v = 0 - v*0.9
        f0 = -f1
        f2 = -k*dl*100
  
    else:
        f0 = 0
        f2=0

    disp.fill("black")
    pygame.draw.circle(disp,(200,0,0),(x,y),20)


    pygame.display.update()
    pygame.time.Clock().tick(fps)
    t1 = t2
    v0 = v

pygame.quit()