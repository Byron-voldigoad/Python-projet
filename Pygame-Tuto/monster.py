import  pygame
import random
import animation


# creeune classe qui vas gerer la notion de monstre sur le jeu
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 530 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocyty = random.randint(1, 3)

    def set_loot_amount(self,amount):
        self.loot_amount = amount

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nouveau nombred epv es <= 0
        if self.health <= 0:
            #raparetre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.velocyty = random.randint(1, self.default_speed )
            self.health = self.max_health
            #ajouter le nombre de point
            self.game.add_score(self.loot_amount)

            #si la barre d'evenement est a max
            if self.game.comet_event.is_full_loaded( ):
                #retire du jeu
                self.game.all_monters.remove(self)
                # appel de la methode pour essayer de declencher la plui de meteorita
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        #dessiner notre bar de vie
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (11, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        #le deplacement ne se fait que s'il na pas de collision avec le joueur
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocyty
        #si le monstre est en collision avec le joueur
        else:
            #infliger les degats
            self.game.player.damage(self.attack)


#definir une class pour la momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130,130))
        self.set_speed(3)
        self.set_loot_amount(20)

    #definir une class pour l'alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300,300),130)
        self.max_health = 250
        self.health = self.max_health
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)
