import pygame

pygame.init()

wTop = 0
wLeft = 0
wRight = 300
wBottom = 300


rectX = 100
rectY = 100
rectWidth = 100
rectHeight = 100

dx = 20
dy = 20

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
screen = pygame.display.set_mode((wRight,wBottom))


breakFlag = True
while(breakFlag):
    prevX = rectX
    prevY = rectY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            breakFlag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and rectX-dx >= wLeft:
                rectX-= dx
            elif event.key == pygame.K_RIGHT and rectX + rectWidth + dx <=wRight:
                rectX += dx
            elif event.key == pygame.K_UP and rectY - dy >= wTop:
                rectY -= dy
            elif event.key == pygame.K_DOWN and rectY + rectHeight + dy <= wBottom:
                rectY += dy
        
        pygame.draw.rect(screen,BLACK,(prevX,prevY,rectWidth,rectHeight))
        screen.fill(GREEN)
        pygame.draw.rect(screen,RED,(rectX,rectY,rectWidth,rectHeight))
    pygame.display.flip()
    
