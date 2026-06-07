# dados.py
# pares do jogo e funções de salvar/carregar recorde
# a coordenação já usa salvar_recorde e carregar_recorde no template

import os

# pares de filmes e séries (emoji, nome)
# cada item aparece 2 vezes no jogo
PARES = [
    ("🎬", "Breaking Bad"),
    ("🦁", "Rei Leao"),
    ("🕷", "Homem Aranha"),
    ("🐉", "Game of Thrones"),
    ("🚀", "Interestelar"),
    ("🤖", "Ex Machina"),
    ("🧙", "Harry Potter"),
    ("🌊", "Moana"),
]


def salvar_recorde(caminho, recorde):
    # salva o recorde num arquivo de texto
    # aprendi que precisa criar a pasta antes se não existir
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w") as arquivo:
        arquivo.write(str(recorde))


def carregar_recorde(caminho):
    # tenta ler o recorde do arquivo
    # se o arquivo não existir ainda, retorna 0
    try:
        with open(caminho, "r") as arquivo:
            return int(arquivo.read())
    except:
        return 0