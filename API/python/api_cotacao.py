import requests

print('GitHub Useres')

coin = input('Você gostaria de cotar euro, dólar ou bitcoin? ')
acesso = ''
if coin.lower() == 'euro':
    coin = 'EUR-BRL'
    acesso = 'EURBRL'
elif coin.lower() == 'dolar':
    coin = 'USD-BRL'
    acesso = 'USDBRL'
elif coin.lower() == 'bitcoin':
    coin = 'BTC-BRL'
    acesso = 'BTCBRL'

url = f'https://economia.awesomeapi.com.br/last/{coin}'

response = requests.get(url)
data = response.json()
currency_data = data.get(acesso)

if response.status_code == 200:
    if currency_data and "name" in currency_data:
        print(f'Nome da moeda: {currency_data["name"]}')
    if currency_data and "low" in currency_data:
        print(f'Atual cotação da moeda: {currency_data["low"]}')
    else:
        print(f'Dados inválidos ou chave "name" não encontrada para {acesso}.')
else:
    print(f'Erro na solicitação. Código de status: {response.status_code}')
