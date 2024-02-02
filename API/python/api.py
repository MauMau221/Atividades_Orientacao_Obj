import requests

print('GitHub Useres')

username = input('Você gostaria de cotar euro, dólar ou bitcoin? ')
acesso = ''
if username.lower() == 'euro':
    username = 'EUR-BRL'
    acesso = 'EURBRL'
elif username.lower() == 'dolar':
    username = 'USD-BRL'
    acesso = 'USDBRL'
elif username.lower() == 'bitcoin':
    username = 'BTC-BRL'
    acesso = 'BTCBRL'

url = f'https://economia.awesomeapi.com.br/last/{username}'

response = requests.get(url)
data = response.json()
currency_data = data.get(acesso)

if response.status_code == 200:
    if currency_data and "name" in currency_data:
        print(f'Nome da moeda: {currency_data["name"]}')
    else:
        print(f'Dados inválidos ou chave "name" não encontrada para {acesso}.')
else:
    print(f'Erro na solicitação. Código de status: {response.status_code}')
