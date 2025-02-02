import time 
import random

# a bad matrix class D:
class TrnMtx:

    matrix = [[]]

    def __init__(self):
        self.random_matrix()

    MATRIX_LEN = len(matrix[0])

    def convert_to_pairs():
        array = []

        for i in range(TrnMtx.MATRIX_LEN):
            for j in range(TrnMtx.MATRIX_LEN):
                if matrix[i][j] == 1:
                    array.append([i+1,j+1])

        return array

    def convert_from_pairs(pairs):
        new_matrix = [[0] * TrnMtx.MATRIX_LEN for _ in range(TrnMtx.MATRIX_LEN)] 
        
        for i in pairs:
 
            new_matrix[i[0]-1][i[1]-1] = 1

        return new_matrix
    def random_matrix():
        
        TrnMtx.MATRIX_LEN = random.randint(3,50)
        new_matrix = [[0] * TrnMtx.MATRIX_LEN for _ in range(TrnMtx.MATRIX_LEN)]

        for i in range(TrnMtx.MATRIX_LEN):
            for c in range(TrnMtx.MATRIX_LEN):
                if random.randint(1,15) == 1:
                    new_matrix[i][c] = 1

        TrnMtx.matrix = new_matrix
        return new_matrix


temp_matrix = TrnMtx.random_matrix()
MATRIX_LEN = TrnMtx.MATRIX_LEN

matrix = temp_matrix


# Warshall's

# calculate time
t = time.time()
for k in range(MATRIX_LEN):
    for i in range(MATRIX_LEN):
        for j in range(MATRIX_LEN):
            if matrix[i][k] == 1 and matrix[k][j] == 1:
                matrix[i][j] = 1

for i in matrix:
    print(i)
warsh_time = time.time()-t


# calculate time
print(warsh_time)

# finds conections by swapping [s,v] -> [v+1,s]
def find_connections(start, value):
    # if [start,value] is a combo add it
    if [start,value] in start_array:

        if [start,value] not in start_array:
            start_array.append([start,value])

        return find_connections(start=value+1,value=start)
    
    # go next
    if value < MATRIX_LEN:
        
        return find_connections(start=value+1,value=start)

# calculate time
t = time.time()
# Mine
start_array = TrnMtx.convert_to_pairs()

# if they are there
array = find_connections(1,1)

matrix = TrnMtx.convert_from_pairs(start_array)
for i in matrix:
    print(i)

my_time = time.time()-t
print(my_time)
print(warsh_time/my_time)

