import pygame, os
from base.sprites import Generic
from player import Player
from settings import *

# Obtain file system directories
current_dir = os.path.dirname(__file__)
assets_dir = os.path.join(current_dir, "..\\assets")

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.setup()

    def setup(self):
        Generic(pos=(0,0),
                surf=pygame.image.load(os.path.join(assets_dir, 'world/ground.png')).convert_alpha(),
                groups=self.all_sprites,
                z=LAYERS['ground']
                )
        self.player = Player((512, 384), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.customize_draw(self.player)
        self.all_sprites.update(dt)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def customize_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        sprites_obj = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': []}

        # Saving all sprites to sprites_obj and sort to display them in order
        for sprite in self.sprites():
            sprites_obj[str(sprite.z)].append(sprite)
            
        for layer in sprites_obj:
            for sprite in sprites_obj[layer]:
                offset_rect = sprite.rect.copy()
                offset_rect.center -= self.offset
                self.display_surface.blit(sprite.image, offset_rect)