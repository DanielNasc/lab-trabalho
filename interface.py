import json
import re
from PySimpleGUI import (Window, Button, Input, Text, Image, Column, HSeparator, VSeparator, Push, popup, theme
)
import os
import subprocess
import platform

current_dir = os.path.dirname(os.path.realpath(__file__))

# Tema
theme('Black')
imagem = 'ufca.png'

# Layout Inicial
layout_inicial_esquerdo = [
    [Image(filename='user.png')],
]

layout_inicial_direito = [
    [Text('Senha:'), Push(), Input(password_char='*', key='SENHA')],
    [Push(), Button('Login!', key='L1')]
]

layout_inicial = [
    [Column(layout_inicial_esquerdo),
    VSeparator(),
    Column(layout_inicial_direito)]
]

# Janela Inicial
window_ini = Window (
    'Menu Inicial',
    layout=layout_inicial,
    element_justification='c'
)

while True:
    event, values = window_ini.read()
    if "L1" in event:
        if values['SENHA'] == 'zueira':
            imagem = 'ramon.png'
            break
        elif values['SENHA'] == 'ufca':
            imagem = 'avatar.png'
            break
        elif values['SENHA'] == 'tomato':
            imagem = 'malu.png'
            break
        elif values['SENHA'] == 'anonimous':
            imagem = 'ufca.png'
            break
        elif values['SENHA'] == 'kpoper':
            imagem = 'daniel.png'
            break
    elif event is None:
        break 

window_ini.close()

# Primeira Coluna de Botões
layout_botoes_col1 = [
    [Text('Exercício 1:'), Push(), Button('Run', key='E1'), Button('Info', key='B1')],

    [Text('Exercício 4:'), Push(), Button('Run', key='E4'), Button('Info', key='B4')],

    [Text('Exercício 7:'), Push(), Button('Run', key='E7'), Button('Info', key='B7')],

    [Text('Exercício 10:'), Push(), Button('Run', key='E10'), Button('Info', key='B10')],

]

# Segunda Coluna de Botões
layout_botoes_col2 = [
    [Text('Exercício 2:'), Push(), Button('Run', key='E2'), Button('Info', key='B2')],

    [Text('Exercício 5:'), Push(), Button('Run', key='E5'), Button('Info', key='B5')],

    [Text('Exercício 8:'), Push(), Button('Run', key='E8'), Button('Info', key='B8')],

    [Text('Exercício 11:'), Push(), Button('Run', key='E11'), Button('Info', key='B11')],
]

# Terceira Coluna de Botões
layout_botoes_col3 = [
    [Text('Exercício 3:'), Push(), Button('Run', key='E3'), Button('Info', key='B3')],

    [Text('Exercício 6:'), Push(), Button('Run', key='E6'), Button('Info', key='B6')],

    [Text('Exercício 9:'), Push(), Button('Run', key='E9'), Button('Info', key='B9')],

    [Text('Exercício 12:'), Push(), Button('Run', key='E12'), Button('Info', key='B12')]
]

# Coluna Vazia
layout_vazio = [[]]

# Layout Principal

layout = [
    [Text('Trabalho de Laboratório', font=('Bahnschrift 17'))],
    [HSeparator()],
    [HSeparator('')],
    [Image(filename= imagem, key='IMAGE')],
    [HSeparator()],
    [HSeparator('')],
    [HSeparator('')],
    [HSeparator('')],
    [Column(layout_botoes_col1),
    Column(layout_vazio),
    Column(layout_botoes_col2),
    Column(layout_vazio),
    Column(layout_botoes_col3)],
    [Text('Exercício 13: '), Button('Run', key='E13'), Button('Info', key='B13')]

]

# Janela Principal
window = Window (
    'Ramon Supremacy',
    size=(1280, 720),
    layout=layout,
    element_justification='c'
)

def execute(file):
    if platform.system() == "Windows":
        os.startfile(f"{current_dir}/{file}")
    else:
        command = f"gnome-terminal -- sh -c \"{current_dir}/{file}; read -p '\nPressione ENTER para sair...' REPLY \""
        subprocess.call(command, shell=True)

with open("./buttons.json", "r") as f:
    programs = json.load(f)

# Popups e Executáveis

while True:
    event, values = window.read()
    
    if "B" in event:
        popup(
                programs[event]["description"],
                title=programs[event]["title"],
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
    elif "E" in event:
        e_num = re.sub('[^0-9]', "", event)
        execute(f"ex{e_num}")
    elif event is None:
        break

# Fechar janela
window.close()