from globals import *
from bin_tree import *
font = pygame.font.SysFont('Arial',35)
font2 = pygame.font.SysFont("timesnewroman",60)
text_x = 16*50/2-100
color1 = (72, 168, 181)
color2 = (72, 120, 181)
def BT(arg):
    
    is_working = True
    screen = pygame.display.set_mode((width, height))
    screen.fill(WHITE)
    pygame.draw.rect(screen, (255, 0, 0), (board_size * cell_size + GAP, 0, 50, 51))
    pygame.draw.line(screen, (WHITE), [board_size * cell_size + GAP + 5, 5], [board_size * cell_size + GAP + 45, 45], 3)
    pygame.draw.line(screen, (WHITE), [board_size * cell_size + GAP + 5, 45], [board_size * cell_size + GAP + 45, 5], 3)
    pygame.draw.rect(screen, (35, 140, 72), (board_size * cell_size, 0, 50, 50))
    i = font2.render("i", True, WHITE)
    screen.blit(i, (board_size * cell_size + 18, -8))
    draw_filled_board()
    draw_bin_tree(arg)

    pygame.display.flip()

    while is_working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_working = False
                return Menu()  # Возвращаемся в меню при закрытии окна
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= board_size * cell_size + GAP and mouse[0] <= board_size * cell_size + GAP + GAP and \
                        mouse[1] >= 0 and mouse[1] <= 50:
                    is_working = False
                    return Menu()
                    
def dirChose():
    b_x = text_x-text_x//4

    b1_color = color1
    b1_y = 300
    b_w = 325
    b_h = 75

    b2_color = color1
    b2_y = 400

    b3_color = color1
    b3_y = 500

    b4_color = color1
    b4_y = 600

    sw = font.render("Southwest",True,BLACK)
    se = font.render("Southeast",True,BLACK)
    nw = font.render("Northwest",True,BLACK)
    ne = font.render("Northeast",True,BLACK)
    info = font.render("Выберите тип лабиринта Двоичное дерево",True,BLACK)
    is_working = True
    screen = pygame.display.set_mode((800,800))
    screen.fill(WHITE)

    pygame.display.flip()
    while(is_working):
        pygame.draw.rect(screen,b1_color,(b_x,b1_y,b_w,b_h),border_radius=5)
        screen.blit(sw,(text_x,320))
    
        pygame.draw.rect(screen,b2_color,(b_x,b2_y,b_w,b_h),border_radius=5)
        screen.blit(se,(text_x,420))

        pygame.draw.rect(screen,b3_color,(b_x,b3_y,b_w,b_h),border_radius=5)
        screen.blit(nw,(text_x,520))

        pygame.draw.rect(screen,b4_color,(b_x,b4_y,b_w,b_h),border_radius=5)
        screen.blit(ne,(text_x,620))

        screen.blit(info,(65,100))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                is_working = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= b_x and mouse[0] <= b_x+b_w and mouse[1]>= b1_y and mouse[1]<=b1_y+b_h:
                    is_working = False
                    return BT("SW")
                if mouse[0] >= b_x and mouse[0] <= b_x+b_w and mouse[1]>= b2_y and mouse[1]<=b2_y+b_h:
                    is_working = False
                    return BT("SE")
                if mouse[0] >= b_x and mouse[0] <= b_x+b_w and mouse[1]>= b3_y and mouse[1]<=b3_y+b_h:
                    is_working = False
                    return BT("NW")
                if mouse[0] >= b_x and mouse[0] <= b_x+b_w and mouse[1]>= b4_y and mouse[1]<=b4_y+b_h:
                    is_working = False
                    return BT("NE")
            if mouse[0] >= b_x and mouse[0] <= b_x+b_w and mouse[1]>= b1_y and mouse[1]<=b1_y+b_h:
                b1_color = color1
            else:
                b1_color = color2
            if mouse[0] >= b_x and mouse[0] <= b_x+b_w and mouse[1]>= b2_y and mouse[1]<=b2_y+b_h:
                b2_color = color1
            else:
                b2_color = color2
            if mouse[0] >= b_x and mouse[0] <= b_x+b_w and mouse[1]>= b3_y and mouse[1]<=b3_y+b_h:
                b3_color = color1
            else:
                b3_color = color2
            if mouse[0] >= b_x and mouse[0] <= b_x+b_w and mouse[1]>= b4_y and mouse[1]<=b4_y+b_h:
                b4_color = color1
            else:
                b4_color = color2
        pygame.display.flip()
def Menu():
    hw = font.render("Бинарное дерево",True,BLACK)
    Button1_X = 250
    Button1_Y = 200
    Button1_Size_W = 350
    Button1_Size_H = 100
    button_color = color1
    is_working = True
    screen = pygame.display.set_mode((800,800))
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
                    is_working = False
                    return dirChose()
        pygame.display.flip()
