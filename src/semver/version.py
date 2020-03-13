
def parse_version(version):
    return version[1:].split('.')

def inc_patch(version):
    a, b, c = parse_version(version)
    c = str(int(c)+1)
    return 'v' + '.'.join([a, b, c])

def inc_minor(version):
    a,b,c = parse_version(version)
    b = str(int(b)+1)
    c = '0'
    return 'v' + '.'.join([a, b, c])

def inc_major(version):
    a,b,c = parse_version(version)
    a = str(int(a)+1)
    b, c = '0', '0'
    return 'v' + '.'.join([a, b, c])

def increment(version, tag):
    new_tag = tag
    if version == 'major':
        new_tag = inc_major(tag)
    elif version == 'minor':
        new_tag = inc_minor(tag)
    elif version == 'patch':
        new_tag = inc_patch(tag)
    return new_tag
