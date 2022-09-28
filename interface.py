from ctypes import alignment
from PySimpleGUI import (Window, Button, Text, Image, Input, 
Column, HSeparator, VSeparator, Push, popup, theme
)
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Tema
theme('Black')

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
    [Image(filename='avatar.png', key='IMAGE')],
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

# Popups e Executáveis
while True:
    event, values = window.read()

    match(event):
        case 'B1':
            popup(
                'Recebe dois numeros, mostra o maior e soma os dois.',
                title='Exercício 1',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
                #image='ramon.png' 
            )
        case 'E1':
            os.startfile(f"{current_dir}\\ex1")
        
        case 'B2':
            popup(
                'Recebe um nome de usuário e verifica se ele existe.',
                title='Exercício 2',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E2':
            os.startfile(f"{current_dir}\\ex2")

        case 'B3':
            popup(
                'Lista todos os arquivos e diretórios do diretório atual.',
                title='Exercício 3',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E3':
            os.startfile(f"{current_dir}\\ex3")
        
        case 'B4':
            popup(
                'Recebe um número e imprime todos os pares entre 0 e o número digitado.',
                title='Exercício 4',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E4':
            os.startfile(f"{current_dir}\\ex4")
        
        case 'B5':
            popup(
                'Recebe o nome de um arquivo e mostra quantos bytes ele tem.',
                title='Exercício 5',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E5':
            os.startfile(f"{current_dir}\\ex5")
        
        case 'B6':
            popup(
                'Pequeno menu de 3 opções de listagem de recursos do sistema.',
                title='Exercício 6',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E6':
            os.startfile(f"{current_dir}\\ex6")

        case 'B7':
            popup(
                'Imprime todas as datas em que serão ministradas aulas.',
                title='Exercício 7',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E7':
            os.startfile(f"{current_dir}\\ex7")

        case 'B8':
            popup(
                'Substitui o nome de todos os arquivos do diretório, pela palavra passada.',
                title='Exercício 8',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E8':
            os.startfile(f"{current_dir}\\ex8")

        case 'B9':
            popup(
                'Imprime ordenadamente todos os argumentos passados pelo usuário.',
                title='Exercício 9',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E9':
            os.startfile(f"{current_dir}\\ex9")

        case 'B10':
            popup(
                'Imprime ordenadamente palavras passadas pelo usuário.',
                title='Exercício 10',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E10':
            os.startfile(f"{current_dir}\\ex10")

        case 'B11':
            popup(
                'Recebe dois números e um operando, e realiza a operação.',
                title='Exercício 11',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E11':
            os.startfile(f"{current_dir}\\ex11")

        case 'B12':
            popup(
                'Apresenta os usuário do sistema e respectivos SHELLs.',
                title='Exercício 12',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E12':
            os.startfile(f"{current_dir}\\ex12")

        case 'B13':
            popup(
                'Recebe um número e imprime todos os pares entre 0 e o número digitado.',
                title='Exercício 13',
                background_color='#060814',
                line_width=50,
                custom_text='Voltar'
            )
        case 'E13':
            os.startfile(f"{current_dir}\\ex13")

        case None:
            break

# Fechar janela
window.close()