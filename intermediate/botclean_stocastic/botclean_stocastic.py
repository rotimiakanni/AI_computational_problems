from os.path import realpath, join, dirname

def findIndex(x, m):
    '''Returns the index(position) of the an object in the 2D grid'''
    for item in x:
        if m in item:
            return (x.index(item), item.index(m))

def nextMove(posr, posc, board):
    '''
    link to problem: https://www.hackerrank.com/challenges/botcleanr/problem

    A deterministic environment is one where the next state is completely determined 
    by the current state of the environment and the task executed by the agent. 
    If there is any randomness involved in determining the next state, 
    the environment is stochastic. The game Bot Clean took place in a deterministic 
    environment. In this version, the bot is given 200 moves to clean as many 
    dirty cells as possible. The grid initially has 1 dirty cell. 
    When the bot cleans this cell, a new cell in the grid is made dirty. 
    The new cell can be anywhere in the grid. The bot here is positioned at the top left 
    corner of a 5*5 grid. Your task is to move the bot to appropriate dirty cell and clean it.

    sample input:
    0 0
    b---d
    -----
    -----
    -----
    -----

    sample out:
    RIGHT

    resultant state:
    -b--d
    -----
    -----
    -----
    -----

    '''
    bot = (posr, posc)
    dirt = findIndex(board, 'd') # get location of the dirt
    # check if bot x-position is same as dirt x-position
    # if bot y-position is less than dirt y-position, then move RIGHT
    # if bot y-position is greater than dirt y-position, then move LEFT
    # if bot y-position is same as dirt y-position, then spot is CLEAN
    if bot[0] == dirt[0]:
        if bot[1] < dirt[1]:
            print('RIGHT')
        elif bot[1] == dirt[1]:
            print('CLEAN')
        else:
            print('LEFT')

    # check if bot Y-position is same as dirt Y-position
    # if bot X-position is less than dirt X-position, then move DOWN
    # if bot X-position is greater than dirt X-position, then move UP
    # if bot X-position is same as dirt X-position, then spot is CLEAN
    elif bot[1] == dirt[1]:
        if bot[0] < dirt[0]:
            print('DOWN')
        elif bot[0] == dirt[0]:
            print('CLEAN')
        else:
            print('UP')
    
    #  if absolute value of difference between x-position of bot and dirt
    #  is greater than abs value of difference between y-position of bot
    #  and dirt,then LEFT or RIGHT movement is simulated
    elif abs(bot[0] - dirt[0]) > abs(bot[1] - dirt[1]):
        if bot[1] < dirt[1]:
            print('RIGHT')
        else:
            print('LEFT')

    #  if absolute value of difference between x-position of bot and dirt
    #  is equal to abs value of difference between y-position of bot
    #  and dirt,the LEFT or RIGHT movement is also simulated   
    elif abs(bot[0] - dirt[0]) == abs(bot[1] - dirt[1]):
        if bot[1] < dirt[1]:
            print('RIGHT')
        else:
            print('LEFT')
    
    #  if absolute value of difference between x-position of bot and dirt
    #  is less than abs value of difference between y-position of bot
    #  and dirt,then UP or DOWN movement is simulated
    elif abs(bot[0] - dirt[0]) < abs(bot[1] - dirt[1]):
        if bot[0] < dirt[0]:
            print('DOWN')
        else:
            print('UP')

input_file = join(dirname(realpath(__file__)), 'sample.txt')
ip_file = open(input_file)
if __name__ == "__main__":
    pos = [int(i) for i in ip_file.readline().strip().split()]
    board = [[j for j in ip_file.readline().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)