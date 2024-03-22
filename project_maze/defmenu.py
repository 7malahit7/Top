from globals import *
from bin_tree import *
font = pygame.font.SysFont('Arial',35)
hw = font.render("Бинарное дерево",False,BLACK)
Button1_X = 250
Button1_Y = 200
Button1_Size_W = 350
Button1_Size_H = 100

def BT():
    is_working = True
    screen = pygame.display.set_mode((width,height))
    screen.fill(WHITE)
    draw_filled_board()
    draw_bin_tree("SE")
    draw_border()  
    pygame.display.flip()
    while(is_working):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_working = False
            
def Menu():
    button_color = (72, 168, 181)
    color1 = (72, 168, 181)
    color2 = (72, 120, 181)
    is_working = True
    screen = pygame.display.set_mode((800,1000))
    screen.fill(WHITE)
    while(is_working):
        for event in pygame.event.get():
            pygame.draw.rect(screen,button_color,(Button1_X,Button1_Y,Button1_Size_W,Button1_Size_H),border_radius=5)
            screen.blit(hw,(290,230))
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                is_working = False
            if mouse[0] >= Button1_X and mouse[0] <= Button1_X+Button1_Size_W and mouse[1]>= Button1_Y and mouse[1]<=Button1_Y+Button1_Size_H:
                button_color = color1
            else:
                button_color = color2
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= Button1_X and mouse[0] <= Button1_X+Button1_Size_W and mouse[1]>= Button1_Y and mouse[1]<=Button1_Y+Button1_Size_H:
                    BT()
                    pygame.display.flip()
                    is_working = False
        pygame.display.flip()
