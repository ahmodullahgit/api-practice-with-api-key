import requests
import json
url = 'https://restcountries.com/v2/all'
response = requests.get(url)
# print(response.status_code)
content = json.loads(response.content)

i = 0
while i <= 10:
    single_country = content[i]
    name = single_country.get('name')
    region = single_country.get('region')
    capital = single_country.get('alpha3Code')
    currency = single_country.get('currencies')[0].get('name')
    templete = f'{name} is the country of {region}. {capital} is the capital of {name}. The currency of {name} is {currency}.'
    print(templete)
    i += 1




