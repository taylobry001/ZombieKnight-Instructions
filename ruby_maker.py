self.ruby_sprites = load_frames("image/ruby", RUBY_FRAMES, (64, 64))

self.current_sprite = 0
self.image = self.ruby_sprites[self.current_sprite]
self.rect = self.image.get_rect()
self.rect.bottomleft = (x, y)

main_group.add(self)


self.animate(self.ruby_sprites, 0.25)


if self.current_sprite < len(sprite_list) - 1:
    self.current_sprite += speed
else:
    self.current_sprite = 0

self.image = sprite_list[int(self.current_sprite)]
