import random, time, copy
width = 60
height = 20

next_cells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

while True:
    print('\n\n\n\n\n')
    c_cells = copy.deepcopy(next_cells)

    for y in range(height):
        for x in range(width):
            print(c_cells[x][y], end='')
        print()
    
    for x in range(width):
        for y in range(height):
            x_coord = (x-1)%width
            x_coord2 = (x+1)%width
            y_coord = (y-1)%height
            y_coord2 = (y+1)%height

            num_neighbors = 0

            if c_cells[x][y_coord] == '#':
                num_neighbors += 1
            if c_cells[x][y_coord2] == '#':
                num_neighbors += 1 
            if c_cells[x_coord][y_coord] == '#':
                num_neighbors += 1 
            if c_cells[x_coord][y] == '#':
                num_neighbors += 1
            if c_cells[x_coord2][y] == '#':
                num_neighbors += 1           
            if c_cells[x_coord2][y_coord] == '#':
                num_neighbors += 1
            if c_cells[x_coord2][y_coord2] == '#':
                num_neighbors += 1
            if c_cells[x_coord][y_coord2] == '#':
                num_neighbors += 1
            if (c_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3)):
                next_cells[x][y] = '#'
            elif c_cells[x][y] == ' ' and num_neighbors == 3:
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = ' '
        time.sleep(1)



