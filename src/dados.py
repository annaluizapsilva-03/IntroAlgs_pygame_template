import os

PARES = [
    ("🎬", "Breaking Bad"),
    ("🦁", "Rei Leao"),
    ("🕷", "Homem Aranha"),
    ("🐉", "Game of Thrones"),
    ("🚀", "Interestelar"),
    ("🦇", "Batman"), 
    ("🧙", "Harry Potter"),
    ("🌊", "Moana"),
]


def salvar_recorde(caminho, recorde):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w") as arquivo:
        arquivo.write(str(recorde))


def carregar_recorde(caminho):
    try:
        with open(caminho, "r") as arquivo:
            return int(arquivo.read())
    except:
        return 0
