import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT


RUBY_FRAMES = [f"tile00{i}.png" for i in range(7)]


def load_frames(folder, filenames, size):

    return [
        pygame.transform.scale(pygame.image.load(f"{folder}/{name}"), size)
        for name in filenames
    ]


def flip_frames(frames):

    return [pygame.transform.flip(s, True, False) for s in frames]


def advance_frame(current, sprite_list, speed):

    if current < len(sprite_list) - 1:
        return current + speed, False
    return 0, True


def teleport(sprite):

    if sprite.position.x > WINDOW_WIDTH // 2:
        sprite.position.x = 86
    else:
        sprite.position.x = WINDOW_WIDTH - 150

    if sprite.position.y > WINDOW_HEIGHT // 2:
        sprite.position.y = 64
    else:
        sprite.position.y = WINDOW_HEIGHT - 132

    sprite.rect.bottomleft = sprite.position


def handle_portal_collision(sprite):
    if pygame.sprite.spritecollide(sprite, sprite.portal_group, False):
        sprite.portal_sound.play()
        teleport(sprite)


def apply_motion(sprite):
    sprite.velocity += sprite.acceleration
    sprite.position += sprite.velocity + 0.5 * sprite.acceleration

    if sprite.position.x < 0:
        sprite.position.x = WINDOW_WIDTH
    elif sprite.position.x > WINDOW_WIDTH:
        sprite.position.x = 0

    sprite.rect.bottomleft = sprite.position