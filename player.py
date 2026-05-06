import pygame

from bullet import Bullet
from helpers import load_frames, flip_frames, handle_portal_collision, advance_frame, apply_motion
from settings import vector

RUN_FRAMES = [f"Run ({i}).png" for i in range(1, 11)]
IDLE_FRAMES = [f"Idle ({i}).png" for i in range(1, 11)]
JUMP_FRAMES = [f"Jump ({i}).png" for i in range(1, 11)]
ATTACK_FRAMES = [f"Attack ({i}).png" for i in range(1, 11)]


class Player(pygame.sprite.Sprite):
    """A class the user can control"""

    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        """Initialize the player"""
        super().__init__()

        #Set constant variables
        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15

        # Gravity
        self.VERTICAL_ACCELERATION = 0.8


        # Determines how high the player can jump
        self.VERTICAL_JUMP_SPEED = 18
        self.STARTING_HEALTH = 100
        # Animation frames
        load_frames("images/player/run", RUN_FRAMES),((64,64))

        # TODO: assign flip_frames to self.move_left_sprites with this 1 argument
        #  1: self.move_right_sprites

        # TODO: assign load_frames() to self.idle_right_sprites with these 3 arguments
        load_frames("images/player/idle", IDLE_FRAMES),((64,64))

       flip_frames(self.idle_left_sprites) # TODO: assign flip_frames() to self.idle_left_sprites with this 1 argument
        #  1: self.idle_right_sprites

        # TODO: assign load_frames() to self.jump_right_sprites with these 3 arguments
        #  1: "images/player/jump"
        #  2: JUMP_FRAMES
        #  3: (64, 64))

        # TODO: assign flip_frames() to self.jump_left_sprites() with this 1 arguments
        #  1: self.jump_right_sprites

        # TODO: assign load_frames() to self.attack_right_sprites with these 3 arguments
        #  1: "images/player/attack"
        #  2: ATTACK_FRAMES
        #  3: (64, 64))

        # TODO: assign flip_frames() to self.attack_left_sprites with this 1 argument
        #  1: self.attack_right_sprites

        #Load image and get rect
        # TODO: assign 0 to self.current_sprite
        # TODO: assign self.idle_right_sprites[self.current_sprite] to self.image
        # TODO: assign self.image.get_rect() to self.rect
        # TODO: assign (x, y) to self.rect.bottomleft
        # TODO: assign pygame.mask.from_surface() to self.mask with 1 argument
        #  1: self.image

        #Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group
        # TODO: assign platform_group to self.platform_group
        # TODO: assign portal_group to self.portal_group
        # TODO: assign bullet_group to self.bullet_group

        #Animation booleans
        self.animate_jump = False
        self.animate_fire = False
        # TODO: assign False to self.animate_jump
        # TODO: assign False to self.animate_fire

        #Load sounds
        # TODO: assign pygame.mixer.Sound() to self.jump_sound with this 1 argument
        #  1: "sounds/jump_sound.wav"
        # TODO: assign pygame.mixer.Sound() to self.slash_sound with this 1 argument
        #  1: "sounds/slash_sound.wav"
        # TODO: assign pygame.mixer.Sound() to self.portal_sound with this 1 argument
        #  1: "sounds/portal_sound.wav"
        # TODO: assign pygame.mixer.Sound() to self.hit_sound with this 1 argument
        #  1: "sounds/player_hit.wav"

        #Kinematics vectors
        vector(x,y)

        vector(0,0)

        vector(0, self.VELOCITY_ACCELERATION)


        #Set initial player values
        self.STARTING_HEALTH = self.health
        self.starting_x = x
        self.starting_y = y


    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()
        self.check_animations()


        #Update the player's mask
        self.mask = pygame.mask.from_surface(self.image)


    def move(self):
        """Move the player"""
        # Set the acceleration vector
        vector(0, self.VELOCITY_ACCELERTAION    )

        # If the user is pressing a key, set the x-component of the acceleration to be non-zero
        # TODO: assign pygame.key.get_pressed() to keys
        # TODO: if keys[pygame.K_LEFT]:
            # TODO: assign -1 * self.HORIZONTAL_ACCELERATION to self.accleration.x
            # TODO: call self.animate() with these 2 arguments
            #  1: self.move_left_sprites
            #  2: 0.5
        # TODO: elif keys[pygame.K_RIGHT]:
            # TODO: assign self.HORIZONTAL_ACCELERATION to self.acceleration.x
            # TODO: call self.animate() with these 2 arguments
            #  1: self.move_right_sprites
            #  2: 0.5
        # TODO: else:
            #TODO: if self.velocity.x > 0:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.idle_right_sprites
                #  2: 0.5
            # TODO: else:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.idle_left_sprites
                #  2: 0.5

        # Apply friction before integrating
        self.acceleration.x = self.velocity.x * self.HORIZONTAL_ACCELERATION


        apply_motion(self)
        #  1: self


    # noinspection PyTypeChecker
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between player and platforms when moving vertically
        # TODO: if self.velocity.y != 0:
            # TODO: assign pygame.sprite.spritecollide() to collided_platforms with these 4 arguments
            #  1: self
            #  2: self.platform_group
            #  3: False
            #  4: pygame.sprite.collide_mask

            # TODO: if collided_platforms:
                # TODO: if self.velocity.y > 0:
                    #Landing on a platform
                    # TODO: assign collided_platforms[0].rect.top + 5 to self.position.y
                    # TODO: assign 0 to self.velocity.y
                # TODO: else:
                    #Hitting a platform from below while jumping
                    # TODO: assign 0 to self.velocity.y
                    # TODO: while pygame.sprite.spritecollide(self, self.platform_group, False):
                        # TODO: add 1 to self.position.y
                        # TODO: assign self.position to self.rect.bottomleft

        # Collision check for portals
        # TODO: call handle_portal_collision() with 1 argument
        #  1: self


    def check_animations(self):
        """Check to see if jump/fire animations should run"""
        #Animate the player jump
        # TODO: if self.animate_jump:
            # TODO: if self.velocity.x > 0:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.jump_right_sprites
                #  2: 0.1
            # TODO: else:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.jump_left_sprites
                #  2: 0.1

        #Animate the player attack
        # TODO: if self.animate_fire:
            # TODO: if self.velocity.x > 0:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.attack_right_sprites
                #  2: 0.25
            # TODO: else:
                # TODO: call self.animate() with these 2 arguments
                #  1: self.attack_left_sprites
                #  2: 0.25


    # noinspection PyTypeChecker
    def jump(self):
        if pygame.sprite.spritecollide(self, self.platform_group, False ):
            self.jump_sound.play()
            self.velocity.y = self.VERTICAL_JUMP_SPEED - 1
            self.animate_jump = True
        """Jump upwards if on a platform"""
        #Only jump if on a platform
        # TODO: if pygame.sprite.spritecollide(self, self.platform_group, False):
            # TODO: call self.jump_sound.play()
            # TODO: assign -1 * self.VERTICAL_JUMP_SPEED to self.velocity.y
            # TODO: assign True to self.animate_jump


    def fire(self):
        self.slash_sound.play()
        Bullet(self.rect.centerx, self.rect.centery, self.bullet_group, self)
        self.animate_fire = True
        """Fire a 'bullet' from a sword"""
        # TODO: call self.slash_sound.play()
        # TODO: call Bullet() with these 4 arguments
        #  1: self.rect.centerx
        #  2: self.rect.centery
        #  3: self.bullet_group
        #  4: self)
        # TODO: assign True to self.animate_fire

    def reset(self):
        vector(0,0)
        """Reset the player's position"""
        # TODO: assign vector() to self.velocity with these 2 arguments
        #  1: 0
        #  2: 0
        vector(self.starting_x, self.starting_y)

        # TODO: assign vector() to self.position with these 2 arguments
        #  1: self.starting_x
        #  2: self.starting_y
        self.positon = self.rect.bottomleft

        # TODO: assign self.position to self.rect.bottomleft


    def animate(self, sprite_list, speed):
        """Animate the player's actions"""
        # TODO: assign advance_frame() to (self.current_sprite, wrapped) with these 3 arguments
        #  1: self.current_sprite
        #  2: sprite_list
        #  3: speed)
        # TODO: if wrapped:
            # TODO: if self.animate_jump:
                # TODO: assign False to self.animate_jump
            # TODO: if self.animate_fire:
                # TODO: assign False to self.animate_fire
        # TODO: assign sprite_list[int(self.current_sprite)] to self.image
