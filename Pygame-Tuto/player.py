import pygame
from projectile import Projectile
import animation

#cree un premiere classe pour representer le joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 11
        self.velocity = 3
        self.all_projectile = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 490

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le jouer n'a plus de pv
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        #dessiner notre bar de vie
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (11, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])


    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile

        self.all_projectile.add(Projectile(self))
        #demarrer l'animation
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play("tir")



    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monters):
            self.rect.x += self.velocity

    def move_left(self):
        # si le jouer n'est pas en collision avec le monstre
        self.rect.x -= self.velocity