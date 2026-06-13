from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor, criar_cartas
from src.dados import salvar_recorde, carregar_recorde
import tempfile
import os

PARES_TESTE = [
    ("🎬", "Breaking Bad"),
    ("🦁", "Rei Leao"),
    ("🕷", "Homem Aranha"),
    ("🐉", "Game of Thrones"),
]


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_criar_cartas_quantidade_correta():
    """Deve criar o dobro de cartas em relacao aos pares fornecidos."""
    cartas = criar_cartas(PARES_TESTE, 140, 100, 4)
    assert len(cartas) == len(PARES_TESTE) * 2


def test_criar_cartas_viradas_para_baixo():
    """Todas as cartas devem comecar viradas para baixo."""
    cartas = criar_cartas(PARES_TESTE, 140, 100, 4)
    assert all(carta["virada"] is False for carta in cartas)


def test_criar_cartas_nao_acertadas():
    """Todas as cartas devem comecar como nao acertadas."""
    cartas = criar_cartas(PARES_TESTE, 140, 100, 4)
    assert all(carta["acertada"] is False for carta in cartas)


def test_criar_cartas_pares_presentes():
    """Cada par deve aparecer exatamente duas vezes no tabuleiro."""
    cartas = criar_cartas(PARES_TESTE, 140, 100, 4)
    nomes = [c["nome"] for c in cartas]
    for _, nome in PARES_TESTE:
        assert nomes.count(nome) == 2


def test_salvar_e_carregar_recorde():
    """Deve salvar e recuperar o recorde corretamente do arquivo."""
    with tempfile.TemporaryDirectory() as pasta:
        caminho = os.path.join(pasta, "sub", "recorde.txt")
        salvar_recorde(caminho, 40)
        assert carregar_recorde(caminho) == 40


def test_carregar_recorde_arquivo_inexistente():
    """Deve retornar zero quando o arquivo de recorde nao existir."""
    assert carregar_recorde("caminho/inexistente.txt") == 0