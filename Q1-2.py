import numpy
from sympy import *

def main():
    
    nx = ny = nz = 1 / (3 ** 0.5)

    x = Symbol('x')
    
    s1 = solve([((1 - cos(pi / x)) / 3) + cos(pi / x) - 0.911], x)
    
    s2 = solve([((1 - cos(pi / x)) / 3) - (sin(pi / x) / (3 ** 0.5)) - 0.333], x)
    
    s3 = solve([((1 - cos(pi / x)) / 3) + (sin(pi / x) / (3 ** 0.5)) + 0.244], x)
    
    print(s1)
    print(s2)
    print(s3)
    
    return 0


if __name__ == "__main__":
    main()