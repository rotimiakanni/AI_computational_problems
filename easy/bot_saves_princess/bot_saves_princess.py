from os.path import realpath, join, dirname


def findIndex(x, m):
    '''Returns the index of the an object in the 2D grid'''
    for item in x:
        if m in item:
            return (x.index(item), item.index(m))

def displayPathtoPrincess(n,grid):
    """
    link to problem: https://www.hackerrank.com/challenges/saveprincess/problem

    Princess Peach is trapped in one of the four corners of a square grid. 
    You are in the center of the grid and can move one step at a time in any of 
    the four directions. Can you rescue the princess?

    sample input:
    3
    ---
    -m-
    p--

    sample output:
    DOWN
    LEFT
    """
    goal = findIndex(grid, 'p') # locate the princess p in 2D grid
    location = findIndex(grid, 'm') # locate the bot in the 2D grid
    moves = []
    # move UP or DOWN until bot is in same row as princess
    while goal[0] != location[0]:
        if goal[0] < location[0]:
            location = (location[0]-1, location[1])
            moves.append('UP')
        elif goal[0] > location[0]:
            location = (location[0]+1, location[1])
            moves.append('DOWN')
    # move LEFT or RIGHT until bot is in same column as princess
    while goal[1] != location[1]:
        if goal[1] < location[1]:
            location = (location[0], location[1]-1)
            moves.append('LEFT')
        elif goal[1] > location[1]:
            location = (location[0], location[1]+1)
            moves.append('RIGHT')
    # print the moves
    for move in moves:
        print(move)

input_file = join(dirname(realpath(__file__)), 'sample.txt')
ip_file = open(input_file)
m = int(ip_file.readline())
grid = [] 
for i in range(0, m): 
    grid.append(ip_file.readline().strip())

displayPathtoPrincess(m,grid)