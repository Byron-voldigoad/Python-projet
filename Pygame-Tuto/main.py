import pygame
import math
from game import Game
pygame.init()


#definir une clock
clock = pygame.time.Clock()
FPS = 70


# generer la fenetre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,700))

#importere et changer l'arriere plan
background = pygame.image.load('PygameAssets-main/bg.jpg')

#importer changer notre banniere
banner = pygame.image.load("PygameAssets-main/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#importer ou changer notre boutton
play_button = pygame.image.load("PygameAssets-main/button.png")
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/1.9)


#charger notr jeu
game = Game()

running = True

# boucle tant que cettte condition est vrai
while running:

    #appliquer l'arrier plan du jeu
    screen.blit(background,(0,-220))

    #verifier si notre jeu a commencer ou non
    if game.is_playing:
        #declancher les instructions de pdate
        game.update(screen)
    #verifier si notre jeu n'a pas commencer
    else:
        #ajouter mon ecran de bien venue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()

        #detecter si un jouer lache yne touche au clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclacher pour lancer le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # metre le jeux en mode lancer
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en colision avec le boutons jouer
            if play_button_rect.collidepoint(event.pos):
                #metre le jeux en mode lancer
                game.start()
                #jouer le son
                game.sound_manager.play('click')
    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)