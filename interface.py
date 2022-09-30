import json
import re
from PySimpleGUI import (Window, Button, Input, Text, Image, Column, HSeparator, VSeparator, Push, popup, theme
)
import os
import subprocess
import platform

current_dir = os.path.dirname(os.path.realpath(__file__))

# Tema inicial
theme('DarkBlue2')
photo = 'ufca.png'

# Layout Inicial
left_home_layout= [
    [Image(filename='user.png')],
]

right_home_layout = [
    [Text('Senha:'), Push(), Input(password_char='*', key='SENHA')],
    [Push(), Button('Login!', key='L1')],
    [Text('Caso visitante: ufca'), Push()]
]

home_layout = [
    [Column(left_home_layout),
    VSeparator(),
    Column(right_home_layout)]
]

# Janela Inicial

home_window = Window (
    'Menu Inicial',
    layout=home_layout,
    element_justification='c'
)

while True:
    event, values = home_window.read()
    if "L1" in event:
        if values['SENHA'] == 'zueira':
            photo = 'ramon.png'
            break
        elif values['SENHA'] == 'ufca':
            photo = 'avatar.png'
            break
        elif values['SENHA'] == 'tomato':
            photo = 'malu.png'
            break
        elif values['SENHA'] == 'anonimous':
            photo = 'ufca.png'
            break
        elif values['SENHA'] == 'kpoper':
            photo = 'daniel.png'
            break
    elif event is None:
        break 

home_window.close()

# Tema inicial
theme('Black')

def create_buttons_layout(start, end):
    return [
        [Text(f'Exercício {x}:'), Push(), Button('Run', key=f'E{x}'), Button('Info', key=f'B{x}')]
             for x in range(start, end + 1, 3)
        ]

# Primeira Coluna de Botõess
button_layout_col1 = create_buttons_layout(1, 10)

# Segunda Coluna de Botões
button_layout_col2 = create_buttons_layout(2, 11)

# Terceira Coluna de Botões
button_layout_col3 = create_buttons_layout(3, 12)

# Coluna Vazia
empty_layout = [[]]

# Layout Principal
layout = [
    [Text('Trabalho de Laboratório', font=('Bahnschrift 17'))],
    [HSeparator()],
    [HSeparator('')],
    [Image(filename= photo, key='IMAGE')],
    [HSeparator()],
    [HSeparator('')],
    [HSeparator('')],
    [HSeparator('')],
    [Column(button_layout_col1),
    Column(empty_layout),
    Column(button_layout_col2),
    Column(empty_layout),
    Column(button_layout_col3)],
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