def comma_devide(spam):
    spam[-1] = 'and ' + spam[-1]
    return ', '.join(spam) 


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_devide(spam))