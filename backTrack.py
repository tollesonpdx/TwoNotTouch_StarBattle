
from collections import namedtuple

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

# def class CSP():
#     def __init__(self, X, D, C):
#         self.X = X
#         self.D = D
#         self.C = C

def backtracking_search(csp):
    assignment= Assignment(init_assignments(csp.X), set())
    return backtrack(assignment, csp)

def backtrack(assignment, csp):
    #if assignment is complete then return assignment
    if is_complete(assignment):
        return assignment
    var = select_unassigned_var(csp, assignment)
    for value in order_domain_values(var, assignment, csp):
        #if value is consistent with assignment then
        if value_consistent_with_assignment(value, assignment):

            # add {var=value} to assignment
            assignment.vals[var]=value

            # inferecnes<-(csp, var, assignment) use to for arc consistency
            inferences = inference(csp, var, assignment)

            # if inferences not != failure
            # check to make sure domains are not empty, will get caught next time if selecting vars with smallest domains
            
            #add inferecnes to assignment
            newUnavailable = inferences - assignment.unavailable
            assignment.unavailable = assignment.unavailable | newUnavailable

            #result <- backTrack(assignment, csp)
            result = backtrack(assignment, csp)

            #if result != failsure 
            if result:
                return result

            #remove {var=val} and inferences from assignemnt 
            assignment.vals[var]=None
            assignment.unavailable = assignment.unavailable - newUnavailable

    #return failsure
    return None

def value_consistent_with_assignment(value, assignment):
    """
    applies constraint to value and assignment
    input: value, assignment
    output: bool
    """
    vals = list(assignment.vals.values())
    vals.append(value)
    #need to filter out none
    vals = [val for val in vals if val]
    return notTooClose(vals)

#not tested
def order_domain_values(var, assignment, csp):
    """
    returns values in domain that are arc consistent, 
    assuming unavailable has been updated via forward propogation
    """
    #what order should values be tried?
    #don't try ones that are already taken.  arc consitency
    return csp.D[var] - assignment.unavailable

# not tested
def select_unassigned_var(csp, assignment):
    # which variable should be assigned next?
    minDomainSize=100000
    minVar=None
    vars=assignment.vals.keys() 
    for var in vars:
        if not assignment.vals[var]:
            domainSize= len(csp.D[var])
            if domainSize < minDomainSize:
                minDomainSize=domainSize
                minVar= var
    return minVar

    
def is_complete(assignments):
    isComplete=True

    for val in assignments.vals.values():
        if not val:
            isComplete = False
    return isComplete

def inference(csp, var, assignment):
    inferences=set()
    newCoord = assignment.vals[var]

    #get position
    inferences.add(newCoord)

    #add neighbors
    inferences = inferences.union(set(get_neighbors(newCoord)))

    #check if row filled
    coords = list(assignment.vals.values())
    coords = [coord for coord in coords if coord]

    rowCount=0
    for coord in coords:
        if coord[0] == newCoord[0]:
            rowCount += 1

    if rowCount == 2:
        inferences = inferences.union(get_row(newCoord, csp))

    #check of col filed
    colCount=0
    for coord in coords:
        if coord[1] == newCoord[1]:
            colCount += 1

    if colCount == 2:
        inferences = inferences.union(get_col(newCoord, csp))

    return inferences

def get_row(newCoord, csp):
    #coords are eiter in assignments
    allCoords=set()
    domains= csp.D.values()
    for d in domains:
        allCoords = allCoords.union(d)

    return {coord for coord in allCoords if coord[0] == newCoord[0]}

def get_col(newCoord, csp):
    allCoords=set()
    domains= csp.D.values()
    for d in domains:
        allCoords = allCoords.union(d)

    return {coord for coord in allCoords if coord[1] == newCoord[1]}

# --------------------------------------------------------------
#                             constraint functions
# --------------------------------------------------------------

def notTooClose(coords):
    """
    constraint function
    inmput list of vals currently assigned variables ++ new potential val
    output bool if new var matches constraint
    """
    #make coord no set should overlap
    noCoordsSame=no_coords_same(coords) 

    # make sure no neighbors overlap
    noCoordsAreNeighbors= no_coords_are_neighbors(coords)

    #make sure only two in each row
    #make sure only two in each col
    noMoreThanTwo=no_more_than_two(coords)
    
    return noCoordsSame and noCoordsAreNeighbors and noMoreThanTwo

def no_more_than_two(coords):
    """
    collumns and rows contain no more than two stars
    """
    return rows_have_two_or_less(coords) and cols_have_two_or_less(coords)

def rows_have_two_or_less(coords):
    rowCounts={}

    for coord in coords:
        if coord[0] in rowCounts:
            rowCounts[coord[0]] += 1
        else:
            rowCounts[coord[0]] = 1

    for count in rowCounts.values():
        if count > 2:
            return False

    return True

def cols_have_two_or_less(coords):
    colCounts={}

    for coord in coords:
        if coord[1] in colCounts:
            colCounts[coord[1]] += 1
        else:
            colCounts[coord[1]] = 1

    for count in colCounts.values():
        if count > 2:
            return False
            
    return True

def no_coords_same(coords):
    """
    input: list of coords
    output: bool
    """
    takenList=[{coord} for coord in coords]
    s=set() 
    for taken in takenList:
        s= s.symmetric_difference(taken)
    u=set()
    for taken in takenList:
        u= u.union(taken)
    if s!= u:
        #notTooClose = False
        return False
    return True

def no_coords_are_neighbors(coords):
    u = set(coords)

    neighborGroups=[get_neighbors(coord) for coord in coords]
    allNeighbors = set()
    for neighbors in neighborGroups : 
        for neighbor in neighbors:
            if neighbor in u:
                #notTooClose = False
                return False
            else:
                allNeighbors.add(neighbor)
    return True

def get_neighbors(coord):
    top = (coord[0]-1,coord[1])
    topRight = (coord[0]-1,coord[1]+1)
    topLeft = (coord[0]-1,coord[1]-1)
    bottom = (coord[0]+1,coord[1])
    bottomLeft = (coord[0]+1,coord[1]-1)
    bottomRight = (coord[0]+1,coord[1]+1)
    left = (coord[0],coord[1]-1)
    right = (coord[0],coord[1]+1)
    return [top, topRight, topLeft, bottom, bottomLeft, bottomRight, left, right] 


class Assignment():
    def __init__(self, vals, unv):
        self.vals=vals
        self.unavailable=unv

# --------------------------------------------------------------
#                             main
# --------------------------------------------------------------

Duck = namedtuple('Duck', 'bill tail')
CSP = namedtuple('CSP', 'X D C')

#Assignment = namedtuple('Assignment', 'vals unavailable')
        