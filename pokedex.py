pokemons = {'pikachu': {'nome': 'pikachu',
                        'tipo': 'eletrico'},
            '24': {'nome': 'pikachu',
                   'tipo': 'eletrico'},

            'eevee': {'nome': 'eevee',
                      'tipo': 'normal'}
            }

bubasauro = {'numero': 1,
             'nome': 'bubasauro',
             'tipo': ('planta', 'veneno'),
             'fraqueza': ('fogo', 'psiquico', 'gelo', 'voador'),
             'primeira_evolucao:': 'bubasauro',
             'segunda_evolucao': 'ivysauro',
             'terceira_evolucao': 'venossauro'}

ivysauro = {'numero': 2,
            'tipo': ('planta', 'veneno'),
            'fraqueza': ('fogo', 'psiquico', 'gelo', 'voador'),
            'primeira_evolucao:': 'bubasauro',
            'segunda_evolucao': 'ivysauro',
            'terceira_evolucao': 'venossauro'}

venosauro = {'numero': 3,
             'tipo': ('planta', 'veneno'),
             'fraqueza': ('fogo', 'psiquico', 'gelo', 'voador'),
             'primeira_evolucao:': 'bubasauro',
             'segunda_evolucao': 'ivysauro',
             'terceira_evolucao': 'venossauro'}

charmander = {'numero': 4,
              'tipo': 'fogo',
              'fraqueza': ('agua', 'terrestre', 'pedra'),
              'primeira_evolucao:': 'charmander',
              'segunda_evolucao': 'charmeleon',
              'terceira_evolucao': 'charizard'}

charmeleon = {'numero': 5,
              'tipo': 'fogo',
              'fraqueza': ('agua', 'terrestre', 'pedra'),
              'primeira_evolucao:': 'charmander',
              'segunda_evolucao': 'charmeleon',
              'terceira_evolucao': 'charizard'}

charizard = {'numero': 6,
             'tipo': 'fogo',
             'fraqueza': ('agua', 'terrestre', 'pedra'),
             'primeira_evolucao:': 'charmander',
             'segunda_evolucao': 'charmeleon',
             'terceira_evolucao': 'charizard'}

busca = input(f'Escolha um pokemon ou digite o ID: ')
print(busca)
if busca in pokemons:
    print(pokemons.get(busca))

# busca = input('Escolha um pokemon: ')
# print(busca)
# if busca in pokemons:
#     for i in pokemons.get(busca):
#         print(pokemons.get(i))

# busca = input('Escolha um pokemon: ')
# print(busca)
# if busca in pokemons:
#     for i in pokemons:
#         print(pokemons.get(i))
