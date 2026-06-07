import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CAMINHO_RECORDE,
    LARGURA_CARTA,
    ALTURA_CARTA,
    COLUNAS,
    TEMPO_MOSTRAR,
)
from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    criar_cartas,
    desenhar_tela,
    tela_vitoria,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    PARES,
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    clock = pygame.time.Clock()

    # fontes
    fonte_titulo = pygame.font.SysFont("arial", 36, bold=True)
    fonte_normal = pygame.font.SysFont("arial", 18)
    fonte_carta  = pygame.font.SysFont("arial", 14, bold=True)
    fontes = (fonte_titulo, fonte_normal, fonte_carta)

    # estado do jogo
    cartas         = criar_cartas(PARES, LARGURA_CARTA, ALTURA_CARTA, COLUNAS)
    cartas_viradas = []
    pontos         = 0
    vidas          = 3
    recorde        = carregar_recorde(CAMINHO_RECORDE)
    ganhou         = False

    esperando_virar = False
    tempo_esperar   = 0

    rodando = True
    while rodando:
        clock.tick(FPS)
        tempo_atual = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            # tecla R reinicia
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    cartas          = criar_cartas(PARES, LARGURA_CARTA, ALTURA_CARTA, COLUNAS)
                    cartas_viradas  = []
                    pontos          = 0
                    vidas           = 3
                    ganhou          = False
                    esperando_virar = False

            # clique do mouse nas cartas
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                # botão reiniciar
                btn = pygame.Rect(LARGURA_TELA // 2 - 70, ALTURA_TELA - 45, 140, 35)
                if btn.collidepoint(mx, my):
                    cartas          = criar_cartas(PARES, LARGURA_CARTA, ALTURA_CARTA, COLUNAS)
                    cartas_viradas  = []
                    pontos          = 0
                    vidas           = 3
                    ganhou          = False
                    esperando_virar = False
                    continue

                # só vira carta se não estiver esperando e não tiver ganhado
                if not esperando_virar and not ganhou:
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
                                    pontos = calcular_pontos(pontos, 10)
                                    cartas_viradas = []

                                    if pontos // 10 == len(PARES):
                                        ganhou = True
                                else:
                                    esperando_virar = True
                                    tempo_esperar   = tempo_atual

                            break

        # vira as cartas erradas de volta depois do tempo de espera
        if esperando_virar and tempo_atual - tempo_esperar >= TEMPO_MOSTRAR:
            for i in cartas_viradas:
                cartas[i]["virada"] = False
            cartas_viradas  = []
            esperando_virar = False

        # salva recorde se bateu
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pares: {pontos // 10} | Recorde: {recorde // 10}"
        )

        desenhar_tela(tela, cartas, pontos, recorde, fontes)

        if ganhou:
            tela_vitoria(tela, pontos, recorde, fonte_titulo, fonte_normal)

        pygame.display.update()

    pygame.quit()