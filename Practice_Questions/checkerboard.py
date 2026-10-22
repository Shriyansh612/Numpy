import numpy as np

# method 1
# mat = np.zeros((8,8))
# mat[::2,::2] = 1
# mat[1::2,1::2] = 1
# print(mat)


#method 2
mat = np.zeros((8,8))   #creating a zero matrix



rows,cols = np.indices((8,8))   #both are numpy arrays  
print(rows)     #stores row index of each element
print(cols)     #stores column index of each element

diagonal_indices = cols-rows    #stores diagonal number of each element
print(diagonal_indices)
print(type(diagonal_indices))   #nd array

even_diagonals_mask = diagonal_indices%2==0      #boolean numpy array 
print(even_diagonals_mask)

mat[even_diagonals_mask] = 1         #acts on those elements that agrees to the condition
# mat[(rows-cols)%2==0] = 1  also works
print(mat)