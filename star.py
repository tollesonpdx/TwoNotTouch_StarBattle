class Star():
    def __init__(self, row=none, col=none, region=none):
        self.row=row
        self.col=col
        self.region=region

    def get_neighbors(self, Maxrow, MaxCol):
        """
        return list of tuples for neighbors.  tuples is (row,col)
        """
        #fliter the list for out of bounds
        pass

    def get_position(self):
        return (self.row, self.col)

# each variable one of two stars in col
# D_i = {1..(maxCol*2)}
# OR
# each variable is one of two stars in region, algorithm would take region boundres as input
#

# constraints
# star from same region have different locations 
# no two touch from any region
# only two othe star in same row / col from any region
        