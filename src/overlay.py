import pygame, os
from settings import *

# Obtain file system directories
current_dir = os.path.dirname(__file__)
assets_dir = os.path.join(current_dir, "..\\assets")

class Overlay:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.selection_ui = pygame.image.load(os.path.join(assets_dir, 'ui\\selection.png')).convert_alpha()
        self.startend_ui = pygame.image.load(os.path.join(assets_dir, 'ui\\startend.png')).convert_alpha()
        self.path_selection_ui = pygame.image.load(os.path.join(assets_dir, 'ui\\path_selection.png')).convert_alpha()
        self.current_block = pygame.image.load(os.path.join(assets_dir, 'ui\\current_block.png')).convert_alpha()
        self.resetall_img = pygame.image.load(os.path.join(assets_dir, 'ui\\resetall.png')).convert_alpha()
        self.resetpath_img = pygame.image.load(os.path.join(assets_dir, 'ui\\resetpath.png')).convert_alpha()

    def display(self):
        self.display_surface.blit(self.selection_ui, (-50,350))
        self.display_surface.blit(self.startend_ui, (230,352))
        self.display_surface.blit(self.path_selection_ui, (475, 485))
        self.display_surface.blit(self.current_block, (25, 525))
        self.display_surface.blit(self.resetpath_img, (800, 50))
        self.display_surface.blit(self.resetall_img, (800, 125))


    def update(self):
         self.display()

    def update_current_block(self, current_img):
        self.current_block.blit(current_img, (16,16))
            


"""
This class represents the blocks that are avaiable for the user to place, right now
The visualizer only has two blocks (Walls, Blank). This class exists to assist the
Implementation of Overlay, by using constants to locate the ui elements. Future
Blocks could be added (Features such as weighted path finding etc.) Which might
require a rewrite of this class/system if needed to made scalable. 
"""
class Block:
    def __init__(self, x, y, xsize=48, ysize=48):
        self.x = x
        self.y = y
        self.surface = pygame.Surface((xsize, ysize), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=(x,y))

        self.display_surface = pygame.display.get_surface()

    def draw(self):
        self.display_surface.blit(self.surface, (self.x, self.y))

                    