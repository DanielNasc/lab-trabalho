import os
import subprocess
import re

# diretorio onde os arquivos python e bash estão
dir_path = os.path.dirname(os.path.realpath(__file__))

# TEMP ================================================

def print_array(arr):
    i = 0
    for elem in arr:
        print(f"{i} => {elem}")
        i+=1

def choose_program():
    print("\nDigite o numero do programa: ", end="")
    return int(input())

# =====================================================

def main():
    # pega todos os arquivos dos exercicios (os que começam com ex e tem um numero depois)
    program_list = sorted(
                            [ f for f in os.listdir(dir_path) if re.match(r'ex_?[0-9]', f) ], # array com todos os arquivos shell que começam com ex e têm um número depois
                            key=lambda elem: int(re.sub('[^0-9]', '', elem)) # função que retorna o número do arquivo, usada para ordenar o arrays
                        ) # array ordenado

    # [ PLACEHOLDERS | Luma troca depois pelas funções da interface ]
    print_array(program_list)
    selected_number = choose_program()
    selected_program = program_list[selected_number]

    test = subprocess.call(f"./{selected_program}", shell=True)


if __name__ == "__main__":
    main()