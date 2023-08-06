import random
from time import sleep
import random as rd

# Código de Cores
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
end_color = '\033[m'

group = ['Pedra', 'Papel', 'Tesoura']
pontos = 0


def line():
    print('=-' * 20)


# Apresentação do jogo

while True:
    cont = 0

    for palavra in group:
        # sleep(1)
        print(f'{" "*(cont * 15)}{yellow}{group[cont]}{end_color}...')
        cont += 1
        if cont >= 3:
            break

# Tela de Escolha
    while True:
        player = ' '
        while player not in group:
            line()
            player = str(input('Faça sua escolha! ')).strip() .lower() .title()
            if player not in group:
                print(f'{red}ATENÇÃO{end_color} Escolha Pedra, Papel ou Tesoura!')
            print('_' * 40)

        print(f'Jogador escolheu: {blue}{player}{end_color}!')

        if player in group:
            pc = random.choice(group)
            print(f'O computador escolheu: {red}{pc}{end_color}')
            if pc == 'Pedra':
                print('_' * 40)
                if player == 'Pedra':
                    print(
                        f'Ambos jogaram {yellow}Pedra{end_color}. Deu {yellow}EMPATE{end_color}')
                elif player == 'Papel':
                    print(
                        f'{yellow}Pedra{end_color} perde de {yellow}Papel{end_color}. Você {yellow}GANHOU{end_color}')
                else:
                    print(
                        f'{yellow}Pedra{end_color} ganha de {yellow}Tesoura{end_color}. Você {yellow}PERDEU{end_color}')

            elif pc == 'Papel':
                print('_' * 40)
                if player == 'Papel':
                    print(
                        f'Ambos jogaram {yellow}Papel{end_color}. Deu {yellow}EMPATE{end_color}')
                elif player == 'Tesoura':
                    print(
                        f'{yellow}Papel{end_color} perde de {yellow}Tesoura{end_color}. Você {yellow}GANHOU{end_color}')
                else:
                    print(
                        f'{yellow}Papel{end_color} ganha de {yellow}Pedra{end_color}. Você {yellow}PERDEU{end_color}')

            else:
                print('_' * 40)
                if player == 'Tesoura':
                    print(
                        f'Ambos jogaram {yellow}Tesoura{end_color}. Deu {yellow}EMPATE{end_color}')
                elif player == 'Tesoura':
                    print(
                        f'{yellow}Tesoura{end_color} perde de {yellow}Pedra{end_color}. Você {yellow}GANHOU{end_color}')
                else:
                    print(
                        f'{yellow}Tesoura{end_color} ganha de {yellow}Papel{end_color}. Você {yellow}PERDEU{end_color}')
            pass

        line()

# Condição de Contnuidade do Jogo
        esc = str(input('Deseja continuar? [S/N] ').lower() .strip())

        if esc != 's':
            break
        else:
            print('\n'*3)
    break
