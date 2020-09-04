
# coding: utf-8

# In[ ]:


import numpy as np
import scipy.linalg as lin
import matplotlib.pyplot as plt
import scipy.sparse
import scipy.sparse.linalg
from astropy.units import dT
from mpl_toolkits.mplot3d import Axes3D

xmax = 2.4
ymax = 3
N = int(input('Discreate the plate = '))

nx = 4*N #number of x-axis squares
ny = 5*N #number of y-axis squares

#determine width of the squares
dx = xmax/nx
dy = ymax/ny

#options
method=0
print('1. Gauss-Seidel \n2. Leiberman')
while (method<=0 or method>=3):
    method = int(input('Choose a method = '))
    if method ==1 :
        iteration = int(input('Number of iteration = '))
    if method ==2 :
        lamb = float(input('Weighting factor = '))
        iteration = int(input('Number of iteration = '))

#set temperature
T = np.zeros([ny+1,nx+1]) #set surface temperature = 0
T[ny,:] = 50 #T bottom
T[0,:] = 300 #T top
T[:,0] = 75 #T left
T[:,nx] = 100 #T right
print(T)

Tcopy = np.zeros([ny+1,nx+1])
Tcopy[ny,:] = 50 
Tcopy[0,:] = 300 
Tcopy[:,0] = 75
Tcopy[:,nx] = 100

Tfinal = np.zeros([ny+1,nx+1])
Tfinal[ny,:] = 50 
Tfinal[0,:] = 300 
Tfinal[:,0] = 75
Tfinal[:,nx] = 100

M = (nx-1)*(ny-1)
print(M)

Trelaxed = np.zeros([M,M]) #matrix initiation
Tseconditeration = np.zeros([M,M]) #matrix initiation

for a in range(M):
    for j in range(1,ny):
        for i in range(1,nx):
            if method == 1:
                for k in range (iteration) :
                    R = T[j,i-1]+T[j-1,i]+T[j,i+1]+T[j+1,i]
                    T[j,i] = 0.25*R
            if method == 2:
                for k in range (iteration) :
                    R = T[j,i-1]+T[j-1,i]+T[j,i+1]+T[j+1,i]
                    T[j,i] = 0.25*R
                    Trelaxed[j,i]=lamb*T[j,i]+(1-lamb)*Tcopy[j,i]     
                    for k in range (iteration) :
                        R = Trelaxed[j,i-1]+Trelaxed[j-1,i]+Trelaxed[j,i+1]+Trelaxed[j+1,i]
                        Tseconditeration[j,i] = 0.25*R
                        Tfinal[j,i]=lamb*Tseconditeration[j,i]+(1-lamb)*Trelaxed[j,i]
           
#plot
fig = plt.figure()
ax = Axes3D(fig)

X = np.linspace(0, xmax, nx+1)
Y = np.linspace(0, ymax, ny+1)
X,Y = np.meshgrid(X, Y)

if method == 1:
    print(T)
    ax.plot_surface(Y,X,T, rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.set_xlim (0,ymax)
    ax.set_ylim (0,xmax)
    ax.set_xlabel('y(cm)', fontsize=10)
    ax.set_ylabel('x(cm)', fontsize=10)
    ax.set_zlabel('$^\circ$C', fontsize=10)
    ax.zaxis.set_rotate_label(False)
    plt.show()
    
if method == 2:
    print (Tfinal)
    ax.plot_surface(Y,X,Tfinal, rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.set_xlim (0,ymax)
    ax.set_ylim (0,xmax)
    ax.set_xlabel('y(cm)', fontsize=10)
    ax.set_ylabel('x(cm)', fontsize=10)
    ax.set_zlabel('$^\circ$C', fontsize=10)
    ax.zaxis.set_rotate_label(False)
    plt.show()

