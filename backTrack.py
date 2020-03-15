
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
    return backtrack({}, csp)

def backtrack(assignments, csp):
    #if assignments is complete then return assignments
    if is_complete(assignments):
        return assignments
    var = select_unassigned_var(csp, assignments)
    for value in order_domain_values(var, assignments, csp):
        #if value is consistent with assignment then
        # if empty will just fall through loop and return failusre 

        # add {var=value} to assignments
        assignments[var]=value

        # inferecnes<-(csp, var, assignment) use to for arc consistency
        inferences = inference(csp, var, assignments)

        # if inferences not != failure
        # check to make sure domains are not empty, will get caught next time if selecting vars with smallest domains
            
            #add inferecnes to assignment
            #newInferences = inferecnes- constraints
            #constraints = newInferecnes untion constraints

            #result <- backTrack()

            # if result not equal failusre
                #return result
            
        #remove var=val and inferences from assignemnt 
        # why is this not indented more since no inferences potentially
    #return failsure





def inference(csp, var, assignment):
    return None

    
#not tested
def order_domain_values(var, assignment, csp):
    #what order should values be tried?
    #don't try ones that are already taken.  arc consitency
    return csp.D[var] - csp.C

# not tested
def select_unassigned_var(csp, assignments):
    # which variable should be assigned next?
    vars=assignments.keys() 
    for var in vars:
        if not assignments[var]:
            return var
    # change later to find var with smallest domain
    #minDomainSize=100000
    
def is_complete(assignments):
    isComplete=True
    for val in assignments.values():
        if not val:
            isComplete = False
    return isComplete

# --------------------------------------------------------------
#                             main
# --------------------------------------------------------------


Duck = namedtuple('Duck', 'bill tail')
duck =Duck(bill='wide orange', tail='long')
print(duck.bill)

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

# dictionary of  var: domain, set of coord 
D = init_domains(X, regionDomains)

#constraint = ()
C=set()

# use named tuple for CSP
Duck = namedtuple('Duck', 'bill tail')
duck =Duck(bill='wide orange', tail='long')
print(duck.bill)

CSP = namedtuple('CSP', 'X D C')
csp = CSP(X=X, D=D, C=C)


# constraints
# star from same region have different locations- costar(var)
# no two touch from any region-  neighbors(coord)
# only two othe star in same row / col from any region row(coord), col(cood)
        