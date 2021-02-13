import pygame

class Ataque:
    def __init__(self, personagem):
        self._pos_x = personagem.pos_x
        self._pos_y = personagem.pos_y
        self.velocidade = 10
        self._personagem = personagem
        self._tiro = pygame.image.load("Imagens/bola de fogo.png")

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def tiro(self):
        return self._tiro

    def dispara(self, angle, personagem):
        if angle == 0:
            self._pos_y += self.velocidade
        if angle == 90:
            self._pos_x += self.velocidade
        if angle == 180:
            self._pos_y -= self.velocidade
        if angle == 270:
            self._pos_x -= self.velocidade