def grid():
    grid = [['.' for i in range(9)] for i in range(6)]
    grid[0][2:4] = ['0' for _ in range(2)]
    grid[0][5:7] = ['0' for _ in range(2)]
    grid[1][1:8] = ['0' for _ in range(7)]
    grid[2][1:8] = grid[1][1:8]
    grid[3][2:7] = ['0' for _ in range(5)]
    grid[4][3:6] = ['0' for _ in range(3)]
    grid[5][4] = '0'
    for x in grid:
        for y in x:
            print(y, end='')
        print()
grid()