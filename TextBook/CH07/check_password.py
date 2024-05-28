import re
def strong_passwd(ps):
    s = re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[a-zA-Z0-9]{8,}', ps)
    return True if s else False

ps = input()
print(strong_passwd(ps))