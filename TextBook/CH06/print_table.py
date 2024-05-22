import numpy as np
arr = []
def f(table_data):
    for n in range(4):
        for i in table_data:
            arr.append(i[n])

    h = np.array(arr).reshape(4,3)
    for x in h:
        for y in x:
            print(y.rjust(8), end='')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

f(table_data)