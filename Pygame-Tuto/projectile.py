import pygame

#definir la classe qui vas gerer le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    #definir l constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origine_image,self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player.all_projectile.remove(self)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #verifier si le projectile entre en collision avec un monstrre
        for monster in self.player.game.check_collision(self, self.player.game.all_monters):
            #supprimer le projectile
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        #verifieer si le projectile n'est plus present sur lecrans
        if self.rect.x > 1080:
            #supprimer le projectile (en dehor de l'ecrans)
            self.remove()