from os.path import realpath, join, dirname


def findIndex(x, m):
    '''Returns the index of the an object in the 2D grid'''
    for item in x:
        if m in item:
            return (x.index(item), item.index(m))

def nextMove(r,c,grid):
    '''
    link to problem: https://www.hackerrank.com/challenges/saveprincess2/problem

    Complete the function nextMove which takes in 4 parameters 
    - an integer N, integers r and c indicating the row & column 
    position of the bot and the character array grid - and 
    outputs the next move the bot makes to rescue the princess.

    sample input:
    5
    2 3
    -----
    -----
    p--m-
    -----
    -----

    sample output:
    LEFT

    resultant state:
    -----
    -----
    p-m--
    -----
    -----
    '''
    goal = findIndex(grid, 'p')
    location = (r, c)
    if goal[0] == location[0]:
        if goal[1] < location[1]:
            return('LEFT')
        else:
            return('RIGHT')
    elif goal[0] < location[0]:
        return('UP')
    else:
        return('DOWN')

input_file = join(dirname(realpath(__file__)), 'sample.txt')
ip_file = open(input_file)
n = int(ip_file.readline())
r,c = [int(i) for i in ip_file.readline().strip().split()]
grid = []
for i in range(0, n):
    grid.append(ip_file.readline())

print(nextMove(r,c,grid))