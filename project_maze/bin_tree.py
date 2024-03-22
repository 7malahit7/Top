from globals import *
import random
def draw_border():
    pygame.draw.line(screen,BLACK,[GAP,GAP],[cell_size*board_size+GAP,GAP],2)
    pygame.draw.line(screen,BLACK,[GAP*board_size+GAP-1,GAP],[GAP*board_size+GAP-1,GAP*board_size+GAP],2)
    pygame.draw.line(screen,BLACK,[GAP*board_size+GAP-1,GAP*board_size+GAP],[GAP,GAP+board_size*cell_size],2)
    pygame.draw.line(screen,BLACK,[GAP,GAP+board_size*cell_size],[GAP,GAP],2)

def draw_filled_board():
    for row in range(board_size):
        for col in range(board_size):
            draw_full_cell(col,row)
def draw_full_cell(row,col):
    pygame.draw.rect(screen,BLACK,(row*cell_size+GAP,col*cell_size+GAP, cell_size,cell_size))
    pygame.draw.rect(screen,WHITE,(row*cell_size+1+GAP,col*cell_size+1+GAP,cell_size-2,cell_size-2))  
def draw_empty_cell(row,col):
    remove_left_cell(row,col)
    remove_right_cell(row,col)
    remove_top_cell(row,col)
    remove_bot_cell(row,col)

def remove_right_cell(row,col):
    pygame.draw.line(screen,WHITE,[row*cell_size+49+GAP,col*cell_size+1+GAP],[row*cell_size+49+GAP,col*cell_size+48+GAP],2)
def remove_left_cell(row,col):
    pygame.draw.line(screen,WHITE,[row*cell_size-1+GAP,col*cell_size+1+GAP],[row*cell_size-1+GAP,col*cell_size+48+GAP],2)    
def remove_top_cell(row,col):
    pygame.draw.line(screen,WHITE,[row*cell_size+1+GAP,col*cell_size-1+GAP],[row*cell_size+48+GAP,col*cell_size+GAP-1],2)  
def remove_bot_cell(row,col):
    pygame.draw.line(screen,WHITE,[row*cell_size+1+GAP,col*cell_size+49+GAP],[row*cell_size+48+GAP,col*cell_size+49+GAP],2) 

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
    

def draw_bin_tree(arg):
    global arr
    if arg == "SW":
        arr = bin_tree_SW(arr)
    elif arg == "NE":
        arr = bin_tree_NE(arr)
    elif arg == "NW":
        arr = bin_tree_NW(arr)
    elif arg == "SE":
        arr = bin_tree_SE(arr)
    
    for row in range(board_size):
        for col in range(board_size):
            if arr[row][col] == 0:
                draw_full_cell(col,row)
    for row in range(board_size):
        for col in range(board_size):
            if arr[row][col] == 1:    
                draw_empty_cell(col,row)
    for row in range(board_size):
        for col in range(board_size):
            if arr[row][col] == 2:    
                remove_left_cell(col,row)
    for row in range(board_size):
        for col in range(board_size):
            if arr[row][col] == 3:    
                remove_right_cell(col,row)
    for row in range(board_size):
        for col in range(board_size):
            if arr[row][col] == 4:    
                remove_top_cell(col,row)
    for row in range(board_size):
        for col in range(board_size):
            if arr[row][col] == 5:    
                remove_bot_cell(col,row)
    
