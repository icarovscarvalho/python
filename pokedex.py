#--------------------------------ID:001---------------------------
pokemons = {'bubasauro': {'nome': 'bubasauro',
                          'tipo': ('planta', 'veneno')},
            '1': {'nome': 'bubasauro',
                  'tipo': ('planta', 'veneno'),
                  'fraqueza': ('fogo', 'psiquico', 'gelo', 'voador')},
#--------------------------------ID:002---------------------------
            'ivysauro': {'nome': 'ivysauro',
                          'tipo': ('planta', 'veneno')},
            '2': {'nome': 'ivysauro',
                  'tipo': ('planta', 'veneno'),
                  'fraqueza': ('fogo', 'psiquico', 'gelo', 'voador')},
#--------------------------------ID:003---------------------------
            'venossauro': {'nome': 'venossauro',
                         'tipo': ('planta', 'veneno')},
            '3': {'nome': 'venossauro',
                  'tipo': ('planta', 'veneno'),
                  'fraqueza': ('fogo', 'psiquico', 'gelo', 'voador')},
#--------------------------------ID:004---------------------------
            'charmander': {'nome': 'charmander',
                           'tipo': ('planta', 'veneno'),
                           'fraqueza': ('agua', 'terrestre', 'pedra')},
            '4': {'nome': 'charmander',
                  'tipo': 'fogo',
                  'fraqueza': ('agua', 'terrestre', 'pedra')},
#--------------------------------ID:005---------------------------
            'charmeleon': {'nome': 'charmeleon',
                           'tipo': ('planta', 'veneno'),
                           'fraqueza': ('agua', 'terrestre', 'pedra')},
            '5': {'nome': 'charmeleon',
                  'tipo': 'fogo',
                  'fraqueza': ('agua', 'terrestre', 'pedra')},
#--------------------------------ID:006---------------------------
            'charizard': {'nome': 'charizard',
                           'tipo': ('planta', 'veneno'),
                           'fraqueza': ('agua', 'terrestre', 'pedra')},
            '6': {'nome': 'charizard',
                  'tipo': 'fogo',
                  'fraqueza': ('agua', 'terrestre', 'pedra')},
#--------------------------------ID:024---------------------------
            'pikachu': {'nome': 'pikachu',
                        'tipo': 'eletrico'},
            '24': {'nome': 'pikachu',
                   'tipo': 'eletrico'},
#--------------------------------ID:132---------------------------
            'eevee': {'nome': 'eevee',
                      'tipo': 'normal'},
            }

while True:
    busca = input(f'Escolha um pokemon ou digite o ID: ').lower().strip()
    if busca not in pokemons:
        print('Você deve escolher um ID de 1 à 151 ou digitar o nome do Pokemon corretamente!\n')
    # print(busca)
    if busca in pokemons:
        print(pokemons.get(busca))
        # sair = str(input('Quer escolher outro pokemon? [Y]/[N] ')).lower().strip()
        # print(sair)

        # if sair == 'y':
        #     continue
        # elif sair == 'n':
        #     break
        # else:
        #     print('Digite um valor válido!')