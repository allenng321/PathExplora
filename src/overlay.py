import pygame, os
from settings import *

# Obtain file system directories
current_dir = os.path.dirname(__file__)
assets_dir = os.path.join(current_dir, "..\\assets")

class Overlay:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.tiles = ['grass', 'wall2']
        self.blocks = [Block(50, 50), Block(50, 100)]

        # for i in self.tiles:
        #     self.blocks.append(Block())

        self.selection_ui = pygame.image.load(os.path.join(assets_dir, 'ui\\selection.png')).convert_alpha()
        
    def display(self):
        self.display_surface.blit(self.selection_ui, (-50,350))

"""
This class represents the blocks that are avaiable for the user to place, right now
The visualizer only has two blocks (Walls, Blank). This class exists to assist the
Implementation of Overlay, by using constants to locate the ui elements. Future
Blocks could be added (Features such as weighted path finding etc.) Which might
require a rewrite of this class/system if needed to made scalable. 
"""
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface = pygame.Surface((48, 48), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=(x,y))

        self.display_surface = pygame.display.get_surface()
        self.img = pygame.image.load(os.path.join(assets_dir, 'pathfinder\\Graphics\\bush.png')).convert_alpha()

    def draw(self):
            if self.img:
                self.surface.blit(self.img, (0,0))
            self.display_surface.blit(self.surface, (self.x, self.y))