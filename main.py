import pygame
from player import Player
from inimigo import Inimigo
from ataque import Ataque

pygame.init()
janela_principal = pygame.display.set_mode((1600,1200))
pygame.display.set_caption("Jogo do Pipi atirador")

jogador = Player()
inimigo = Inimigo()
disparo = Ataque(jogador)
angle = 0

janela_aberta = True
while janela_aberta:

    pygame.time.delay(10)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_aberta = False

    comando = pygame.key.get_pressed()

    if comando[pygame.K_UP]:
        angle = 180
        jogador.cima()

    if comando[pygame.K_DOWN]:
        angle = 0
        jogador.baixo()

    if comando[pygame.K_RIGHT]:
        angle = 90
        jogador.direita()

    if comando[pygame.K_LEFT]:
        angle = 270
        jogador.esquerda()

    if comando[pygame.K_SPACE]:
        disparo.dispara(angle, jogador)


    janela_principal.fill((255,255,255))

    # img_copy = pygame.transform.rotate(jogador.personagem, angle)
    # janela_principal.blit(img_copy, (jogador.pos_x - int(img_copy.get_width() / 2), jogador.pos_y - int(img_copy.get_height() / 2)))
    janela_principal.blit(pygame.transform.rotate(jogador.personagem, angle), (jogador.pos_x, jogador.pos_y))
    janela_principal.blit(inimigo.monstro, (inimigo.pos_x, inimigo.pos_y))
    janela_principal.blit(disparo.tiro, (disparo.pos_x, disparo.pos_y))

    inimigo.anda(jogador)

    pygame.display.update()

pygame.quit()