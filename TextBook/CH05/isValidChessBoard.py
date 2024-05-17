import re
def is_valid_chess_board(dict):
    a = list(dict.keys())
    lst = list(filter(lambda x: x.endswith('z') or x.startswith('9'),a))
    return  False if len(lst) != 0 else True
    
dict = {'9a': 'wking', '7b': 'bpawn'}
dict1 = {'8a': 'bqueen', '4e': 'wknight'}
print(is_valid_chess_board(dict))
print(is_valid_chess_board(dict1))

