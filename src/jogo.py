import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    LARGURA_CARTA,
    ALTURA_CARTA,
    COLUNAS,
    TEMPO_MOSTRAR,
    PONTOS_PAR,
    TEMPO_PARTIDA,
    TOTAL_FASES,
    PARES_INICIAIS,
    CARTAS_POR_FASE,
    REDUCAO_TEMPO_FASE,
)
from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    criar_cartas,
    calcular_tempo_restante,
    desenhar_hud,
    tela_inicial,
    tela_vitoria,
    tela_derrota,
    desenhar_fundo,
    iniciar_estrelas,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    PARES,
)


def pares_da_fase(fase):
    """Retorna a lista de pares (subconjunto de PARES) usada na fase indicada."""
    qtd_pares = PARES_INICIAIS + (fase - 1) * (CARTAS_POR_FASE // 2)
    qtd_pares = min(qtd_pares, len(PARES))
    return PARES[:qtd_pares]


def tempo_da_fase(fase):
    """Retorna o tempo total (em segundos) disponível para a fase indicada."""
    tempo = TEMPO_PARTIDA - (fase - 1) * REDUCAO_TEMPO_FASE
    return max(15, tempo)  # nunca deixa o tempo zerar ou ficar negativo


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    clock = pygame.time.Clock()

    fonte_titulo = pygame.font.SysFont("arial", 36, bold=True)
    fonte_normal = pygame.font.SysFont("arial", 18)
    fonte_carta  = pygame.font.SysFont("arial", 14, bold=True)
    fontes = (fonte_titulo, fonte_normal, fonte_carta)

    recorde = carregar_recorde(CAMINHO_RECORDE)

    estado = "inicio"

    fase           = 1
    pares_atuais   = pares_da_fase(fase)
    cartas         = []
    cartas_viradas = []
    pontos         = 0
    vidas          = 3
    tempo_inicio   = 0

    esperando_virar = False
    tempo_esperar   = 0

    rodando = True
    while rodando:
        clock.tick(FPS)
        tempo_atual = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    estado          = "inicio"
                    fase            = 1
                    pares_atuais    = pares_da_fase(fase)
                    cartas          = []
                    cartas_viradas  = []
                    pontos          = 0
                    vidas           = 3
                    esperando_virar = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                if estado == "inicio":
                    btn_jogar = pygame.Rect(LARGURA_TELA // 2 - 80, 420, 160, 45)
                    if btn_jogar.collidepoint(mx, my):
                        estado          = "jogando"
                        fase            = 1
                        pares_atuais    = pares_da_fase(fase)
                        cartas          = criar_cartas(pares_atuais, LARGURA_CARTA, ALTURA_CARTA, COLUNAS)
                        cartas_viradas  = []
                        pontos          = 0
                        vidas           = 3
                        tempo_inicio    = tempo_atual
                        esperando_virar = False

                elif estado == "jogando":
                    btn = pygame.Rect(LARGURA_TELA // 2 - 70, ALTURA_TELA - 45, 140, 35)
                    if btn.collidepoint(mx, my):
                        estado = "inicio"
                        continue

                    if not esperando_virar:
                        for i in range(len(cartas)):
                            carta = cartas[i]
                            rect_carta = pygame.Rect(carta["x"], carta["y"],
                                                    LARGURA_CARTA, ALTURA_CARTA)

                            if (rect_carta.collidepoint(mx, my)
                                    and not carta["virada"]
                                    and not carta["acertada"]):

                                carta["virada"] = True
                                cartas_viradas.append(i)

                                if len(cartas_viradas) == 2:
                                    i1 = cartas_viradas[0]
                                    i2 = cartas_viradas[1]

                                    if cartas[i1]["nome"] == cartas[i2]["nome"]:
                                        cartas[i1]["acertada"] = True
                                        cartas[i2]["acertada"] = True
                                        pontos = calcular_pontos(pontos, PONTOS_PAR)
                                        cartas_viradas = []

                                        # Verifica se a fase atual foi concluída
                                        if pontos // PONTOS_PAR == len(pares_atuais) * fase \
                                            if False else (sum(1 for c in cartas if c["acertada"]) == len(cartas)):
                                            if fase < TOTAL_FASES:
                                                fase           += 1
                                                pares_atuais     = pares_da_fase(fase)
                                                cartas           = criar_cartas(pares_atuais, LARGURA_CARTA, ALTURA_CARTA, COLUNAS)
                                                cartas_viradas   = []
                                                tempo_inicio     = tempo_atual
                                                esperando_virar  = False
                                            else:
                                                estado = "vitoria"
                                                if pontos > recorde:
                                                    recorde = pontos
                                                    salvar_recorde(CAMINHO_RECORDE, recorde)
                                    else:
                                        esperando_virar = True
                                        tempo_esperar   = tempo_atual

                                break

                elif estado in ("vitoria", "derrota"):
                    pass

        if esperando_virar and tempo_atual - tempo_esperar >= TEMPO_MOSTRAR:
            for i in cartas_viradas:
                cartas[i]["virada"] = False
            cartas_viradas  = []
            esperando_virar = False

        if estado == "jogando":
            tempo_restante = calcular_tempo_restante(tempo_inicio, tempo_da_fase(fase))
            if tempo_restante == 0:
                estado = "derrota"
                if pontos > recorde:
                    recorde = pontos
                    salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(TITULO_JOGO)

        if estado == "inicio":
            tela_inicial(tela, fonte_titulo, fonte_normal)

        elif estado == "jogando":
            tempo_restante = calcular_tempo_restante(tempo_inicio, tempo_da_fase(fase))
            desenhar_hud(tela, pontos, recorde, tempo_restante,
                         len(pares_atuais), pontos // PONTOS_PAR, fontes)
            for carta in cartas:
                from src.funcoes import desenhar_carta
                desenhar_carta(tela, carta, fonte_titulo, fonte_carta)

        elif estado == "vitoria":
            tempo_restante = calcular_tempo_restante(tempo_inicio, tempo_da_fase(fase))
            desenhar_hud(tela, pontos, recorde, tempo_restante,
                         len(pares_atuais), pontos // PONTOS_PAR, fontes)
            for carta in cartas:
                from src.funcoes import desenhar_carta
                desenhar_carta(tela, carta, fonte_titulo, fonte_carta)
            tela_vitoria(tela, pontos, recorde, fonte_titulo, fonte_normal)

        elif estado == "derrota":
            tempo_restante = calcular_tempo_restante(tempo_inicio, tempo_da_fase(fase))
            desenhar_hud(tela, pontos, recorde, tempo_restante,
                         len(pares_atuais), pontos // PONTOS_PAR, fontes)
            for carta in cartas:
                from src.funcoes import desenhar_carta
                desenhar_carta(tela, carta, fonte_titulo, fonte_carta)
            tela_derrota(tela, pontos, recorde, fonte_titulo, fonte_normal)

        pygame.display.update()

    pygame.quit()
    pygame.display.update()
 
    pygame.quit()
  
