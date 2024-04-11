from globals_vars import *
board_size = 16
cell_size = 50 * 16 / board_size
arr = [0]*board_size
for i in range(board_size):
    arr[i] = [0]*board_size
def draw_border(sc):
    pygame.draw.line(sc, WHITE, [GAP, GAP], [cell_size * board_size + GAP, GAP], 2)
    pygame.draw.line(sc, WHITE, [cell_size * board_size + GAP, GAP], [cell_size * board_size + GAP, cell_size * board_size + GAP], 2)
    pygame.draw.line(sc, WHITE, [cell_size * board_size + GAP, cell_size * board_size + GAP], [GAP, cell_size * board_size + GAP], 2)
    pygame.draw.line(sc, WHITE, [GAP, cell_size * board_size + GAP], [GAP, GAP], 2)


def draw_filled_board(sc):
    for row in range(board_size):
        for col in range(board_size):
            draw_full_cell(col,row,sc)
def draw_full_cell(row,col,sc):
    pygame.draw.rect(sc,WHITE,(row*cell_size+GAP,col*cell_size+GAP, cell_size,cell_size))
    pygame.draw.rect(sc,BLACK,(row*cell_size+1+GAP,col*cell_size+1+GAP,cell_size-2,cell_size-2))  
def draw_empty_cell(row,col,sc):
    remove_left_cell(row,col,sc)
    remove_right_cell(row,col,sc)
    remove_top_cell(row,col,sc)
    remove_bot_cell(row,col,sc)

def remove_right_cell(row,col,sc):
    pygame.draw.line(sc,BLACK,[row*cell_size+cell_size-1+GAP,col*cell_size+1+GAP],[row*cell_size+cell_size-1+GAP,col*cell_size+cell_size-1+GAP],2)
def remove_left_cell(row,col,sc):
    pygame.draw.line(sc,BLACK,[row*cell_size-1+GAP,col*cell_size+1+GAP],[row*cell_size-1+GAP,col*cell_size+cell_size-2+GAP],2)    
def remove_top_cell(row,col,sc):
    pygame.draw.line(sc,BLACK,[row*cell_size+1+GAP,col*cell_size-1+GAP],[row*cell_size+cell_size-2+GAP,col*cell_size+GAP-1],2)  
def remove_bot_cell(row,col,sc):
    pygame.draw.line(sc,BLACK,[row*cell_size+1+GAP,col*cell_size+cell_size-1+GAP],[row*cell_size+cell_size-2+GAP,col*cell_size+cell_size-1+GAP],2) 

# Алгоритм двоичного дерева
def bin_tree_NE(arr): 
    for i in range(board_size):
        for j in range(board_size):
            if i == 0:
                arr[i][j] = 3
            elif j == board_size-1:
                arr[i][j] = 4
            elif j != board_size-1 and i != 0:
                arr[i][j] = random.randint(3,4)
            
    return arr
def bin_tree_NW(arr):
    for i in range(board_size):
        for j in range(board_size):
            if i == 0:
                arr[i][j] = 2
            elif j == 0:
                arr[i][j] = 4
            elif j != 0 and i != 0:
                arr[i][j] = random.choice([2,4])
 
    return arr
def bin_tree_SW(arr):
    for i in range(board_size):
        for j in range(board_size):
            if i == board_size-1:
                arr[i][j] = 2
            elif j == 0:
                arr[i][j] = 5
            elif j != 0 and i != board_size-1:
                arr[i][j] = random.choice([2,5])
    return arr
def bin_tree_SE(arr): #3 5
    for i in range(board_size):
        for j in range(board_size):
            if i == board_size-1:
                arr[i][j] = 3
            elif j == board_size-1:
                arr[i][j] = 5
            elif i!= board_size-1 and j != board_size-1:
                arr[i][j] = random.choice([3,5])
    return arr
        

#отрисовка лабиринта двоичным деревом
#0 - залитая клетка
#1 - пустая
#2 - слева пустая
#3 - справа пустая
#4 - сверху пустая
#5 - снизу пустая
# NE  4 3
# NW  4 2
# SW  2 5 
# SE  3 5 
    

def draw_bin_tree(arg,sc):
    global arr
    arr = [0]*board_size
    for i in range(board_size):
        arr[i] = [0]*board_size 
    if arg == "SW":
        arr = bin_tree_SW(arr)
    elif arg == "NE":
        arr = bin_tree_NE(arr)
    elif arg == "NW":
        arr = bin_tree_NW(arr)
    elif arg == "SE":
        arr = bin_tree_SE(arr)
    draw_border(sc)
    for row in range(board_size):
        for col in range(board_size):
            if arr[row][col] == 0:
                draw_full_cell(col,row,sc)
            elif arr[row][col] == 0:    
                draw_empty_cell(col,row,sc)
            elif arr[row][col] == 2:    
                remove_left_cell(col,row,sc)
            elif arr[row][col] == 3:    
                remove_right_cell(col,row,sc)
            elif arr[row][col] == 4: 
                remove_top_cell(col,row,sc)
            elif arr[row][col] == 5:    
                remove_bot_cell(col,row,sc)
            clock.tick(10000)
            draw_border(sc)
            pygame.display.flip()

