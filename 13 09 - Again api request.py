from requests import get
import json
response = get('https://restcountries.com/v3.1/all')
# print(response.status_code)
content = json.loads(response.content)

print('Country Name \t\t\t Capital')
print('*'*33)
"""
i = 0
while i<= 10:
    single_country = content[i]
    name = single_country.get('name')
    capital = single_country.get('capital')
    print(name,'\t\t\t',capital)
    i += 1
"""
for couuntry_name in content:
    country = couuntry_name.get('name').get('official')
    capital = couuntry_name.get('capital')[0]
    print(f'{country} \t\t\t {capital}')