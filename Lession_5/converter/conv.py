import json

import requests

print('Конвертер валют')
amount = input('Введите сумму перевода: ').strip(' / .')
fromy = input('Введите валюту, из которой нужно конвертировать: ').strip(' / .')
to = input('Введите валюту, в которую нужно конвертировать: ').strip(' / .')
url = f"https://api.apilayer.com/fixer/convert?to={to}&from={fromy}&amount={amount}"

payload = {}
headers = {
    "apikey": "o6pRuF0ip59FM357amw082PwSphT86bj"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text
val_sum = json.loads(result)
# print(result)

print(val_sum['query'], sep=' ', end='\n')
print(f'{amount} в {fromy} = ', val_sum['result'], f'в {to}')
