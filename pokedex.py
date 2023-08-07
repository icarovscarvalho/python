bubasauro = {'numero': 1, 'tipo': 'planta', 'poder': 'veneno', 'fraqueza': (
    'fogo', 'psiquico', 'gelo', 'voador'), 'primeira_evolucao:': 'bubasauro', 'segunda_evolucao': 'ivysauro', 'terceira_evolucao': 'venossauro'}

ivysauro= {'numero': 2, 'tipo': 'planta', 'poder': 'veneno', 'fraqueza': (
    'fogo', 'psiquico', 'gelo', 'voador'), 'primeira_evolucao:': 'bubasauro', 'segunda_evolucao': 'ivysauro', 'terceira_evolucao': 'venossauro'}

venosauro= {'numero': 3, 'tipo': 'planta', 'poder': 'veneno', 'fraqueza': (
    'fogo', 'psiquico', 'gelo', 'voador'), 'primeira_evolucao:': 'bubasauro', 'segunda_evolucao': 'ivysauro', 'terceira_evolucao': 'venossauro'}

charmander= {'numero': 4, 'tipo': 'fogo', 'poder': 'fogo', 'fraqueza': (
    'agua', 'terrestre', 'pedra'), 'primeira_evolucao:': 'charmander', 'segunda_evolucao': 'charmeleon', 'terceira_evolucao': 'charizard'}

charmander= {'numero': 4, 'tipo': 'fogo', 'poder': 'fogo', 'fraqueza': (
    'agua', 'terrestre', 'pedra'), 'primeira_evolucao:': 'charmander', 'segunda_evolucao': 'charmeleon', 'terceira_evolucao': 'charizard'}

charmeleon= {'numero': 5, 'tipo': 'fogo', 'poder': 'fogo', 'fraqueza': (
    'agua', 'terrestre', 'pedra'), 'primeira_evolucao:': 'charmander', 'segunda_evolucao': 'charmeleon', 'terceira_evolucao': 'charizard'}

charizard= {'numero': 6, 'tipo': 'fogo', 'poder': 'fogo', 'fraqueza': (
    'agua', 'terrestre', 'pedra'), 'primeira_evolucao:': 'charmander', 'segunda_evolucao': 'charmeleon', 'terceira_evolucao': 'charizard'}

pokemons = [bubasauro,ivysauro,venosauro,charmander,charmeleon,charizard]

print(pokemons[bubasauro]['numero'])

# print(bubasauro['tipo'])
# print(pokemons[0])

# print(bubasauro.values()) - Verificar os valores dentro da biblioteca
# print(bubasauro.keys()) - Verifica as categorias dentro da biblioteca
# print(bubasauro.itens()) - Verifica ambos grupos dentro da biblioteca

#for k,v in filme.itens(): - Para cada key in values
    #print(f'O {numero} é {1}) - Escreva isto