import time


class trnMtx:
  matrix = [
    [0,1,0,0],
    [0,0,0,0],
    [0,0,0,1],
    [1,0,0,0],
    ]
  
  MATRIX_LEN = len(matrix[0])

  def convert_to_pairs():
    array = []

    for i in range(MATRIX_LEN):
        for j in range(MATRIX_LEN):
            if matrix[i][j] == 1:
                array.append([i+1,j+1])

    return array


matrix = trnMtx.matrix

MATRIX_LEN = trnMtx.MATRIX_LEN

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
def find_connections(start, value, current_connections = []):

    # if [start,value] is a combo add it
    if [start,value] in start_array:
        
        current_connections.append([start,value])
        
        return find_connections(start=value+1,value=start,current_connections=current_connections)
    
    # go next
    if value < MATRIX_LEN:
        
        return find_connections(start=value+1,value=start,current_connections=current_connections)
    
    return current_connections

# calculate time
t = time.time()
# Mine
start_array = trnMtx.convert_to_pairs()

# if they are there
array = find_connections(1,1)
for i in array:
    if [array[0][0], i[1]] not in start_array:
        start_array.append([array[0][0], i[1]])
        
my_time = time.time()-t
print(my_time)
print(warsh_time/my_time)
# returns pairs as matrix relation
print(start_array)
