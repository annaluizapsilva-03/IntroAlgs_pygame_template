# funcoes.py
# funções de lógica e desenho do jogo da memória
# a coordenação já importa algumas dessas no template (calcular_pontos, etc.)

import pygame
from src.config import (
    LARGURA_TELA, ALTURA_TELA,
    LARGURA_CARTA, ALTURA_CARTA,
    ROXO, ROXO_ESCURO, BRANCO, PRETO,
    VERDE, AMARELO, CINZA, FUNDO,
)


# ── funções que já vêm no template da coordenação ───────────────────

def calcular_pontos(pontos_atuais, bonus):
    # chamada quando o jogador acerta um par
    return pontos_atuais + bonus


def jogador_perdeu(vidas):
    # no jogo da memória não tem vidas, então nunca perde por isso
    # deixei aqui pra manter o padrão do template
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    # garante que um valor fica entre minimo e maximo
    # usamos pra não deixar o cursor sair da tela
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(rect1, rect2):
    # checa se dois retângulos estão se tocando
    return rect1.colliderect(rect2)


def tomar_dano(vidas, dano):
    # reduz as vidas (não usamos no jogo da memória mas o template pede)
    return vidas - dano


# ── funções específicas do jogo da memória ──────────────────────────

def criar_cartas(pares, largura_carta, altura_carta, colunas):
    import random
    todas = pares + pares
    random.shuffle(todas)

    espaco_x = (LARGURA_TELA - colunas * largura_carta) // (colunas + 1)
    espaco_y = 20
    inicio_y = 100

    cartas = []
    for i in range(len(todas)):
        coluna = i % colunas
        linha  = i // colunas

        x = espaco_x + coluna * (largura_carta + espaco_x)
        y = inicio_y + linha  * (altura_carta  + espaco_y)

        carta = {
            "x":        x,
            "y":        y,
            "emoji":    todas[i][0],
            "nome":     todas[i][1],
            "virada":   False,
            "acertada": False,
        }
        cartas.append(carta)

    return cartas


def desenhar_carta(tela, carta, fonte_titulo, fonte_carta):
    x = carta["x"]
    y = carta["y"]

    if carta["acertada"]:
        pygame.draw.rect(tela, VERDE, (x, y, LARGURA_CARTA, ALTURA_CARTA), border_radius=8)
        pygame.draw.rect(tela, PRETO, (x, y, LARGURA_CARTA, ALTURA_CARTA), 2, border_radius=8)
        texto = fonte_carta.render(carta["nome"], True, PRETO)
        tela.blit(texto, (x + LARGURA_CARTA // 2 - texto.get_width() // 2,
                          y + ALTURA_CARTA  // 2 - texto.get_height() // 2))

    elif carta["virada"]:
        pygame.draw.rect(tela, BRANCO,      (x, y, LARGURA_CARTA, ALTURA_CARTA), border_radius=8)
        pygame.draw.rect(tela, ROXO_ESCURO, (x, y, LARGURA_CARTA, ALTURA_CARTA), 2, border_radius=8)
        txt_emoji = fonte_carta.render(carta["emoji"], True, PRETO)
        tela.blit(txt_emoji, (x + LARGURA_CARTA // 2 - txt_emoji.get_width() // 2, y + 20))
        txt_nome = fonte_carta.render(carta["nome"], True, ROXO_ESCURO)
        tela.blit(txt_nome,  (x + LARGURA_CARTA // 2 - txt_nome.get_width() // 2,  y + 60))

    else:
        pygame.draw.rect(tela, ROXO,        (x, y, LARGURA_CARTA, ALTURA_CARTA), border_radius=8)
        pygame.draw.rect(tela, ROXO_ESCURO, (x, y, LARGURA_CARTA, ALTURA_CARTA), 2, border_radius=8)
        ponto = fonte_titulo.render("?", True, BRANCO)
        tela.blit(ponto, (x + LARGURA_CARTA // 2 - ponto.get_width() // 2,
                          y + ALTURA_CARTA  // 2 - ponto.get_height() // 2))


def desenhar_tela(tela, cartas, pontos, recorde, fontes):
    fonte_titulo, fonte_normal, fonte_carta = fontes

    tela.fill(FUNDO)

    titulo = fonte_titulo.render("Jogo da Memoria - Filmes & Series", True, ROXO_ESCURO)
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 15))

    txt_pont = fonte_normal.render(f"Pares: {pontos // 10}", True, ROXO_ESCURO)
    txt_rec  = fonte_normal.render(f"Recorde: {recorde // 10}", True, ROXO_ESCURO)
    tela.blit(txt_pont, (20, 20))
    tela.blit(txt_rec,  (LARGURA_TELA - txt_rec.get_width() - 20, 20))

    for carta in cartas:
        desenhar_carta(tela, carta, fonte_titulo, fonte_carta)

    btn_rect = pygame.Rect(LARGURA_TELA // 2 - 70, ALTURA_TELA - 45, 140, 35)
    mouse = pygame.mouse.get_pos()
    cor_btn = ROXO_ESCURO if btn_rect.collidepoint(mouse) else ROXO
    pygame.draw.rect(tela, cor_btn, btn_rect, border_radius=8)
    txt_btn = fonte_normal.render("Reiniciar", True, BRANCO)
    tela.blit(txt_btn, (btn_rect.centerx - txt_btn.get_width() // 2,
                        btn_rect.centery - txt_btn.get_height() // 2))

    return btn_rect


def tela_vitoria(tela, pontos, recorde, fonte_titulo, fonte_normal):
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    overlay.set_alpha(180)
    overlay.fill(ROXO_ESCURO)
    tela.blit(overlay, (0, 0))

    msg1 = fonte_titulo.render("VOCE GANHOU!! 🎉", True, AMARELO)
    msg2 = fonte_normal.render(f"Pares encontrados: {pontos // 10}", True, BRANCO)
    msg3 = fonte_normal.render("Aperte R para jogar de novo", True, CINZA)

    tela.blit(msg1, (LARGURA_TELA // 2 - msg1.get_width() // 2, ALTURA_TELA // 2 - 70))
    tela.blit(msg2, (LARGURA_TELA // 2 - msg2.get_width() // 2, ALTURA_TELA // 2))
    tela.blit(msg3, (LARGURA_TELA // 2 - msg3.get_width() // 2, ALTURA_TELA // 2 + 40))