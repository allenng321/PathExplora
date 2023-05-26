import pygame, os
from pygame import Color
from overlay import Block
from settings import *

# Obtain file system directories
current_dir = os.path.dirname(__file__)
assets_dir = os.path.join(current_dir, "..\\..\\assets")

class GridSystem:
    def __init__(self, rows, cols):
        self.grids = []
        self.img = pygame.image.load(os.path.join(assets_dir, 'ui\\grasstile.png')).convert_alpha()
        self.mouse_down = False

        # Selection of blocks for capturign user input
        self.blocks = [Block(143, 538), Block(190, 538)]

        # Choosing the grid to start or end
        self.start_end = [Block(340, 538), Block(405, 538)]

        # Handles and modify path data 
        self.cur_selected = 0 # 0 = grass, 1 = wall

        self.path_data = []
        for i in range(16):
            row = [0] * 16
            self.path_data.append(row)

        # Add surface grids
        for r in range(rows):
            inner_arr = []
            for c in range(cols):
                inner_arr.append(GridCell(GRID_INIT_X + r*GRID_SIZE,GRID_INIT_Y + c*GRID_SIZE, self.img))
            self.grids.append(inner_arr)    

    def display_grids(self):
        for i in self.grids:
            for j in i:
                j.draw()

        for block in self.blocks:
            block.draw()

        for de in self.start_end:
            de.draw()
    
    # Check for user mouse input to obtain specific grid cells
    def check_input(self):
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            
            # Check on single left click button down
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_down = True
                self.on_collide_cell(mouse_pos)
                self.on_click_block(mouse_pos)
                self.on_click_startend(mouse_pos)

            # No longer holding on mouse click
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.mouse_down = False

            elif event.type == pygame.MOUSEMOTION and self.mouse_down:
                 self.on_collide_cell(mouse_pos)

    # Upon clicking under block selection ui, switch block placement on grid_system
    def on_click_block(self, mouse_pos):
        # self.blocks[0] represents wall, self.blocks[1] represents grass

        if self.blocks[0].rect.collidepoint(mouse_pos):
            self.cur_selected = 1
        elif self.blocks[1].rect.collidepoint(mouse_pos):
            self.cur_selected = 0

    def on_click_startend(self, mouse_pos):
        if self.start_end[0].rect.collidepoint(mouse_pos):
            print("Checked Start")
        elif self.start_end[1].rect.collidepoint(mouse_pos):
            print("Checked End")
        

    # On click cell, calculates the specific grid cell by obtaining the mouse position
    def on_collide_cell(self, mouse_pos):
        for row in self.grids:
            for cell in row:
                if cell.rect.collidepoint(mouse_pos):
                    cell_row = int((cell.x-GRID_INIT_X)/30)
                    cell_col = int((cell.y-GRID_INIT_Y)/30)

                    cur = None
                    if self.cur_selected == 0:
                        cur = pygame.image.load(os.path.join(assets_dir, 'ui\\grasstile.png')).convert_alpha()
                    else:
                        cur = pygame.image.load(os.path.join(assets_dir, 'pathfinder\\Graphics\\bush.png')).convert_alpha()
                    self.grids[cell_row][cell_col].update_image(cur)

                    # Modify path_data for backend
                    self.path_data[cell_row][cell_col] = self.cur_selected

class GridCell:
    def __init__(self, x, y, image=None):
        self.x = x
        self.y = y
        self.surface = pygame.Surface((GRID_SIZE, GRID_SIZE), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=(x,y))
        self.display_surface = pygame.display.get_surface()
        
        # Each grid defaults to be a empty cell
        if image:
            self.image = image
        else:
            self.image = None

    def draw(self):
        if self.image:
            self.surface.blit(self.image, (0,0))
        self.display_surface.blit(self.surface, (self.x, self.y))

    def update_image(self, image):
        self.surface.fill(Color(0,0,0,0))
        self.image = image
        
