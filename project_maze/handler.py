from globals_vars import *
board_size = 16
cell_size = 50 * 16 / board_size
arr_right = []
arr_bot = []
#обводка лабиринта
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
def remove_right_cell(row,col,sc):
    pygame.draw.line(sc,BLACK,[row*cell_size+cell_size-1+GAP,col*cell_size+1+GAP],[row*cell_size+cell_size-1+GAP,col*cell_size+cell_size-2+GAP],2)
def remove_bot_cell(row,col,sc):
    pygame.draw.line(sc,BLACK,[row*cell_size+1+GAP,col*cell_size+cell_size-1+GAP],[row*cell_size+cell_size-2+GAP,col*cell_size+cell_size-1+GAP],2) 

# Алгоритмы двоичного дерева с разным смещением

# Пример генерации лабиринта двоичным деревом
# С Северо-Восточным смещением
def bin_tree_NE(right, bot): 
    for i in range(board_size):
        for j in range(board_size):
            if i == 0:
                right[i][j] = 0
            elif j == board_size - 1:
                bot[i-1][j] = 0
            else:
                dir = random.randint(0, 1)
                if dir:
                    right[i][j] = 0
                else:
                    bot[i-1][j] = 0
    return right, bot

def bin_tree_NW(right, bot):
    for i in range(board_size):
        for j in range(board_size):
            if i == 0:
                right[i][j-1] = 0
            if j == 0:
                bot[i-1][j] = 0
            if j != 0 and i != 0:
                r = random.randint(0, 1)
                if r:
                    right[i][j-1] = 0
                else:
                    bot[i-1][j] = 0
    return right, bot

def bin_tree_SW(right, bot):
    for i in range(board_size):
        for j in range(board_size):
            if i == board_size - 1:
                right[i][j-1] = 0
            if j == 0:
                bot[i][j] = 0
            if j != 0 and i != board_size - 1:
                r = random.randint(0, 1)
                if r:
                    right[i][j-1] = 0
                else:
                    bot[i][j] = 0
    return right, bot

def bin_tree_SE(right, bot):
    for i in range(board_size):
        for j in range(board_size):
            if i == board_size - 1:
                right[i][j] = 0
            if j == board_size - 1:
                bot[i][j] = 0
            if i != board_size - 1 and j != board_size - 1:
                r = random.randint(0, 1)
                if r:
                    right[i][j] = 0
                else:
                    bot[i][j] = 0
    return right, bot



#отрисовка лабиринта
def draw_bin_tree(arg,sc):

    global arr_right
    arr_right = [1]*board_size
    for i in range(board_size):
        arr_right[i] = [1]*board_size 

    global arr_bot
    arr_bot = [1]*board_size
    for i in range(board_size):
        arr_bot[i] = [1]*board_size 



    if arg == "SW":
        arr_right,arr_bot = bin_tree_SW(arr_right,arr_bot)
    elif arg == "NE":
        arr_right,arr_bot = bin_tree_NE(arr_right,arr_bot)
    elif arg == "NW":
        arr_right,arr_bot = bin_tree_NW(arr_right,arr_bot)
    elif arg == "SE":
        arr_right,arr_bot = bin_tree_SE(arr_right,arr_bot)
    draw_border(sc)
    for i in range(board_size):
        arr_right[i][board_size-1] = 1
        arr_bot[board_size-1][i] = 1
    for row in range(board_size):
        for col in range(board_size):  
            if arr_bot[row][col] == 0: 
                remove_bot_cell(col,row,sc)
            if arr_right[row][col] == 0:    
                remove_right_cell(col,row,sc)

            clock.tick(1000000)
            draw_border(sc)
            pygame.display.flip()
