# Memória Cinematrográfica

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Priscilla Louzada Nesio
- Anna Luiza Silva
  
## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Um jogo da memória consiste em encontrar pares de cartas iguais que estão viradas para baixo. 
O jogador escolhe duas cartas por rodada e, se as cartas forem iguais, elas permanecem abertas; caso contrário, são escondidas novamente.
O objetivo principal do jogo é exercitar a memória e completar todos os pares no menor número de tentaivas possível e com um tempo menor a cada nível concluído, utilizando conceitos de programação.

## Objetivo do jogador

O objetivo do jogador é encontrar todos os pares de cartas iguais, usando a memória para lembrar a posição de cada carta e completar o jogo com o menor número possível de tentativas e tempo limitado. 

## Regras do jogo

Liste as principais regras do jogo.

- Todas as cartas começam viradas para baixo.
- As cartas contém séries e filmes diversos. 
- O jogador deve escolher duas cartas por rodada.
- Se as duas cartas forem iguais, elas permanecem viradas para cima.
- Se as duas cartas forem diferentes, as cartas são viradas para baixo novamente.
- O jogador deve memorizar as posições das cartas para encontrar os pares mais rápido.
- O jogo termina quando todos os pares forem encontrados.
- Se o jogador não conseguir concluir a fase juntando todos os pares no tempo correto, o jogo deverá ser reiniciado.
- A cada fase avançada, vão se adicionando 2 cartas e diminuindo 15 segundos do tempo inicial (1 minuto e 30 segundos).
- A cada fase que for completada, o jogador ganha 5 pontos (15 pontos no total).
- São 3 fases no total, ganha quem encontrar todos os pares em todos os níveis dentro do limite de tempo.

## Controles

- Mouse (clicar para virar as cartas e avançar de fase).

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
