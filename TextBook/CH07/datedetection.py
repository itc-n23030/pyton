import re
s = input()
def pattern_match(s):
    result = re.match(r'(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/([1-2][0-9]{3})', s)
    return  True if result else False

print(pattern_match(s))