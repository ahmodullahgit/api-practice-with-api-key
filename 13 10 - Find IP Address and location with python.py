"""
from requests import get
import json

ip_api = 'https://api.ipify.org?format=json'
response = get(ip_api)
if response.status_code == 200:
    content = json.loads(response.content)
    ip = content.get('ip')
else:
    print('Connection Error!')

ip_details = f'http://ip-api.com/json/{ip}'
response = get(ip_details)
if response.status_code == 200:
    content = json.loads(response.content)
    city = content.get('city')
    isp = content.get('isp')
    templete = f'Your ip address is {ip}. You are located in {city}. Your ISP is {isp}.'
    print(templete)
else:
    print('Connection Error!')
"""

# Converting into function:
from requests import get
import json

def request_content(url):
    response = get(url)
    if response.status_code == 200:
        content = json.loads(response.content)
    else:
        content = "Connection Error!"
    return content
ip_api = 'https://api.ipify.org?format=json'
# ip_content = request_content(ip_api)      output: {'ip': '103.172.29.37'} is a dict
ip = request_content(ip_api)['ip']
ip_details = f'http://ip-api.com/json/{ip}'
# ip_details_content = request_content(ip_details)
city = request_content(ip_details)['city']
isp = request_content(ip_details)['isp']
templete = f'Your ip address is {ip}. You are located in {city}. Your ISP is {isp}.'
print(templete)

