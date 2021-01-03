dirs = [
    lambda x, y, z, p: (x, y + 1, z + 1, p + [(x, y)]),
    lambda x, y, z, p: (x - 1, y, z + 1, p + [(x, y)]),
    lambda x, y, z, p: (x + 1, y, z + 1, p + [(x, y)]),
    lambda x, y, z, p: (x - 1, y - 1, z + sqrt(2), p + [(x, y)]),
    lambda x, y, z, p: (x + 1, y - 1, z + sqrt(2), p + [(x, y)]),
    lambda x, y, z, p: (x - 1, y + 1, z + sqrt(2), p + [(x, y)]),
    lambda x, y, z, p: (x + 1, y + 1, z + sqrt(2), p + [(x, y)])
]
def valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def adjacent(grid, frontier):
    for (x, y, z, p) in frontier:
        for d in dirs:
            nx, ny, nz, np = d(x, y, z, p)
            if valid(grid, nx, ny):
                yield (nx, ny, nz, np)
def flood(grid, frontier):
    res = list(adjacent(grid, frontier))
    for (x, y, z, p) in frontier:
        grid[x][y] = 1
    return res

def UCS(grid, start, end):
    start, end = tuple(start), tuple(end)
    frontier = [(start[0], start[1], 0, [])]
    res = []
    while frontier and grid[end[0]][end[1]] == 0:
        frontier = flood(grid, frontier)
        for (x, y, z, p) in frontier:
            matrix[x, y] == 'X'  # danh dau duong di
            print('[(', x, y, ')]')
            if (x, y) == end:
                res.append((z, p + [(x, y)]))
    if not res:
        return ()
    return sorted(res)[0]
