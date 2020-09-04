# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

######################################################################
# (Template) Laporan Praktikum ke-<2>                                #
# Integral tanpa plot                                                #
# Hari & Tanggal: <Rabu, 25 April 2018>                              #
# Shift ke      : <2>                                                #
# NIM           : <10316029>                                         #
# Nama Lengkap  : <Faiq Iftirul Mahlidah>                            #
# Alamat email  : <faiqim13@gmail.com>                               #
#                                                                    #
# Saya menyatakan bahwa kode program saya adalah hasil pemikiran     #
# saya sendiri dengan MENGIKUTI ALGORITMA YANG DISAMPAIKAN DI KELAS  #
# PERKULIAHAN AS2205 Astronomi Komputasi dan bahan-bahan modul       #
# praktikum yang telah disediakan.
# Sanksi nilai siap saya terima bila ada praktek plagiarisme         #
# (plagiat) dalam kode program ini.                                  #
#                                                                    #
######################################################################

import numpy
import scipy
import numpy as np
import matplotlib
import scipy
import math
import sys




#-(0)---- IMPORTING MODULES ---------
# importing math and numpy modules. Do it!
#’quad’: definite integral modul from scipy
from scipy.integrate import quad
#-------------------------------------
#-(1)------- THE FUNCTION ------------
#xa = x'
#na = n'
def integrand(x):
    return (((144/30) * (x/30)**0.44 * np.exp((x/30)**1.44))*6/x)

#-------------------------------------
#-(2)INTEGRATION BOUNDARIES, say a & b
# using ’input’ or ’raw_input’
#a=dmin
#b=dmax
a = 1

def integLeft(a, b, f, nbins=10):
    h = float(b-a)/nbins    # allow input of integer a and b
    assert h > 0            # warn if b not > a
    assert type(nbins) == int
    
    sum = 0.0
    for n in range(nbins):  # [0, 1, ... nbins-1]
        sum = sum + h * f(a + n*h)   # left hand rule

    return sum

def integMid(a, b, f, nbins=10):
    '''Return the integral from a to b of function f using the midpoint rule

    >>> integMid(0, 1, f, 4)
    0.828125
    '''
    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = 0.0
    x = a + h/2                  # first midpoint
    while (x < b):
        sum += h * f(x)
        x += h

    return sum

def integTrap(a, b, f, nbins=10):
    '''Return the integral from a to b of function f using trapezoidal rule

    >>> integTrap(0, 1, f, 4)
    0.84375
    '''
    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = (h/2) * (f(a) + f(b))  # endpoints are special
    for n in range(1, nbins):    # [1, 2, ... nbins-1]
        sum += h * f(a + n*h)
    
    return sum

