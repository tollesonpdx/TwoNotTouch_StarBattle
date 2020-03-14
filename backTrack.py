
def get_region_coords(board):
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
    vars = {}
    for region in regions:
        vars[str(region)+"A"]=None
        vars[str(region)+"B"]=None
    return vars


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
regionCoords = get_region_coords(board)

# set of variables
X = init_variables(regionCoords.keys())

# set of domains
#D=

# each variable one of two stars in col
# D_i = {1..(maxCol*2)}
# OR
# each variable is one of two stars in region, algorithm would take region boundres as input
#

# constraints
# star from same region have different locations 
# no two touch from any region
# only two othe star in same row / col from any region
        