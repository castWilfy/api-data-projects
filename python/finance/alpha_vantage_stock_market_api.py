import requests

symbol = 'ELF'
API_KEY = 'Insert Api key here'
url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'

response = requests.get(url)
data = response.json()

print(data)