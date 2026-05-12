# Gravity
self.VERTICAL_ACCELERATION = 3
self.HORIZONTAL_VELOCITY = 5

# Animation frames
self.ruby_sprites = load_frames("images/ruby", RUBY_FRAMES, (64, 64))

# Load image and rect
self.current_sprite = 0
self.image = self.ruby_sprites[self.current_sprite]
self.rect = self.image.get_rect()
self.rect.bottomleft = (WINDOW_WIDTH // 2, 100)

# Attach groups
self.platform_group = platform_group
self.portal_group = portal_group

# Load sounds
self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")

# Kinematic vectors
self.position = vector(self.rect.x, self.rect.y)

self.velocity = vector(
    random.choice([-1 * self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]),
    0
)

self.acceleration = vector(0, self.VERTICAL_ACCELERATION)


# UPDATE
self.animate(self.ruby_sprites, 0.25)
self.move()
self.check_collisions()


# MOVE
apply_motion(self)


# CHECK COLLISIONS
collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)

if collided_platforms:
    self.position.y = collided_platforms[0].rect.top + 1
    self.velocity.y = 0

handle_portal_collision(self)


# ANIMATE
if self.current_sprite < len(sprite_list) - 1:
    self.current_sprite += speed
else:
    self.current_sprite = 0

self.image = sprite_list[int(self.current_sprite)]
