# python default function
"""
def increment(salary, increase = .1):
    salary = salary + (salary * increase)
    return salary
print(round(increment(50000, increase=.25)))
"""
from requests import get
import json

response = get('https://math.berkeley.edu/wp/wp-json/')
if response.status_code == 200:
    content = json.loads(response.content)
    name = content.get('name')
    description = content.get('description')
    time_zone = content.get('timezone_string')
    print(f'We\'re visiting the site, named {name}.\n Read some description about it: \n info: {description} \n Time Zone: {time_zone}')
else:
    print('fail')