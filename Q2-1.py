import numpy as np
import sympy
from math import *

def main():
    
    rot_mat = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
               [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
               [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    
    theta = [pi/3, pi/6, pi/4]
    
    # first matrix
    rot_mat[0][0][0] = 1
    rot_mat[0][0][1] = 0
    rot_mat[0][0][2] = 0
    rot_mat[0][1][0] = 0
    rot_mat[0][1][1] = sympy.cos(theta[0])
    rot_mat[0][1][2] = -sympy.sin(theta[0])
    rot_mat[0][2][0] = 0
    rot_mat[0][2][1] = sympy.sin(theta[0])
    rot_mat[0][2][2] = sympy.cos(theta[0])
    
    # second matrix
    rot_mat[1][0][0] = sympy.cos(theta[1])
    rot_mat[1][0][1] = 0
    rot_mat[1][0][2] = sympy.sin(theta[1])
    rot_mat[1][1][0] = 0
    rot_mat[1][1][1] = 1
    rot_mat[1][1][2] = 0
    rot_mat[1][2][0] = -sympy.sin(theta[1])
    rot_mat[1][2][1] = 0
    rot_mat[1][2][2] = sympy.cos(theta[1])
    
    # third matrix
    rot_mat[2][0][0] = sympy.cos(theta[2])
    rot_mat[2][0][1] = -sympy.sin(theta[2])
    rot_mat[2][0][2] = 0
    rot_mat[2][1][0] = sympy.sin(theta[2])
    rot_mat[2][1][1] = sympy.cos(theta[2])
    rot_mat[2][1][2] = 0
    rot_mat[2][2][0] = 0
    rot_mat[2][2][1] = 0
    rot_mat[2][2][2] = 1
    
    
    mul = np.matmul(np.array(rot_mat[1]), np.array(rot_mat[0]))
    result = np.matmul(np.array(rot_mat[2]), mul)
    
    print(result)
    
    return 0


if __name__ == "__main__":
    main()