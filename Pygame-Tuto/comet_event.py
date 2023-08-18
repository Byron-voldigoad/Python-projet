import pygame
from commet import Comet

#creer une classe pour gerer cet evenement
class CometFallEvent:
    # lors du chargement -> creer un compteir
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 15
        self.game = game
        self.fall_mode = False
        #definir un groupe de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()


    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loaded(self):
        return self.percent >= 100

    def reser_persent(self):
        self.percent = 0

    def meteor_fall(self):
        #bocles pour les valeur 1a 10
        for i in range(1,10):
            #apparaitre 1 premier boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #la jauge d'eve,nement est totalement charger
        if self.is_full_loaded() and len(self.game.all_monters) == 0:
            self.meteor_fall()
            self.fall_mode = True #pour activer l'evnement

    def update_bar(self, surface):
        #ajouter du pourcentage a la bare
        self.add_percent()


        # barre noir (en arrier plan)
        pygame.draw.rect(surface, (0,0,0), [
            0, #l'axe des x
            surface.get_height()- 20, # l'axe y
            surface.get_width(), #longueur de la fenetre
            10 # epaisseur de la barre
        ])
        # barre rouge (jauge d'evenement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe y
            (surface.get_width()/100) * self.percent,  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
