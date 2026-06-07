import pygame
 
 
def pegar_sprite(caminho, x, y, width, height, scale=1.0):
    # semana 2: ainda não temos spritesheet no jogo da memória
    # então retorna uma surface vazia transparente no lugar
    # assim o código não quebra quando importar essa função
    largura  = int(width  * scale)
    altura   = int(height * scale)
    surface  = pygame.Surface((largura, altura), pygame.SRCALPHA)
    surface.fill((0, 0, 0, 0))  # transparente
    return surface