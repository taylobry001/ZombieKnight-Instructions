import pygame

from settings import FPS, WINDOW_HEIGHT, WINDOW_WIDTH, display_surface
from zombie import Zombie
from ruby import Ruby

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (25, 200, 25)

class Game:
    """A class to help manage gameplay"""

    def __init__(self, player, zombie_group, platform_group, portal_group, bullet_group, ruby_group):
        """Initialize the game"""
        #Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.STARTING_ROUND_TIME = self.round_time = 30
        self.STARTING_ZOMBIE_CREATION_TIME = self.zombie_creation_time = 5


        #Set fonts
        self.title_font = pygame.font.Font("fonts/Poultrygeist.ttf", 48)
        self.HUD_font = pygame.font.Font("fonts/Pixel.ttf", 24)

        #Set sounds
        self.lost_ruby_sound = pygame.mixer.Sound("sounds/lost_ruby.wav")
        self.ruby_pickup_sound = pygame.mixer.Sound("sounds/ruby_pickup.wav")
        self.level_music = pygame.mixer.music("sounds/level_music.wav")
        self.zombie_hit = pygame.mixer.Sound("sounds/zombie_hit.wav")
        self.zombie_kick = pygame.mixer.Sound("sounds/zombie_kick.wav")
        self.slash_sound = pygame.mixer.Sound("sounds/slash_sound.wav")
        self.player_hit = pygame.mixer.Sound("sounds/player_hit.wav")
        self.jump_sound = pygame.mixer.Sound("sounds/jump_sound.wav")
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")


        #Attach groups and sprites
        self.player = player
        self.zombie_group = zombie_group
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group
        self.ruby_group = ruby_group


    def update(self):
        self.frame_count += 1
        if self.frame_count % FPS == 0:
            self.ROUND_TIME = self.round_time
            self.round_time -= 1
            self.frame_count = 0

        self.check_game_over()
        self.check_round_completion()
        self.add_zombie()
        self.check_collisions()

    def draw(self):
        """Draw the game HUD"""

        #Set text
        score_text = self.HUD_font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, WINDOW_HEIGHT - 50)

        health_text = self.HUD_font.render("Health: " + str(self.player.health), True, WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, WINDOW_HEIGHT - 25)

        title_text = self.title_font.render("Zombie Knight", True, GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 25)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50)

        time_text = self.HUD_font.render("Sunrise In: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25)

        #Draw the HUD
        display_surface.blit()
        display_surface.blit(score_text, score_rect)
        display_surface.blit(health_text, health_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)

    def add_zombie(self):

        if self.frame_count % FPS == 0:
            if self.round_time % self.zombie_creation_time == 0:
                Zombie()
        """Add a zombie to the game"""
        #Check to add a zombie every second
        if self.frame_count % FPS == 0:
            if self.round_time % self.STARTING_ZOMBIE_CREATION_TIME == 0:
                Zombie(self.platform_group, self.portal_group, self.round_number, 5 + self.round_number)
                self.zombie_group.add_zombie(Zombie)
        # TODO: if self.frame_count % FPS == 0:
            #Only add a zombie if zombie creation time has passed
            # TODO: if self.round_time % self.zombie_creation_time == 0:
                # TODO: assign Zombie() to zombie with these 4 arguments
                #  1: self.platform_group
                #  2: self.portal_group
                #  3: self.round_number
                #  4: 5 + self.round_number
                # TODO: call self.zombie_group.add() with this 1 argument
                #  1: zombie


    def check_collisions(self):
        """Check collisions that affect gameplay"""
        #See if any bullet in the bullet group hit a zombie in the zombie group
        collisions = pygame.sprite.groupcollide(self.bullet_group, self.zombie_group, True, False)

        if collisions:
            for zombie_list in collisions.values():
                for zombie in zombie_list:
                    zombie.hit_sound.play()
                    zombie.is_dead = True
                    zombie.animate_death = True

        # See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        collision_list = pygame.sprite.spritecollide(self.player, self.zombie_group, False)

        if collision_list:
            for zombie in collision_list:
                # The zombie is dead; stomp it
                if zombie.is_dead:
                    zombie.kick_sound.play()
                    zombie.kill()
                    self.score += 25

                    ruby = Ruby(self.platform_group, self.portal_group)
                    self.ruby_group.add(ruby)

                # The zombie isn't dead, so take damage
                else:
                    self.player.health -= 20
                    self.player.hit_sound.play()

                    # Move the player to not continually take damage
                    self.player.position.x -= 256 * zombie.direction
                    self.player.rect.bottomleft = self.player.position
                    #Move the player to not continually take damage


        #See if a player collided with a ruby
        if pygame.sprite.spritecollide(self.player, self.ruby_group, False):
            self.score += 100
            self.player.health += 10
            self.ruby_pickup_sound.play()
            if self.player.health > self.player.STARTING_HEALTH:
                self.player.STARTING_HEALTH = self.player.health


        #See if a living zombie collided with a ruby
        for zombie in self.zombie_group:
            if not zombie.is_dead:
                if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                    self.lost_ruby_sound.play()
                    Zombie(self.platform_group, self.portal_group, self.round_number, 5 + self.round_number)
                    self.zombie_group.add(Zombie)


        # TODO: for zombie in self.zombie_group:
            # TODO: if not zombie.is_dead:
                # TODO: if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                    # TODO: call self.lost_ruby_sound.play()
                    # TODO: assign Zombie() to zombie with these 4 arguments
                    #  1: self.platform_group
                    #  2: self.portal_group
                    #  3: self.round_number
                    #  4: 5 + self.round_number
                    # TODO: call self.zombie_group.add() with this 1 argument
                    #  1: zombie


    def check_round_completion(self):
        if self.round_timer == 0:
            self.start_new_round()


    def check_game_over(self):
        if self.player <= 0:
            self.game_over = True
            pygame.mixer.music.stop()
            self.pause_game("GAME OVER! Final Score: " + str(self.score), "Press 'Enter' to continue")
            self.reset_game()
        """Check to see if the player lost the game"""
        # TODO: if self.player.health <= 0:
            # TODO: call pygame.mixer.music.stop()
            # TODO: call self.pause_game() with these 2 arguments
            #  1: "Game Over! Final Score: " + str(self.score)
            #  2: "Press 'Enter' to play again..."
            # TODO: call self.reset_game()


    def start_new_round(self):
        self.round_time += 1
        """Start a new night"""
        # TODO: add 1 to self.round_number

        #Decrease zombie creation time...more zombies
        if self.round_number < self.STARTING_ZOMBIE_CREATION_TIME:
            self.zombe_creation_time -= 1
        # TODO: if self.round_number < self.STARTING_ZOMBIE_CREATION_TIME:
            # TODO: subtract 1 from self.zombie_creation_time

        #Reset round values
        self.START_ROUND_TIME = self.round_time
        self.zombie_group.empty()
        self.ruby_group.empty()
        self.bullet_group.empty()
        self.player.reset()
        self.pause_game("You Won! Final Score: " + str(self.score), "Press 'Enter' to continue")
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time

        # TODO: call self.zombie_group.empty()
        # TODO: call self.ruby_group.empty()
        # TODO: call self.bullet_group.empty()

        # TODO: call self.player.reset()

        # TODO: call self.pause_game() with these 2 arguments
        #  1: "You survived the night!"
        #  2: "Press 'Enter' to continue..."


    def pause_game(self, main_text, sub_text):
        pygame.mixer.music.pause()
        """Pause the game"""
        # TODO: call pygame.mixer.music.pause()

        #Create main pause text
        self.title_font.render(main_text, True, GREEN)
        main_rect.center(main_text.get_rect())
        main_rect.center (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        # TODO: assign self.title_font.render() to main_text with these 3 arguments
        #  1: main_text
        #  2: True
        #  3: GREEN
        # TODO: assign main_text.get_rect() to main_rect
        # TODO: assign (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) to main_rect.center

        #Create sub pause text
        self.title_font.render(sub_text, True, WHITE)
        sub_text.center(sub_text.get_rect())
        sub_rect.center(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)
        # TODO: assign self.title_font.render() to sub_text with these 3 arguments
        #  1: sub_text
        #  2: True
        #  3: WHITE
        # TODO: assign sub_text.get_rect() to sub_rect
        # TODO: assign (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64) to sub_rect.center

        #Display the pause text
        # TODO: call display_surface.fill() with this 1 argument
        #  1: BLACK
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: main_text
        #  2: main_rect
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: sub_text
        #  2: sub_rect
        # TODO: call pygame.display.update()

        #Pause the game until user hits enter or quits
        # TODO: assign True to is_paused
        # TODO: while is_paused:
            # TODO: for event in pygame.event.get():
                # TODO: if event.type == pygame.KEYDOWN:
                    #User wants to continue
                    # TODO: if event.key == pygame.K_RETURN:
                        # TODO: assign False to is_paused
                        # TODO: call pygame.mixer.music.unpause()
                #User wants to quit
                # TODO: if event.type == pygame.QUIT:
                    # TODO: assign False to is_paused
                    # TODO: call pygame.event.post() with this 1 argument
                    #  1: pygame.event.Event(pygame.QUIT)
                    # TODO: call pygame.mixer.music.stop()


    def reset_game(self):
        """Reset the game"""
        #Reset game values
        # TODO: assign 0 to self.score
        # TODO: assign 1 to self.round_number
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time
        # TODO: assign self.STARTING_ZOMBIE_CREATION_TIME to self.zombie_creation_time

        #Reset the player
        # TODO: assign self.player.STARTING_HEALTH to self.player.health
        # TODO: call self.player.reset()

        #Empty sprite groups
        # TODO: call self.zombie_group.empty()
        # TODO: call self.ruby_group.empty()
        # TODO: call self.bullet_group.empty()

        # TODO: call pygame.mixer.music.play() with these 2 arguments
        #  1: -1
        #  2: 0.0