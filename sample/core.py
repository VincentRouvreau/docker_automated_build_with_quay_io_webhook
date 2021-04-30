import numpy as np

def determinant(matrice):
    np_mat = np.array(matrice)
    return np.linalg.det(np_mat)