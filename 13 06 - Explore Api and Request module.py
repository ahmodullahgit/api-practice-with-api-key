import requests
response = requests.get('https://www.python.org')
print(b'to promote, protect, and advance the Python' in response.content)
print(response.status_code)
print(response.content)