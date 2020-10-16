import pygame
pygame.init()

x=50
y=400
width=40
height=60
vel=5
scrWid=500
scrHei=500

isJump=False
jumpCountMax=10
jumpCount=jumpCountMax
left=False
   

win=pygame.display.set_mode((scrWid,scrHei))

pygame.display.set_caption("Firsst Game")


run=True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x< scrHei -width -vel:
        x+=vel
    if not(isJump):
        """
        if keys[pygame.K_UP] and y>vel:
            y-=vel
        if keys[pygame.K_DOWN] and y< scrWid -height -vel:
            y+=vel
        """
        if keys[pygame.K_SPACE] :
            isJump=True
    else:
        if jumpCount>=-jumpCountMax:
            neg=1
            if jumpCount< 0:
                neg=-1
            y-= (jumpCount **2) *0.2 *neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=jumpCountMax       
    
    win.fill((0,0,0))
    pygame.draw.rect(win,(0,255,0),(x,y,width,height))
    pygame.display.update()