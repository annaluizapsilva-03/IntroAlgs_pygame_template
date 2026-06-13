import pygame

from src.config import (
    LARGURA_TELA, ALTURA_TELA,
    LARGURA_CARTA, ALTURA_CARTA,
    ROXO, ROXO_ESCURO, BRANCO, PRETO,
    VERDE, AMARELO, VERMELHO, CINZA, FUNDO,
    TEMPO_PARTIDA,
)
import random

_estrelas = []

def iniciar_estrelas():
    global _estrelas
    _estrelas = [
        {
            "x": random.randint(0, LARGURA_TELA),
            "y": random.randint(0, ALTURA_TELA),
            "r": random.randint(1, 3),
            "brilho": random.randint(100, 255),
            "vel": random.uniform(0.3, 1.0),
        }
        for _ in range(80)
    ]

def desenhar_fundo(tela):
   
    global _estrelas

    for y in range(ALTURA_TELA):
        ratio = y / ALTURA_TELA
        r = int(10  + ratio * 40)
        g = int(0   + ratio * 10)
        b = int(40  + ratio * 60)
        pygame.draw.line(tela, (r, g, b), (0, y), (LARGURA_TELA, y))

    for e in _estrelas:
        e["brilho"] += e["vel"] * random.choice([-1, 1]) * 3
        e["brilho"] = max(80, min(255, e["brilho"]))
        cor = (e["brilho"], e["brilho"], int(e["brilho"] * 0.8))
        pygame.draw.circle(tela, cor, (e["x"], e["y"]), e["r"])
  
def calcular_pontos(pontos_atuais, bonus):
    return pontos_atuais + bonus
 
 
def jogador_perdeu(vidas):
    return vidas <= 0
 
 
def limitar_valor(valor, minimo, maximo):
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor
 
 
def verificar_colisao(rect1, rect2):
    return rect1.colliderect(rect2)
 
 
def tomar_dano(vidas, dano):
    return vidas - dano
 
def criar_cartas(pares, largura_carta, altura_carta, colunas):
    import random
    todas = pares + pares
    random.shuffle(todas)
 
    espaco_x = (LARGURA_TELA - colunas * largura_carta) // (colunas + 1)
    espaco_y = 20
    inicio_y = 120
 
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
 
 
def calcular_tempo_restante(tempo_inicio):
    
    tempo_passado = (pygame.time.get_ticks() - tempo_inicio) // 1000
    return max(0, TEMPO_PARTIDA - tempo_passado)
 
