import re

def strip_text(text, *character):
    if character:
        l_regex = re.compile(r'^%s*' % character[0])
        r_regex = re.compile(r'%s*$' % character[0])
    else:
        l_regex = re.compile(r'^\s*')
        r_regex = re.compile(r'\s*$')
    text = l_regex.sub('', text)
    text = r_regex.sub('', text)
    print(text)

strip_text('    前後のスペース文字を取り除く    ')
strip_text('XXXX前後のXを取り除くXXXX', 'X')
