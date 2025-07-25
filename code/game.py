import pygame

from code.menu import Menu


class Game:
    # CRIANDO A TELA
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    #INICIANDO O JOGO
    def run(self):
        #MANTENDO ELA ABERTA
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.quit()  # Close window
            #        quit()  # End pygame
