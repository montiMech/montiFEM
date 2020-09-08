""" 
key classes and functions for IPython Notebook
author: wolfgang flachberger (c)
em@il: wolfgang.flachberger@stud.unileoben.ac.at
15-07-2020
"""

import matplotlib.pyplot as plt  

from sympy import simplify, symbols, diff, zeros, init_printing, Array, integrate, sin, cos, tan, Integral, exp
from sympy.functions.special.delta_functions import DiracDelta 

from numpy import array, asarray, linspace, dot, set_printoptions, pi

from numpy.linalg import inv

from IPython.display import display




# hermite cubic interpolation functions 

def h0(x,l):
    return 1 - 3 * (x/l)**2 + 2 * (x/l)**3

def h1(x,l):
    return - x * (1 - (x/l))**2

def h2(x,l):
    return 3 * (x/l)**2 - 2 * (x/l)**3

def h3(x,l):
    return - x * ((x/l)**2 -(x/l))





