from os.path import realpath, join, dirname

def findIndex(x, m):
    lis = []
    for item in range(len(x)):
        for char in range(len(x[item])):
            if x[item][char] == m:
                lis.append((item, char))
    return lis


def next_move(posx, posy, dimx, dimy, board):
    '''
    Link to problem: https://www.hackerrank.com/challenges/botcleanlarge/problem

    MegaMaid is a robot whose function is to move through a 
    matrix and clean all of its dirty cells. It's positioned 
    in some cell of an  matrix of dirty (d) and clean (-) cells. 
    It can perform five types of operations:

    LEFT: Move one cell to the left.
    RIGHT: Move one cell to the right.
    UP: Move one cell up.
    DOWN: Move one cell down.
    CLEAN: Clean the cell.
    Given the robot's current location and the configuration of 
    dirty and clean cells in the matrix, print the next operation 
    MegaMaid will perform (e.g., UP, CLEAN, etc.) on a new line.

    sample input:
    0 0
    5 5
    b---d
    -d--d
    --dd-
    --d--
    ----d

    sample output:
    RIGHT

    explanation:
    -b--d
    -d--d
    --dd-
    --d--
    ----d
    '''
    bot = (posx, posy)
    dirtyList = findIndex(board, 'd')
    dirt = (dimx, dimy)
    thresh = dimx * dimy
    for pos in dirtyList:
        steps = abs(bot[0]-pos[0]) + abs(bot[1]-pos[1])
        if steps < thresh:
            thresh = steps
            dirt = pos  
    
    if bot[0] == dirt[0]:
        if bot[1] < dirt[1]:
            print('RIGHT')
        elif bot[1] == dirt[1]:
            print('CLEAN')
        else:
            print('LEFT')
    
    elif bot[1] == dirt[1]:
        if bot[0] < dirt[0]:
            print('DOWN')
        elif bot[0] == dirt[0]:
            print('CLEAN')
        else:
            print('UP')
            
    elif abs(bot[0] - dirt[0]) > abs(bot[1] - dirt[1]):
        if bot [1] < dirt[1]:
            print('RIGHT')
        else:
            print('LEFT')
            
    elif abs(bot[0] - dirt[0]) == abs(bot[1] - dirt[1]):
        if bot [1] < dirt[1]:
            print('RIGHT')
        else:
            print('LEFT')
    
    elif abs(bot[0] - dirt[0]) < abs(bot[1] - dirt[1]):
        if bot [0] < dirt[0]:
            print('DOWN')
        else:
            print('UP')
    
    print("")

if __name__ == "__main__":
    input_file = join(dirname(realpath(__file__)), 'sample.txt')
    ip_file = open(input_file)
    pos = [int(i) for i in ip_file.readline().strip().split()]
    dim = [int(i) for i in ip_file.readline().strip().split()]
    board = [[j for j in ip_file.readline().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)