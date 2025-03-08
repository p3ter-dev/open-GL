import numpy as np

def reconstruct_matrix(U, S, V):
 
    if len(S.shape) == 1:  
        S = np.diag(S)
    
    return np.dot(U, np.dot(S, V.T))

U = np.array([[1, 0], [0, 1]])
S = np.array([3, 2])
V = np.array([[1, 0], [0, 1]])

original_matrix = reconstruct_matrix(U, S, V)
print("Reconstructed Matrix:")
print(original_matrix)
