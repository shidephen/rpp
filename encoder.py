import uuid
from scanner import Symbol

def tostr(value):
    if isinstance(value, Symbol):
        return str(value)
    elif isinstance(value, str):
        return '"%s"' % value
    elif isinstance(value, uuid.UUID):
        return '{%s}' % value
    else:
        return str(value)

def encode(lists, indent=2, level=0):
    result = ''
    if any(isinstance(x, list) for x in lists):
        result += '<'
    for i, item in enumerate(lists):
        if i > 0:
            result += ' ' * (level + 1) * indent
        if all(not isinstance(x, list) for x in item):
            name, values = item[0], item[1:]
            strvalues = map(tostr, values)
            result += ' '.join([name] + strvalues) + '\n'
        else:
            result += encode(item, level=(level + 1))
    result += (' ' * level * indent) + '>\n'
    return result
