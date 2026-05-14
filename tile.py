import pygame


class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, image_int, main_group, sub_group=None):
        super().__init__()

        # Load and scale image
        self.image = pygame.transform.scale(
            pygame.image.load(f"images/tiles/Tile({image_int}).png"),
            (32, 32)
        )

        # Add to groups
        if sub_group is not None:
            sub_group.add(self)

        main_group.add(self)

        # Rect
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Mask
        self.mask = pygame.mask.from_surface(self.image)