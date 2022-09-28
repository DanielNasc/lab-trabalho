from PySimpleGUI import (Window, Button, Text, Image, Input, 
Column, VSeparator, Push, popup, theme
)

theme('Black')
font = ("Helvetica", 11)

layout = [
    [Image(filename='avatar.png')],
    [Text('Trabalho de Laboratório', size=(20, 1), font=font)]
]

window = Window (
    'Ramon Supremacy',
    layout=layout,
    element_justification='c'
)

window.read()

window.close()