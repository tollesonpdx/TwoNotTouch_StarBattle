
def region_domains(board):
    """
    make list of tuples for each region to construct domains
    return dictionary of region : set of coord pairs
    """
    regionCoords={}    
    rowIndex=0
    for row in board:
        colIndex=0
        for colVal in row:
            if colVal in regionCoords:
                regionCoords[colVal].add((rowIndex,colIndex))
            else:
                regionCoords[colVal]=set()
                regionCoords[colVal].add((rowIndex,colIndex))
            colIndex +=1
        rowIndex +=1
    return regionCoords

def init_variables(regions):
    vars = set()
    for region in regions:
        vars.add(str(region)+"A")
        vars.add(str(region)+"B")
    return vars

def init_assignments(vars):
    return {var: None for var in vars}

def init_domains(X, regionDomains):
    D = {}
    for var in X:
        D[var] = set()
        D[var]= {coord for coord in regionDomains[int(var[0])]}
    return D

board = ((0,0,1,1,2,2,2,2),
         (3,3,3,1,1,2,2,2),
         (4,4,4,4,1,2,2,2),
         (4,4,4,4,4,4,2,2),
         (5,6,6,6,4,4,2,2),
         (5,6,6,6,6,6,6,6),
         (5,5,7,7,7,7,6,6),
         (7,7,7,7,7,7,7,7))

maxRow = len(board)
maxCol = len(board[0])

regionDomains = region_domains(board)

# set of variables- each variable is one of two stars in region
X = init_variables(regionDomains.keys())

#assignments where key is var from X
assignments= init_assignments(X)

# set of domains
D= init_domains(X, regionDomains)


# constraints
# star from same region have different locations 
# no two touch from any region
# only two othe star in same row / col from any region
        