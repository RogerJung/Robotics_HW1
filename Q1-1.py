import numpy
from sympy import *


def main():
    nx = 1 / (30 ** 0.5)
    ny = 5 / (30 ** 0.5)
    nz = 2 / (30 ** 0.5)
    
    theta = pi / 2
    
    # init. rotation matrix
    rot_mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # x axis rotate
    rot_mat[0][0] = nx * nx * (1 - cos(theta)) + cos(theta)
    rot_mat[0][1] = nx * ny * (1 - cos(theta)) - nz * sin(theta)
    rot_mat[0][2] = nx * nz * (1 - cos(theta)) + ny * sin(theta)
    
    # y axis rotate
    rot_mat[1][0] = nx * ny * (1 - cos(theta)) + nz * sin(theta)
    rot_mat[1][1] = ny * ny * (1 - cos(theta)) + cos(theta)
    rot_mat[1][2] = ny * nz * (1 - cos(theta)) - nx * sin(theta)
    
    # z axis rotate
    rot_mat[2][0] = nx * nz * (1 - cos(theta)) - ny * sin(theta)
    rot_mat[2][1] = ny * nz * (1 - cos(theta)) + nx * sin(theta)
    rot_mat[2][2] = nz * nz * (1 - cos(theta)) + cos(theta)
    
    for i in rot_mat:
        print(i)
    return 0


if __name__ == "__main__":
    main()