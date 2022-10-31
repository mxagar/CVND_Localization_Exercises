#import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    # Loop through all grid cells
    for i, row in enumerate(beliefs):
        p_row_new = []
        for j, cell in enumerate(row):
            # Check if the sensor reading is equal to the color of the grid cell
            # if so, hit = 1
            # if not, hit = 0
            # Basically, we apply pHit in all map cells
            # with the measurement value, pMiss in the rest
            hit = (color == grid[i][j])
            # Save column/cell in row
            p_row_new.append(beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss))
        # Save row in grid
        new_beliefs.append(p_row_new)
        
    # Normalize: divide all elements of new_beliefs by the sum
    # because the complete distribution should add up to 1
    new_beliefs = normalize(new_beliefs)
            
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            # FIXED: width <-> height were interchanged,
            # which had an effect only with rectangular grids 
            new_i = (i + dy ) % height # width
            new_j = (j + dx ) % width # height
            #print("width, height:", width, height)
            #print("i, j:", i, j)
            #print("dy, dx:", dy, dx)
            #print("new_i, new_j:", new_i, new_j)
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
