from collections import deque

from data import *

maze = maze_data.split('\n')

def solveMaze(maze):
    R, C = len(maze), len(maze[0])

    start = (0, 0)
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        else: continue
        break
    else:
        return None

    queue = deque()
    steps = 64
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:
        coord = queue.pop()
        steps -= 1
        visited[coord[0]][coord[1]] = True

        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]): continue
            queue.appendleft((nr, nc, coord[2]+1))

        if steps == 0:
            print(len(queue)+1)

solveMaze(maze)