#экран двоичного дерева
def BT(arg):
    redraw_btn_text = font.render("Regenerate", True, TEXT_COLOR)
    info_BT_text = [['Самый простой в понимании и реализации алгоритм, Двоичное'],
    [' дерево.'],
    [''],
    ['Имеет два побочных эффекта:'],
    ['  1) Лабиринты обладают сильным диагональным смещением'],
    ['    и отсутствием тупиков в его направлении.'],
    ['  2) Два пустых коридора по сторонам лабиринта. Когда'],
    ['    алгоритм «прокапывается» до конца строки/столбца,'],
    ['    ему не остается выбора, кроме как продолжить путь'],
    ['    в одном единственном направлении, создавая'],
    ['    пустые «границы».'],
    [' '],
    ['Сам алгоритм: '],
    ['  1)  Выбрать начальную клетку;'],
    ['  2)  Выбрать случайное направление для прокладывания пути.'],
    ['     Если соседняя клетка в этом направлении выходит за'],
    ['     границы поля, прокопать клетку в единственно возможном'],
    ['     направлении;'],
    ['  3)  Перейти к следующей клетке;'],
    ['  4)  Повторять 2-3 до тех пор, пока не будут обработаны'],
    ['     все клетки;']]
 
    global board_size, cell_size
    is_working = True
    screen_BT = pygame.display.set_mode((width, height))

    screen_BT.fill(BLACK)

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
    pygame.draw.rect(screen_BT, color1, (btn_menu_x, btn_menu_y, btn_menu_width, Button_Size_H), width=3)
    screen_BT.blit(menu_btn_text, (btn_menu_x + 45, btn_menu_y + 30))

    pygame.draw.rect(screen_BT, color1, (btn_regenerate_x, btn_regenerate_y, Button_Size_W, Button_Size_H), width=3)
    screen_BT.blit(redraw_btn_text, (btn_regenerate_x + 70, btn_regenerate_y + 30))
    width_txt = font.render("Size: ", True, color)
    screen_BT.blit(txt_surface, (input_box.x + 145, input_box.y + 30))
    pygame.draw.rect(screen_BT, color, input_box, 2)
    screen_BT.blit(width_txt, (input_box.x + 15, input_box.y + 30))
    for i in range(len(info_BT_text)):
        t = str(info_BT_text[i])[2:-2:]
        txt = info_font.render(t,True,TEXT_COLOR)
        screen_BT.blit(txt,(880,200+i*20))
    pygame.display.flip()
    draw_filled_board(screen_BT)
    draw_bin_tree(arg, screen_BT)
    pygame.display.flip()
    while is_working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Нижние стенки")
                for i in range(len(arr_bot)):
                    print(arr_bot[i])
                print("\nПравые стенки")
                for i in range(len(arr_right)):
                    print(arr_right[i])
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

#выбор смщенеия               
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
#экран меню
def Menu():
    bin_tree_text = font.render("  Binary Tree",True,TEXT_COLOR)
    euler_text = font.render(" Lee Algorithm",True,TEXT_COLOR)

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
                elif mouse[0] >= Button_X and mouse[0] <= Button_X+Button_Size_W and mouse[1]>= Button2_Y and mouse[1]<=Button2_Y+Button_Size_H:
                    return Lee_Alg()
        pygame.display.flip()
# Импорты и глобальные переменные

def Lee_Alg():
    redraw_btn_text = font.render(" Restart", True, TEXT_COLOR)
    info_Lee_Alg = [['Алгоритм Ли, также известный как волновой алгоритм,'],
 ['для поиска кратчайшего пути в лабиринте.'],
['Пользователю предоставляется возможность выбрать'],
 ['начальную и конечную точки на экране.'],
['Алгоритм работает на основе принципа распространения волны:'],
 ['начиная с начальной точки, он распространяет "волну" по '],
 ['соседним клеткам до тех пор, пока не достигнет конечной'],
['точки.'],
[''],
['Основные шаги алгоритма:'],
['1) Установка начальной клетки и конечной клетки.'],
['2) Распространение "волны" от начальной клетки до конечной'],
['клетки, помечая каждую посещённую клетку числом - расстоянием'],
['от начальной клетки.'],
['3)Построение кратчайшего пути, начиная от конечной клетки'],
[' и двигаясь к начальной, по числам, уменьшая их.']]

    screen_Lee = pygame.display.set_mode((width, height))
    draw_filled_board(screen_Lee)
    for i in range(len(info_Lee_Alg)):
        t = str(info_Lee_Alg[i])[2:-2:]
        txt = info_font.render(t,True,TEXT_COLOR)
        screen_Lee.blit(txt,(880,300+i*20))
    screen_Lee.blit(redraw_btn_text, (btn_regenerate_x + 70, btn_regenerate_y + 30))
    global arr_right, arr_bot
    arr_right = [1]*board_size
    for i in range(board_size):
        arr_right[i] = [1]*board_size 
    arr_bot = [1]*board_size
    for i in range(board_size):
        arr_bot[i] = [1]*board_size 
    arr_right,arr_bot = bin_tree_NE(arr_right,arr_bot)  
    pygame.draw.rect(screen_Lee, color1, (btn_regenerate_x, btn_regenerate_y, Button_Size_W, Button_Size_H), width=3)
    for i in range(board_size):
        arr_right[i][board_size-1] = 1
        arr_bot[board_size-1][i] = 1
    screen_Lee.blit(menu_btn_text, (btn_menu_x + 45, btn_menu_y + 30))
    draw_bin_tree("NW",screen_Lee)
    pygame.draw.rect(screen_Lee, color1, (btn_menu_x, btn_menu_y, btn_menu_width, Button_Size_H), width=3)
    start = set_pos(screen_Lee,True) 
    end = set_pos(screen_Lee,False,start)  
    shortest_path = find_shortest_path(arr_right,arr_bot, start, end)  
    draw_shortest_path(shortest_path, screen_Lee)  
    pygame.display.flip()  
    is_working = True
    while is_working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_working = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= btn_menu_x and mouse[0] <= btn_menu_x + Button_Size_W and \
                        mouse[1] >= btn_menu_y and mouse[1] <= btn_menu_y + Button_Size_H:
                    return Menu()
                if mouse[0] >= btn_regenerate_x and mouse[0] <= btn_regenerate_x + Button_Size_W and \
                        mouse[1] >= btn_regenerate_y and mouse[1] <= btn_regenerate_y + Button_Size_H:
                    is_working = False
                    return Lee_Alg()
        pygame.display.flip()
