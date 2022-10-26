import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response.status_code)
content = response.content
new_content = json.loads(content)
print(new_content)

"""
first : we have to import requests library
second : we can get our info from that site we have sent request
third : it needs to check that response code is 200 or not
fourth : we can get content but it will appear in 'bytes' class.
fifth : we need to loads our 'bytes' content in json and store it a variable
finally : we can print it.
"""


