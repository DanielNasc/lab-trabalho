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

def create_buttons_layout(start, end):
    return [
        [Text(f'Exercício {x}:'), Push(), Button('Run', key=f'E{x}'), Button('Info', key=f'B{x}')]
             for x in range(start, end + 1, 3)
        ]

# Primeira Coluna de Botões
layout_botoes_col1 = create_buttons_layout(1, 10)

# Segunda Coluna de Botões
layout_botoes_col2 = create_buttons_layout(2, 11)

# Terceira Coluna de Botões
layout_botoes_col3 = create_buttons_layout(3, 12)

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