def desenhar_carta(tela, carta, fonte_titulo, fonte_carta):
    x = carta["x"]
    y = carta["y"]
    cx = x + LARGURA_CARTA // 2
    cy = y + ALTURA_CARTA  // 2

    if carta["acertada"]:
        # Fundo verde com brilho
        pygame.draw.rect(tela, (80, 200, 100), (x, y, LARGURA_CARTA, ALTURA_CARTA), border_radius=10)
        pygame.draw.rect(tela, (50, 150, 70),  (x, y, LARGURA_CARTA, ALTURA_CARTA), 3, border_radius=10)
        txt = fonte_carta.render(carta["nome"], True, PRETO)
        tela.blit(txt, (cx - txt.get_width()//2, cy - txt.get_height()//2))

    elif carta["virada"]:
        # Fundo branco
        pygame.draw.rect(tela, BRANCO,      (x, y, LARGURA_CARTA, ALTURA_CARTA), border_radius=10)
        pygame.draw.rect(tela, ROXO_ESCURO, (x, y, LARGURA_CARTA, ALTURA_CARTA), 3, border_radius=10)

        # Ícone desenhado por nome
        _desenhar_icone(tela, carta["nome"], cx, cy - 10)

        txt = fonte_carta.render(carta["nome"], True, ROXO_ESCURO)
        tela.blit(txt, (cx - txt.get_width()//2, y + ALTURA_CARTA - 22))

    else:
        # Carta virada — fundo roxo com padrão de filme
        pygame.draw.rect(tela, (120, 80, 180), (x, y, LARGURA_CARTA, ALTURA_CARTA), border_radius=10)
        pygame.draw.rect(tela, ROXO_ESCURO,    (x, y, LARGURA_CARTA, ALTURA_CARTA), 3, border_radius=10)
        # Tira de filme decorativa
        pygame.draw.rect(tela, (80, 40, 120), (x+8, y+8, LARGURA_CARTA-16, 14), border_radius=3)
        pygame.draw.rect(tela, (80, 40, 120), (x+8, ALTURA_CARTA+y-22, LARGURA_CARTA-16, 14), border_radius=3)
        for fx in range(x+14, x+LARGURA_CARTA-14, 16):
            pygame.draw.rect(tela, (160, 120, 220), (fx, y+10, 10, 10), border_radius=2)
            pygame.draw.rect(tela, (160, 120, 220), (fx, ALTURA_CARTA+y-20, 10, 10), border_radius=2)
        # Ponto de interrogação
        ponto = fonte_titulo.render("?", True, BRANCO)
        tela.blit(ponto, (cx - ponto.get_width()//2, cy - ponto.get_height()//2))


def _desenhar_icone(tela, nome, cx, cy):
    if nome == "Breaking Bad":
        pygame.draw.rect(tela, (200, 230, 100), (cx-8, cy-18, 16, 22), border_radius=3)
        pygame.draw.rect(tela, (150, 180, 60),  (cx-5, cy-22, 10, 6),  border_radius=2)
        pygame.draw.circle(tela, (100, 220, 80), (cx, cy+2), 6)

    elif nome == "Rei Leao":
        pygame.draw.circle(tela, (255, 200, 0), (cx, cy), 12)
        for ang in range(0, 360, 45):
            import math
            rx = cx + int(18 * math.cos(math.radians(ang)))
            ry = cy + int(18 * math.sin(math.radians(ang)))
            pygame.draw.line(tela, (255, 160, 0), (cx, cy), (rx, ry), 2)

    elif nome == "Homem Aranha":
        pygame.draw.circle(tela, (220, 30, 30), (cx, cy), 14, 2)
        pygame.draw.line(tela, (220, 30, 30), (cx-14, cy), (cx+14, cy), 2)
        pygame.draw.line(tela, (220, 30, 30), (cx, cy-14), (cx, cy+14), 2)
        pygame.draw.line(tela, (220, 30, 30), (cx-10, cy-10), (cx+10, cy+10), 2)
        pygame.draw.line(tela, (220, 30, 30), (cx+10, cy-10), (cx-10, cy+10), 2)

    elif nome == "Game of Thrones":
        pontos = [
            (cx-14, cy+8), (cx-14, cy-4), (cx-8,  cy-12),
            (cx,    cy-4), (cx+8,  cy-12),(cx+14, cy-4),
            (cx+14, cy+8),
        ]
        pygame.draw.polygon(tela, (220, 180, 0), pontos)
        pygame.draw.polygon(tela, (180, 140, 0), pontos, 2)

    elif nome == "Interestelar":
        pygame.draw.circle(tela, (100, 150, 220), (cx, cy), 10)
        pygame.draw.ellipse(tela, (180, 200, 255), (cx-18, cy-5, 36, 10), 2)

    elif nome == "Ex Machina":
        pygame.draw.rect(tela, (180, 180, 200), (cx-10, cy-14, 20, 22), border_radius=4)
        pygame.draw.circle(tela, (0, 200, 255), (cx-4, cy-6), 3)
        pygame.draw.circle(tela, (0, 200, 255), (cx+4, cy-6), 3)
        pygame.draw.line(tela, (100, 100, 120), (cx-5, cy+4), (cx+5, cy+4), 2)

    elif nome == "Harry Potter":
        pygame.draw.line(tela, (180, 120, 60), (cx-12, cy+12), (cx+8, cy-8), 3)
        pygame.draw.circle(tela, (255, 240, 100), (cx+10, cy-10), 5)

    elif nome == "Moana":
        import math
        pontos_onda = [
            (cx - 14 + i, cy + int(8 * math.sin(math.radians(i * 20))))
            for i in range(29)
        ]
        if len(pontos_onda) > 1:
            pygame.draw.lines(tela, (0, 150, 220), False, pontos_onda, 3)
        pygame.draw.circle(tela, (255, 200, 50), (cx, cy-10), 7)
 
def desenhar_hud(tela, pontos, recorde, tempo_restante, total_pares, pares_certos, fontes):
    fonte_titulo, fonte_normal, fonte_carta = fontes
 
    desenhar_fundo(tela)

    titulo = fonte_titulo.render("Memoria Cinematografica", True, ROXO_ESCURO)
    titulo_x = LARGURA_TELA // 2 - titulo.get_width() // 2
    tela.blit(titulo, (titulo_x, 10))
 
    minutos  = tempo_restante // 60
    segundos = tempo_restante % 60
 
    if tempo_restante <= 30:
        cor_tempo = VERMELHO
    else:
        cor_tempo = ROXO_ESCURO
 
    txt_tempo = fonte_normal.render(f"Tempo: {minutos:02d}:{segundos:02d}", True, cor_tempo)
    tempo_x = LARGURA_TELA // 2 - txt_tempo.get_width() // 2
    tela.blit(txt_tempo, (tempo_x, 50))
 
    txt_pont = fonte_normal.render(f"Pontos: {pontos}", True, ROXO_ESCURO)
    txt_rec  = fonte_normal.render(f"Recorde: {recorde}", True, ROXO_ESCURO)
    tela.blit(txt_pont, (20, 15))
    tela.blit(txt_rec,  (20, 40))
 
    txt_pares = fonte_normal.render(f"Pares: {pares_certos}/{total_pares}", True, ROXO_ESCURO)
    pares_x = LARGURA_TELA - txt_pares.get_width() - 20
    tela.blit(txt_pares, (pares_x, 15))
 
    btn_rect = pygame.Rect(LARGURA_TELA // 2 - 70, ALTURA_TELA - 45, 140, 35)
 
    mouse = pygame.mouse.get_pos()
    if btn_rect.collidepoint(mouse):
        cor_btn = ROXO_ESCURO
    else:
        cor_btn = ROXO
 
    pygame.draw.rect(tela, cor_btn, btn_rect, border_radius=8)
    txt_btn = fonte_normal.render("Reiniciar (R)", True, BRANCO)
    btn_texto_x = btn_rect.centerx - txt_btn.get_width() // 2
    btn_texto_y = btn_rect.centery - txt_btn.get_height() // 2
    tela.blit(txt_btn, (btn_texto_x, btn_texto_y))
 
    return btn_rect
 
def tela_inicial(tela, fonte_titulo, fonte_normal):

    tela.fill(FUNDO)
 
    titulo = fonte_titulo.render("Memoria Cinematografica", True, ROXO_ESCURO)
    sub    = fonte_normal.render("Encontre todos os pares antes do tempo acabar!", True, ROXO)
    inst1  = fonte_normal.render("Clique em duas cartas para revelar", True, PRETO)
    inst2  = fonte_normal.render("Pares corretos valem 5 pontos", True, PRETO)
    inst3  = fonte_normal.render("Voce tem 3 minutos!", True, PRETO)
 
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 100))
    tela.blit(sub,    (LARGURA_TELA // 2 - sub.get_width() // 2, 170))
    tela.blit(inst1,  (LARGURA_TELA // 2 - inst1.get_width() // 2, 260))
    tela.blit(inst2,  (LARGURA_TELA // 2 - inst2.get_width() // 2, 300))
    tela.blit(inst3,  (LARGURA_TELA // 2 - inst3.get_width() // 2, 340))
 
    btn = pygame.Rect(LARGURA_TELA // 2 - 80, 420, 160, 45)
 
    mouse = pygame.mouse.get_pos()
    if btn.collidepoint(mouse):
        cor_btn = ROXO_ESCURO
    else:
        cor_btn = ROXO
    pygame.draw.rect(tela, cor_btn, btn, border_radius=10)
 
    txt_btn = fonte_normal.render("JOGAR", True, BRANCO)
    btn_texto_x = btn.centerx - txt_btn.get_width() // 2
    btn_texto_y = btn.centery - txt_btn.get_height() // 2
    tela.blit(txt_btn, (btn_texto_x, btn_texto_y))
 
    return btn
 
def tela_vitoria(tela, pontos, recorde, fonte_titulo, fonte_normal):
  
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    overlay.set_alpha(190)
    overlay.fill(ROXO_ESCURO)
    tela.blit(overlay, (0, 0))
 
    msg1 = fonte_titulo.render("VOCE GANHOU!! 🎉", True, AMARELO)
    msg2 = fonte_normal.render(f"Pontuacao: {pontos} pontos", True, BRANCO)
    msg3 = fonte_normal.render(f"Recorde: {recorde} pontos", True, BRANCO)
    msg4 = fonte_normal.render("Pressione R para jogar de novo", True, CINZA)
 
    meio_x = LARGURA_TELA // 2
    meio_y = ALTURA_TELA // 2
 
    tela.blit(msg1, (meio_x - msg1.get_width() // 2, meio_y - 90))
    tela.blit(msg2, (meio_x - msg2.get_width() // 2, meio_y - 10))
    tela.blit(msg3, (meio_x - msg3.get_width() // 2, meio_y + 30))
    tela.blit(msg4, (meio_x - msg4.get_width() // 2, meio_y + 80))
 
 
def tela_derrota(tela, pontos, recorde, fonte_titulo, fonte_normal):
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    overlay.set_alpha(190)
    overlay.fill((80, 20, 20))
    tela.blit(overlay, (0, 0))
 
    msg1 = fonte_titulo.render("TEMPO ESGOTADO!", True, VERMELHO)
    msg2 = fonte_normal.render(f"Voce fez {pontos} pontos", True, BRANCO)
    msg3 = fonte_normal.render(f"Recorde: {recorde} pontos", True, BRANCO)
    msg4 = fonte_normal.render("Pressione R para tentar de novo", True, CINZA)
 
    tela.blit(msg1, (LARGURA_TELA // 2 - msg1.get_width() // 2, ALTURA_TELA // 2 - 90))
    tela.blit(msg2, (LARGURA_TELA // 2 - msg2.get_width() // 2, ALTURA_TELA // 2 - 10))
    tela.blit(msg3, (LARGURA_TELA // 2 - msg3.get_width() // 2, ALTURA_TELA // 2 + 30))
    tela.blit(msg4, (LARGURA_TELA // 2 - msg4.get_width() // 2, ALTURA_TELA // 2 + 80))
 