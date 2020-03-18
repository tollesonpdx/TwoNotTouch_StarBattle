import random 

def init_board(rowMax=8, colMax=8):
    """
    returns blank board
    """
    board={}
    for i in range(0,rowMax):
        board[i]={}
        for j in range(0,colMax):
            board[i][j]=False
    return board

def print_board(board, rowMax=8, colMax=8):
    """
    print board
    """
    for i in range(0,rowMax):
        for j in range(0,colMax):
            if board[i][j]:
                print(' X  ', end='')
            else:
                print(' 0  ', end='')
        print('')
        print('')

def to_board(configStr):
    """
    turns string into board with queens on it
    """
    board =  init_board()
    for i in range(0,8):
        board[int(configStr[i])][i] = True
    return board

def random_config(colMax=8):
    """
    makes random config string
    """
    config=''
    for _ in range (0, colMax):
        config = config + str(random.randint(0,7))
    return config

def attacking_queens(board, rowMax=8, colMax=8):
    """
    return number of mutually attacking queens.
    for each qeens find how many attacking, sume, divide by 2
    return
    """
    attackingPairs=set()
    for i in range(0,rowMax):
        for j in range(0,colMax):
            if board[i][j]:
                attackingPairs = attackingPairs.union(attacked_by(i, j, board))

    return len(attackingPairs)

def new_pair(row1, col1, row2, col2):
    """
    input int for row col
    create new set of attackingpairs 
    each set contains strings
    """
    first= str(row1) + str(col1)
    second= str(row2) + str(col2)
    newPair = '' 
    if first < second:
        newPair = first + '-' + second
    else:
        newPair = second + '-' + first
    return newPair
     

def attacked_by(row, col, board, rowMax=8, colMax=8):
    attackingPairs=set()

    #check rest of row
    for i in range(0, col):
        if board[row][i]:
            attackingPairs.add(new_pair(row, col, row, i))

    for i in range(col+1, colMax):
        if board[row][i]:
            attackingPairs.add(new_pair(row, col, row, i))

    #check rest of column
    for i in range(0, row):
        if board[i][col]:
            attackingPairs.add(new_pair(row, col, i, col))

    for i in range(row+1, rowMax):
        if board[i][col]:
            attackingPairs.add(new_pair(row, col, i, col))

    attackingSelf=str(row) + str(col) + '-' + str(row) + str(col)
    #check diaganols
    rowIndex = row - col
    colIndex = 0
    if rowIndex < 0:
        rowIndex=row
        colIndex=col
    while(rowIndex < rowMax and colIndex < colMax):
        if board[rowIndex][colIndex]:
            newPair=new_pair(row, col, rowIndex, colIndex)
            if newPair != attackingSelf:
                attackingPairs.add(newPair)
        rowIndex +=1
        colIndex +=1
     
    rowIndex = row + col
    colIndex = 0
    if rowIndex >= rowMax:
        rowIndex=row
        colIndex=col
    while(rowIndex >= 0 and colIndex < colMax-1):
        if board[rowIndex][colIndex]:
            newPair=new_pair(row, col, rowIndex, colIndex)
            if newPair != attackingSelf:
                attackingPairs.add(newPair)
        rowIndex -= 1
        colIndex += 1

    return attackingPairs

def fitness(config):
    """
    28 non attacking queens is solution
    """
    return 28 - attacking_queens(to_board(config))

def cross_over(parent1, parent2, crossOverPoint=random.randint(0,7), maxCol=8):
    child=''
    for i in range(0, crossOverPoint):
        child=child + parent1[i]

    for i in range(crossOverPoint, maxCol):
        child=child + parent2[i]
    return child

def mutation(config, mutationPoint=random.randint(0,7),
mutation=random.randint(0,7), maxCol=8):
    """
    call mutation randomly outside of function for testing purposes
    """
    mutatedConfig=''

    for i in range(0, mutationPoint):
        mutatedConfig=mutatedConfig + config[i]
    
    mutatedConfig =  mutatedConfig + str(mutation)

    for i in range(mutationPoint+1, maxCol):
        mutatedConfig=mutatedConfig + config[i]
    return mutatedConfig

def get_reproducer(population, randomFitness):
    fitness=0
    index=-1
    individual=None

    while fitness < randomFitness:
        index += 1
        individual = population[index]
        fitness += individual[0]

    if individual:   
        return individual[1]
    else:
        return population[0][1]