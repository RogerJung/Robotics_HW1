import numpy as np
import sympy
from math import *


def main():
    
    nx = []
    ny = []
    nz = []
    theta = []
    
    nx.append(1 / (3 ** 0.5))
    ny.append(1 / (3 ** 0.5))
    nz.append(1 / (3 ** 0.5))
    theta.append(pi / 3)
    
    nx.append(1 / (6 ** 0.5))
    ny.append(-1 / (6 ** 0.5))
    nz.append(2 / (6 ** 0.5))
    theta.append(pi / 6)
    
    nx.append(-1 / (11 ** 0.5))
    ny.append(-3 / (11 ** 0.5))
    nz.append(1 / (11 ** 0.5))
    theta.append(pi / 4)
    
    # init. rotation matrix
    rot_mat = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
               [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
               [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    
    for i in range(3):
        # x axis rotate
        rot_mat[i][0][0] = nx[i] * nx[i] * (1 - sympy.cos(theta[i])) + sympy.cos(theta[i])
        rot_mat[i][0][1] = nx[i] * ny[i] * (1 - sympy.cos(theta[i])) - nz[i] * sympy.sin(theta[i])
        rot_mat[i][0][2] = nx[i] * nz[i] * (1 - sympy.cos(theta[i])) + ny[i] * sympy.sin(theta[i])
        
        # y axis rotate
        rot_mat[i][1][0] = nx[i] * ny[i] * (1 - sympy.cos(theta[i])) + nz[i] * sympy.sin(theta[i])
        rot_mat[i][1][1] = ny[i] * ny[i] * (1 - sympy.cos(theta[i])) + sympy.cos(theta[i])
        rot_mat[i][1][2] = ny[i] * nz[i] * (1 - sympy.cos(theta[i])) - nx[i] * sympy.sin(theta[i])
        
        # z axis rotate
        rot_mat[i][2][0] = nx[i] * nz[i] * (1 - sympy.cos(theta[i])) - ny[i] * sympy.sin(theta[i])
        rot_mat[i][2][1] = ny[i] * nz[i] * (1 - sympy.cos(theta[i])) + nx[i] * sympy.sin(theta[i])
        rot_mat[i][2][2] = nz[i] * nz[i] * (1 - sympy.cos(theta[i])) + sympy.cos(theta[i])
        
    mul = np.matmul(rot_mat[1], rot_mat[0])
    result = np.matmul(rot_mat[2], mul)
    
    # print(np.array(rot_mat[0]))
    # print("--------------")
    # print(np.array(rot_mat[1]))
    # print("--------------")
    # print(np.array(rot_mat[2]))
    # print("--------------")
    
    print(result)

    return 0


if __name__ == "__main__":
    main()