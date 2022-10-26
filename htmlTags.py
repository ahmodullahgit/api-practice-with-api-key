def paragraph_tag(paragraph):
    text = f'<p>{paragraph}</p>'
    return text
print(paragraph_tag('This is a paragraph tag'))

def heading_tag(heading):
    h1 = f'<h1>{heading}</h1>'
    h2 = f'<h2>{heading}</h2>'
    h3 = f'<h3>{heading}</h3>'
    h4 = f'<h4>{heading}</h4>'
    h5 = f'<h5>{heading}</h5>'
    h6 = f'<h6>{heading}</h6>'
    return h1, h2, h3, h4, h5, h6
print(heading_tag('This is a Heading One tag')[4])

def attribute(link, message):
    text = f'<a href="{link}">{message}</a>'
    return text
print(attribute('www.google.com','This is a link'))

def image(source, alt, width, height):
    text = f'<img src="{source}" alt="{alt}" width="{width}" height="{height}">'
    return text
print(image('www.google.com', 'google image', 124, 512))

def bold(paragraph):
    text = f'<b>{paragraph}</b>'
    return text
print(bold('This is a bold text'))
