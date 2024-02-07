import requests

epsodio = input('Você quer dados referente a qual epsodio? ')

url = (f'https://rickandmortyapi.com/api/character/{epsodio}')

response = requests.get(url)
responseJson = response.json()

print(responseJson)