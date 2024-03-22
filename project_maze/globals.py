import pygame
import random

pygame.init()
clock = pygame.time.Clock()
GAP = 50
board_size = 16
cell_size = 50
start_cell_x = 0
start_cell_y = 0
width = board_size*cell_size+GAP*2
height = board_size*cell_size+GAP*2
screen = pygame.display.set_mode((width,height))
BLACK = (0,0,0)
WHITE = (255,255,255)

#инициализация лабиринта с заполнеными клетками
arr = [0]*board_size
for i in range(board_size):
    arr[i] = [0]*board_size
    
