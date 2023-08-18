import pygame
from player import Player
from comet_event import CometFallEvent
from monster import Monster, Mummy, Alien
from sounds import SoundManager


# cree une seconde classe qui vas reprensenter notre jeu
class Game:

    def __init__(self):
        #definir si notre jeu a commencer ou non
        self.is_playing = False
        #generer notre joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #generer l'evenement
        self.comet_event = CometFallEvent(self)
        #groupe de monstre
        self.all_monters = pygame.sprite.Group()
        #gerer le son
        self.sound_manager = SoundManager()
        #mettre le score a 0
        self.font = pygame.font.SysFont("arial black",16,)

        self.score = 0
        self.pressed = { }


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self,points=10):
        self.score += points

    def game_over(self):
        #remetre le jeu a neuf
        self.all_monters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.all_comets =pygame.sprite.Group()
        self.comet_event.reser_persent()
        self.is_playing = False
        self.score = 0
        #jouer le son
        self.sound_manager.play('game_over')


    def update(self, screen):
        #afficher le score sur l'ecran
        score_text = self.font.render(f"Score : {self.score}",1,(0,0,0))
        screen.blit(score_text,(20, 20))

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie duj joueur
        self.player.update_health_bar(screen)

        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # actualiser l'animation du jouer
        self.player.update_animation()

        # recuperer les projeciles du joueur
        for projectile in self.player.all_projectile:
            projectile.move()

        # recuperer les monstre du jeu
        for monster in self.all_monters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer les cometes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectile.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monters.draw(screen)

        #appliquer l'ensemble des images de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # verifier si  le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monters.add(monster_class_name.__call__(self))