import random

pontos = 0

while True:
    print('=-' * 10)
    player = str(input('Você quer PAR [P] ou ÍMPAR [I]?  ')).upper().strip()
    num = int(input('Escolha um número: '))
    pc_num = random.randint(0, 10)
    total = pc_num + num
    print('--'*10)

    if player == 'P':
        if total % 2 == 0:
            print(f'O \033[1;34mJOGADOR\033[m escolheu: \033[1;34m{num}\033[m')
            print(f'O \033[1;31mPC\033[m escolheu: \033[1;31m{pc_num}\033[m')
            print('Deu \033[1;33mPAR\033[m')
            print(f'\n\033[1;34mJOGADOR ganhou\033[m')
            pontos += 1
        else:
            print(f'O \033[1;34mJOGADOR\033[m escolheu: \033[1;34m{num}\033[m')
            print(f'O \033[1;31mPC\033[m escolheu: \033[1;31m{pc_num}\033[m')
            print('Deu \033[1;33mÍMPAR\033[m')
            print(f'\n\033[1;31mPC ganhou\033[m')
            break
    else:
        if total % 2 == 1:
            print(f'O \033[1;34mJOGADOR\033[m escolheu: \033[1;34m{num}\033[m')
            print(f'O \033[1;31mPC\033[m escolheu: \033[1;31m{pc_num}\033[m')
            print('Deu \033[1;33mÍMPAR\033[m')
            print(f'\n\033[1;34mJOGADOR ganhou\033[m')
            pontos += 1
        else:
            print(f'O \033[1;34mJOGADOR\033[m escolheu: \033[1;34m{num}\033[m')
            print(f'O \033[1;31mPC\033[m escolheu: \033[1;31m{pc_num}\033[m')
            print('Deu \033[1;33mPAR\033[m')
            print(f'\n\033[1;31mPC ganhou\033[m')
            break

print(f'\nVocê ganhou \033[1;33m{pontos}\033[m vezes!')
