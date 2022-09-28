from PySimpleGUI import (Window, Button, Text, Image, Input, 
Column, HSeparator, VSeparator, Push, popup, theme
)
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Tema
theme('Black')

layout_botoes_col1 = [
    [Text('Exercício 1:'), Push(), Button('Run', key='E1'), Button('Info', key='B1')],

    [Text('Exercício 4:'), Push(), Button('Run', key='E4'), Button('Info', key='B4')],

    [Text('Exercício 7:'), Push(), Button('Run', key='E7'), Button('Info', key='B7')],

    [Text('Exercício 10:'), Push(), Button('Run', key='E10'), Button('Info', key='B10')],

]

layout_botoes_col2 = [
    [Text('Exercício 2:'), Push(), Button('Run', key='E2'), Button('Info', key='B2')],

    [Text('Exercício 5:'), Push(), Button('Run', key='E5'), Button('Info', key='B5')],

    [Text('Exercício 8:'), Push(), Button('Run', key='E8'), Button('Info', key='B8')],

    [Text('Exercício 11:'), Push(), Button('Run', key='E11'), Button('Info', key='B11')],
]

layout_botoes_col3 = [
    [Text('Exercício 3:'), Push(), Button('Run', key='E3'), Button('Info', key='B3')],

    [Text('Exercício 6:'), Push(), Button('Run', key='E6'), Button('Info', key='B6')],

    [Text('Exercício 9:'), Push(), Button('Run', key='E9'), Button('Info', key='B9')],

    [Text('Exercício 12:'), Push(), Button('Run', key='E12'), Button('Info', key='B12')]
]

layout_vazio = [[]]

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

window = Window (
    'Ramon Supremacy',
    size=(1280, 720),
    layout=layout,
    element_justification='c'
)


while True:
    event, values = window.read()

    match(event):
        case 'B1':
            popup(f'Recebe dois numeros, mostra o maior e soma os dois.', image=('ramon.png'))
        case 'E1':
            os.startfile(f"{current_dir}\\ex1")
        
        case 'B2':
            popup(f'Recebe um nome de usuário e verifica se ele existe.', image=('ramon.png'))
        case 'E2':
            os.startfile(f"{current_dir}\\ex2")

        case 'B3':
            popup(f'Lista todos os arquivos e diretórios do diretóorio atual.', image=('ramon.png'))
        case 'E3':
            os.startfile(f"{current_dir}\\ex3")
        
        case 'B4':
            popup(f'Recebe um número e imprime todos os pares entre\n0 e o número digitado.')
        case 'E4':
            os.startfile(f"{current_dir}\\ex4")
        
        case 'B5':
            popup(f'Recebe o nome de um arquivo e mostra quantos bytes ele tem.')
        case 'E5':
            os.startfile(f"{current_dir}\\ex5")
        
        case 'B6':
            popup(f'Pequeno menu de 3 opções de listagem de recursos do sistema.')
        case 'E6':
            os.startfile(f"{current_dir}\\ex6")

        case 'B7':
            popup(f'Imprime todas as datas em que serão ministradas aulas.')
        case 'E7':
            os.startfile(f"{current_dir}\\ex7")

        case 'B8':
            popup(f'Substitui o nome de todos os arquivos do diretório,\npela palavra passada.')
        case 'E8':
            os.startfile(f"{current_dir}\\ex8")

        case 'B9':
            popup(f'Imprime ordenadamente todos os argumentos\npassados pelo usuário.')
        case 'E9':
            os.startfile(f"{current_dir}\\ex9")

        case 'B10':
            popup(f'Imprime ordenadamente palavras passadas pelo usuário.')
        case 'E10':
            os.startfile(f"{current_dir}\\ex10")

        case 'B11':
            popup(f'Recebe dois números e um operando, e realiza a operação.')
        case 'E11':
            os.startfile(f"{current_dir}\\ex11")

        case 'B12':
            popup(f'Apresenta os usuário do sistema e respectivos SHELLs.')
        case 'E12':
            os.startfile(f"{current_dir}\\ex12")

        case 'B13':
            popup(f'Recebe um número e imprime todos os pares entre\n0 e o número digitado.')
        case 'E13':
            os.startfile(f"{current_dir}\\ex13")

        case None:
            break

window.close()