import PySimpleGUI as sg
from random import randint

MAX_ROWS = MAX_COL = 10

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
    # Nessa função vamos gerar as bombas aleatoriamente. Utilize a função randint
    pass

def gera_layout_tabuleiro():
    # Nessa função vamos gerar o layout do tabuleiro. Para isso precisaremos fazer for de linhas e colunas
    pass

# Gera o layout com os botões
layout =  [[sg.Button('?', size=(4, 2), key=(0,0), pad=(0,0)), sg.Button('?', size=(4, 2), key=(0,1), pad=(0,0)), sg.Button('?', size=(4, 2), key=(0,0), pad=(0,0))]]

window = sg.Window('Minesweeper', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # verifica se existe bomba na botão clicado
    if board[event[0]][event[1]]:
        print("Tem bomba")
window.close()