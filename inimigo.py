import pygame

class Inimigo:
    def __init__(self):
        self._pos_x = 800
        self._pos_y = 0
        self.velocidade = 1
        self._monstro = pygame.image.load("Imagens/Aranha2.png")
        self.personagem = None

    def anda(self, personagem):
        self.personagem = personagem
        if self._pos_y < self.personagem.pos_y:
            self._pos_y += self.velocidade

        if self._pos_y > self.personagem.pos_y:
            self._pos_y -= self.velocidade

        if self._pos_x < self.personagem.pos_x:
            self._pos_x += self.velocidade

        if self._pos_x > self.personagem.pos_x:
            self._pos_x -= self.velocidade

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def monstro(self):
        return self._monstro
