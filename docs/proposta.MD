# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Memória Cinematográfica

Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1:Anna Luiza Pereira Silva
- Nome 2:Priscila Louzada
- Nome 3:
- Nome 4:

## 3. Tipo de jogo

Jogo da Memória

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

Jogo da Memória

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:
O jogo consiste em um tabuleiro com cartas viradas para baixo. Cada carta possui uma imagem relacionada a filmes e séries populares. O jogador deve virar duas cartas por vez e tentar encontrar os pares correspondentes. O objetivo é encontrar todos os pares com o menor número possível de tentativas e no menor tempo possível.


## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

Encontrar todos os pares de cartas do tabuleiro antes que o tempo acabe.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1:Todas as cartas começam viradas para baixo.
- Regra 2:O jogador pode selecionar duas cartas por jogada.
- Regra 3:Se as cartas formarem um par, elas permanecem visíveis
- Regra 4:Se não formarem um par, elas voltam a ficar viradas para baixo após alguns segundos.
- Regra 5:O jogo continua até que todos os pares sejam encontrados ou o tempo termine.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

Encontrar todos os pares de cartas antes do fim do tempo.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

O tempo acaba antes que todos os pares sejam encontrados.

## 9. Elementos previstos no jogo

* Cartas de filmes e séries.
* Cronômetro.
* Sistema de pontuação.
* Contador de tentativas.
* Tela inicial.
* Tela de vitória.
* Tela de derrota.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

O jogador deve encontrar os pares de cartas iguais contendo imagens ou nomes de filmes e séries. As cartas ficam viradas para baixo e podem ser reveladas duas por vez.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:
O principal desafio é memorizar a posição das cartas e encontrar todos os pares antes que o tempo termine. O jogador perde pontos ao selecionar cartas que não formam um par

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:
Cartas contendo imagens ou títulos de filmes e séries. O jogador interage com elas para revelar seu conteúdo e encontrar os pares correspondentes.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

O jogador ganha 5 pontos para cada par encontrado. O jogo possui um cronômetro de 3 minutos e termina quando todos os pares forem encontrados ou quando o tempo acabar. O progresso é medido pela quantidade de pares completados

## 10. Controles previstos

* Mouse para selecionar as cartas.
* Botão para reiniciar o jogo.


Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando:
- Tecla/comando:
- Tecla/comando:

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

O projeto será organizado em módulos para facilitar a manutenção e compreensão do código:

* main.py – arquivo principal responsável por iniciar o jogo.
* game.py – lógica principal do jogo da memória.
* cards.py – gerenciamento das cartas e suas propriedades.
* score.py – controle de pontuação e recordes.
* utils.py – funções auxiliares.
* assets/images – imagens das cartas, filmes e séries.
* assets/sounds – efeitos sonoros.
* tests/ – testes das funções principais.



## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:
* Biblioteca Pygame.
* Imagens de filmes e séries livres para uso acadêmico ou criadas pelo grupo.
* Ícones gratuitos obtidos em bancos de imagens livres.
* Efeitos sonoros gratuitos para acertos, erros e vitória.
* Fontes gratuitas para interface do jogo.

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

* Implementar corretamente a lógica de comparação das cartas.
* Controlar o tempo de exibição quando duas cartas diferentes forem selecionadas.
* Embaralhar as cartas sem comprometer a formação dos pares.
* Desenvolver uma interface organizada e intuitiva.
* Salvar e recuperar recordes utilizando arquivos.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1:
- Dificuldade 2:
- Dificuldade 3:

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

* Tela inicial.
* Tabuleiro com cartas embaralhadas.
* Cartas de filmes e séries.
* Sistema de clique utilizando o mouse.
* Verificação automática de pares.
* Sistema de pontuação.
* Cronômetro da partida.
* Tela de vitória.
* Tela de derrota.
* Salvamento do recorde em arquivo.
* Código modularizado e documentado.
* Testes básicos das funções principais.


## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1:Diferentes níveis de dificuldade.
- Melhoria 2:Sistema de ranking com vários jogadores.
- Melhoria 3:Escolha do tema na tela inicial.