import pygame
import random
#definir un classe qui va  s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    #definir les chose a faire a la creation d l'entité
    def __init__(self,sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'PygameAssets-main/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # commecer l'animation de l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #definir un methode pour demarrer l'animation
    def start_animation(self):
        self.animation = True

    #definir une methode pour animer le sprite
    def animate(self, loop=False):

        #verifier  si l'animation suivnte
        if self.animation:

            #passer a limage suivante
            self.current_image += random.randint(0, 1)
            #verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                #remetre l'animation au  deppart
                self.current_image = 0
                #verifier si l'animation n'est pas en boucle
                if loop is False:
                    #desactivation de l'animation
                    self.animation = False

            #modifier l'image précedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

#definir une fonction pour charger les images d'un sprite
def loard_animation_image(sprite_name):
    #charger les 24 image de ce sprite dans le dossier correspondant
    images = []
    #recuperer le chemin du dossier pour ce sprite
    path = f"PygameAssets-main/{sprite_name}/{sprite_name}"

    #bouvler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

        #renvoyer le contenu de  la liste d'image
    return images


#definir un dictionnaire qui va contenir les images chargees de chaque sprite
animations = {
    'mummy' : loard_animation_image('mummy'),
    'player' : loard_animation_image("player"),
    'alien' : loard_animation_image('alien')
}