import  pygame
import random

#creer une classe pour gerer la comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #definir quel est limage associer a la comete
        self.image = pygame.image.load("PygameAssets-main/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        # retirer la boule de feu
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        #verifier si le nbr de comet = 0
        if len(self.comet_event.all_comets) == 0:
            #remetre la bare a 0
            self.comet_event.reser_persent()
            #apparaitre les monstrer
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 510:
            self.remove()

            #si il n'y a plu de boule de feu sur le terrain
            if len(self.comet_event.all_comets) == 0:
                print("fin")
                #remetre la jauge au depart
                self.comet_event.reser_persent()
                self.comet_event.fall_mode = False

        #verifier si la voule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_player
        ):
            print("toucher")
            #retirer la boule de feu
            self.remove()
            #subir des degats
            self.comet_event.game.player.damage(20)

