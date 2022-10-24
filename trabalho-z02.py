from random import randint

import PySimpleGUI as sg

MAX_ROWS = MAX_COL = 10
BOMBAS = 10

layout = []
# Matriz de 10 x 10 de bombas do campo minado 
board = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

def gera_bombas_aleatorias():
    # Nessa função vamos gerar as bombas aleatoriamente.
    # Utilize a função randint
    bomb = 0
    while bomb < BOMBAS:
        coluna = randint(0,9)
        linha = randint(0,9)

        if not tem_bomba(linha, coluna):
            board[linha][coluna] = 1
            bomb += 1
    print(board)

def tem_bomba(linha, coluna):
    if board[linha][coluna] == 1:
        return True
    return False


def gera_layout_tabuleiro():
    global layout
    for i in range(10):
        layout.append([])
        for j in range(10):
            layout[i].append(sg.Button('?', size=(4, 2), key=(i,j), pad=(0,0)))

#chamada de função gera bombas
gera_bombas_aleatorias()
gera_layout_tabuleiro()

window = sg.Window('Minesweeper', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # verifica se existe bomba na botão clicado
    if board[event[0]][event[1]]:
        print("Tem bomba")
    else:
        window[(event[0], event[1])].update('0',  button_color=('white','black'))
window.close()
