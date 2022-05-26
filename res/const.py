import pygame, sys
from pygame.locals import *


global FPSCLOCK, SCR
pygame.init()
FPS = 120
FPSCLOCK = pygame.time.Clock()
WX = 1000
WY = 625
SCR = pygame.display.set_mode((WX, WY))
SCR.fill((0,0,0))
CANVAS = pygame.Surface((WX,WY))
pygame.display.set_caption("yeet")
MUTE = False

BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (155,155,155)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GOLDEN = (255,215,0)
