def greeting(name, msg="Good Morning"):
    text = f'Hi, {name}. {msg}'
    return text
print(greeting('Ahmod'))
print(greeting('Ahmod', msg='Good Evening'))

'''
def greeting(name, msg="Good Morning"):
    """
    this will return msg="Good Morning" as default function"
    :param name: it takes a name.
    :param msg: don't need to pass any argument; it will work by default.
    :return: it will return name and msg.
    """
'''