def BT(arg):
    redraw_btn_text = font.render("Regenerate", True, TEXT_COLOR)
    menu_btn_text = font.render("Menu", True, TEXT_COLOR)
    global board_size, cell_size
    is_working = True
    screen_BT = pygame.display.set_mode((width, height))

    screen_BT.fill(BLACK)
    btn_regenerate_x = 16 * 50 + 70
    btn_regenerate_y = 14 * 50
    btn_menu_x = btn_regenerate_x + Button_Size_W + 170
    btn_menu_y = 50

    # Пересчитываем размер клеток
    if board_size != 0:
        cell_size = 50 * 16 // board_size

    input_box = pygame.Rect(btn_regenerate_x + Button_Size_W + 50, btn_regenerate_y, Button_Size_W // 1.5 - 30, Button_Size_H)
    color_inactive = (100, 0, 0)
    color_active = (255, 0, 0)
    color = color_inactive
    text = str(board_size)
    active = False

    txt_surface = font.render(text, True, color)
    btn_menu_width = Button_Size_W // 2
    pygame.draw.rect(screen_BT, color1, (btn_menu_x, btn_menu_y, btn_menu_width, Button_Size_H), width=3)
    screen_BT.blit(menu_btn_text, (btn_menu_x + 45, btn_menu_y + 30))

    pygame.draw.rect(screen_BT, color1, (btn_regenerate_x, btn_regenerate_y, Button_Size_W, Button_Size_H), width=3)
    screen_BT.blit(redraw_btn_text, (btn_regenerate_x + 70, btn_regenerate_y + 30))
    width_txt = font.render("Size: ", True, color)
    screen_BT.blit(txt_surface, (input_box.x + 145, input_box.y + 30))
    pygame.draw.rect(screen_BT, color, input_box, 2)
    screen_BT.blit(width_txt, (input_box.x + 15, input_box.y + 30))

    pygame.display.flip()
    draw_filled_board(screen_BT)
    draw_bin_tree(arg, screen_BT)
    pygame.display.flip()
    while is_working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_working = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= btn_regenerate_x and mouse[0] <= btn_regenerate_x + Button_Size_W and \
                        mouse[1] >= btn_regenerate_y and mouse[1] <= btn_regenerate_y + Button_Size_H:
                    is_working = False
                    board_size = int(text)
                    return BT(arg)
                if mouse[0] >= btn_menu_x and mouse[0] <= btn_menu_x + Button_Size_W and \
                        mouse[1] >= btn_menu_y and mouse[1] <= btn_menu_y + Button_Size_H:
                    board_size = int(text)
                    return Menu()
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        pygame.draw.rect(screen_BT, BLACK, (input_box.x, input_box.y, Button_Size_W, Button_Size_H))
                    else:
                        if len(text) != 2:
                            char = event.unicode
                            if str(char).isdigit():
                                pygame.draw.rect(screen_BT, BLACK, (input_box.x, input_box.y, Button_Size_W, Button_Size_H))
                                text += event.unicode
            txt_surface = font.render(text, True, color)
            width_txt = font.render("Size: ", True, color)
            screen_BT.blit(txt_surface, (input_box.x + 145, input_box.y + 30))
            screen_BT.blit(width_txt, (input_box.x + 15, input_box.y + 30))
            pygame.draw.rect(screen_BT, color, input_box, 2)
            pygame.display.flip()
            # print(board_size)

                
def dirChose():

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
    b_x = width//2 - b_w//2
    text_x = b_x+b_w//5
    sw = font.render("Southwest",True,TEXT_COLOR)
    se = font.render("Southeast",True,TEXT_COLOR)
    nw = font.render("Northwest",True,TEXT_COLOR)
    ne = font.render("Northeast",True,TEXT_COLOR)
    info = font2.render("Choose Type Of Binary Tree Maze",True,TEXT_COLOR)
    is_working = True
    screen = pygame.display.set_mode((width, height))
    screen.fill(BLACK)

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

        screen.blit(info,(width//5,100))
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
    bin_tree_text = font.render("  Binary Tree",True,TEXT_COLOR)
    euler_text = font.render("Euler Algorithm",True,TEXT_COLOR)

    button1_color = color1
    Button1_Y = 150
    button2_color = color1
    Button2_Y = 300
    Button_X = width//2 - Button_Size_W//2
    is_working = True
    screen = pygame.display.set_mode((width, height))
    screen.fill(BLACK)
    while(is_working):
        for event in pygame.event.get():
            pygame.draw.rect(screen,button1_color,(Button_X,Button1_Y,Button_Size_W,Button_Size_H),border_radius=5)
            screen.blit(bin_tree_text,(Button_X+20,Button1_Y+30))

            pygame.draw.rect(screen,button2_color,(Button_X,Button2_Y,Button_Size_W,Button_Size_H),border_radius=5)
            screen.blit(euler_text,(Button_X+20,Button2_Y+30))

            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                is_working = False
            if mouse[0] >= Button_X and mouse[0] <= Button_X+Button_Size_W and mouse[1]>= Button1_Y and mouse[1]<=Button1_Y+Button_Size_H:
                button1_color = color1
            else:
                button1_color = color2
            if mouse[0] >= Button_X and mouse[0] <= Button_X+Button_Size_W and mouse[1]>= Button2_Y and mouse[1]<=Button2_Y+Button_Size_H:
                button2_color = color1
            else:
                button2_color = color2
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= Button_X and mouse[0] <= Button_X+Button_Size_W and mouse[1]>= Button1_Y and mouse[1]<=Button1_Y+Button_Size_H:
                    is_working = False
                    return dirChose()
        pygame.display.flip()

