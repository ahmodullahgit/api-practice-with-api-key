
def Browser_Response_Codes(*args):
    for codes in args:
        if codes == '1xxs':
            print(f'{codes} = Information Response!')
        elif codes == '2xxs':
            print(f'{codes} = Success!')
        elif codes == '3xxs':
            print(f'{codes} = Redirection!')
        elif codes == '4xxs':
            print(f'{codes} = Client Errors!')
        elif codes == '5xxs':
            print(f'{codes} = Server Errors')
        else:
            print('You didn\'t enter any valid codes.')
Browser_Response_Codes('1xxs', '2xxs', '3xxs', '4xxs', '5xxs')


def browser_response_codes(*args):
    for code in args:
        if code == 200:
            print(f'{code} ----> Success!')
        elif code == 301:
            print(f'{code} ----> Permanent Redirection!')
        elif code == 302:
            print(f'{code} ----> Temporary Redirection!')
        elif code == 404:
            print(f'{code} ----> Not Found!')
        elif code == 410:
            print(f'{code} ----> Gone!')
        elif code == 500:
            print(f'{code} ----> Internal Server Error!')
        elif code == 503:
            print(f'{code} ----> Service Unavailable!')
        else:
            print('You didn\'t enter any valid code.')

browser_response_codes(200, 301, 302, 404, 410, 500, 503)

# Samrat vai given task:
X = 'a', 'b'
print(X)
print(type(X))

