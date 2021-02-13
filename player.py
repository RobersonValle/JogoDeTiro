import pygame

class Player:
    def __init__(self):
        self._pos_x = 800
        self._pos_y = 600
        self.velocidade = 5
        self._personagem = pygame.image.load("Imagens/Mago2.png")

    def cima(self):
        self._pos_y -= self.velocidade
        pass

    def baixo(self):
        self._pos_y += self.velocidade
        pass

    def direita(self):
        self._pos_x += self.velocidade
        pass

    def esquerda(self):
        self._pos_x -= self.velocidade
        pass

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def personagem(self):
        return self._personagem
