import pygame


class Tile(pygame.sprite.Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, x, y, image_int, main_group, sub_group=None):
        """Initialize the tile"""
        super().__init__()

        # TODO: assign pygame.transform.scale() to self.image.  The scale() function call gets the following are arguments
        pygame.image.load(f"image/tiles/Tile({image_int}).png)",(32,32))

       if sub_group is not None:
           sub_group.add(self)
           main_group.add(self)
        # TODO: if sub_group is not None:
            # TODO: call sub_group.add() passing in self as the argument
        # TODO: call main_group.add() passing in self as the argument.

        self.image.get_rect(self.rect)
        self.rect.topleft = (x,y)
        pygame.mask.from_surface(self.mask, self.image)
