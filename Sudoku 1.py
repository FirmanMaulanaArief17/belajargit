# import pygame library
import pygame
pygame.font.init()
pygame.display.set_caption('Sudoku')
# mempersiapkan tampilan
screen = pygame.display.set_mode((450, 550))
font1 = pygame.font.SysFont("consolas", 40)
font2 = pygame.font.SysFont("georgia", 20)
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)