def set_pos(sc,start_or_end,start=(0,0)):
    is_end = False
    if start_or_end:
        color = (255,0,0)
    else:
        is_end = True
        color = (0,255,0)
    pos = {"x":0,"y":0}
    is_working = True
    size = cell_size-3
    pygame.draw.rect(sc,color,(GAP+cell_size*pos["x"]+2,GAP+cell_size*pos["y"]+2,size,size))
    
    while is_working:
        for event in pygame.event.get():
            if is_end:
                pygame.draw.rect(sc,(255,0,0),(GAP+cell_size*start[1]+2,GAP+cell_size*start[0]+2,size,size))
            if event.type == pygame.QUIT:
                is_working = False
                return
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and pos["x"]!=board_size-1:
                    pygame.draw.rect(sc,BLACK,(GAP+cell_size*pos["x"]+2,GAP+cell_size*pos["y"]+2,size,size))
                    pos["x"]+=1
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and pos["x"]!=0:
                    pygame.draw.rect(sc,BLACK,(GAP+cell_size*pos["x"]+2,GAP+cell_size*pos["y"]+2,size,size))
                    pos["x"]-=1     
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and pos["y"]!=board_size-1:
                    pygame.draw.rect(sc,BLACK,(GAP+cell_size*pos["x"]+2,GAP+cell_size*pos["y"]+2,size,size))
                    pos["y"]+=1
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and pos["y"]!=0:
                    pygame.draw.rect(sc,BLACK,(GAP+cell_size*pos["x"]+2,GAP+cell_size*pos["y"]+2,size,size))
                    pos["y"]-=1   
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    is_working = False
                    return (pos["y"],pos["x"])
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= btn_menu_x and mouse[0] <= btn_menu_x + Button_Size_W and \
                        mouse[1] >= btn_menu_y and mouse[1] <= btn_menu_y + Button_Size_H:
                    return Menu()
                if mouse[0] >= btn_regenerate_x and mouse[0] <= btn_regenerate_x + Button_Size_W and \
                        mouse[1] >= btn_regenerate_y and mouse[1] <= btn_regenerate_y + Button_Size_H:
                    is_working = False
                    return Lee_Alg()
            pygame.draw.rect(sc,color,(GAP+cell_size*pos["x"]+2,GAP+cell_size*pos["y"]+2,size,size))
        pygame.display.flip()   
    return (pos["y"],pos["x"])

def find_shortest_path(maze_right,maze_bot, start, end):
    queue = [start]
    visited = set() # словарь из неповторяющихся элементов 
    prev = {}
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in get_neighbors(current, maze_right,maze_bot):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                prev[neighbor] = current
    # Восстанавливаем кратчайший путь
    shortest_path = [end]
    while shortest_path[-1] != start:
        shortest_path.append(prev[shortest_path[-1]])
    shortest_path.reverse()
    return shortest_path

def get_neighbors(cell, maze_right,maze_bot):
    row, col = cell
    neighbors = []
    # Проверяем клетку сверху
    if row > 0 and maze_bot[row - 1][col] != 1:
        neighbors.append((row - 1, col))
    # Проверяем клетку снизу
    if row < board_size - 1 and maze_bot[row][col] != 1:  
        neighbors.append((row + 1, col))
    # Проверяем клетку слева
    if col > 0 and maze_right[row][col - 1] != 1:  
        neighbors.append((row, col - 1))
    # Проверяем клетку справа
    if col < board_size - 1 and maze_right[row][col] != 1: 
        neighbors.append((row, col + 1))
    return neighbors

def draw_shortest_path(path, screen):
    for cell in path:
        row, col = cell
        # Отрисовка красного квадрата по середине клетки
        pygame.draw.rect(screen, (255, 0, 0), (col * cell_size + GAP + cell_size // 2 - 1, row * cell_size + GAP + cell_size // 2 - 1, 3, 3))
        clock.tick(15)
        pygame.display.flip()
