import pygame
import random
pygame.init()
clock = pygame.time.Clock()
GAP = 50
start_cell_x = 0
start_cell_y = 0
width = 1600
height = 900
Button_Size_W = 350
Button_Size_H = 100
BLACK = (0,0,0)
WHITE = (255,255,255)
TEXT_COLOR = (10, 191, 42)
font = pygame.font.SysFont('Courier New',35,bold=True)
info_font = pygame.font.SysFont('Courier New',20,bold=True)
font2 = pygame.font.SysFont("Courier New",50,bold=True)
color1 = (31, 25, 24)
color2 = (56, 46, 44)
btn_regenerate_x = 16 * 50 + 70
btn_regenerate_y = 14 * 50
btn_menu_x = btn_regenerate_x + Button_Size_W + 170
btn_menu_y = 50    
btn_menu_width = Button_Size_W // 2
menu_btn_text = font.render("Menu", True, TEXT_COLOR)
