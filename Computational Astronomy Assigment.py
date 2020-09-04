
# coding: utf-8

# In[48]:


import numpy as np
import matplotlib.pyplot as plt

data = 'Enam Massa Matahari.txt'
L = np.loadtxt(data, usecols=(3))
Te = np.loadtxt(data, usecols=(4))

Lsun = 3.85*10**33
Ly = L/Lsun

plt.figure(1)
plt.scatter(Te, Ly, s=1)
plt.gca().invert_xaxis()
#plt.plot(Te, F107, 'bo', label='F10.7 per hari')
plt.legend()
plt.title('Diagram HR Tiga Massa Matahari')
plt.xlabel('Temperatur Efektif ($K$)')
plt.ylabel('Luminositas ($L\odot$)')
plt.savefig('Tiga Massa Matahari.png', dpi=800)
plt.show()


# In[50]:


import numpy as np
import matplotlib.pyplot as plt

data = 'Satu Massa Matahari.txt'
L = np.loadtxt(data, usecols=(3))
Te = np.loadtxt(data, usecols=(4))

Lsun = 3.85*10**33
Ly = L/Lsun

plt.figure(1)
plt.plot(Te, Ly)
plt.scatter(Te, Ly, s=5)
plt.gca().invert_xaxis()
plt.legend()
plt.title('Diagram HR Satu Massa Matahari')
plt.xlabel('Temperatur Efektif ($K$)')
plt.ylabel('Luminositas ($L\odot$)')
plt.savefig('Satu Massa Matahari.png', dpi=800)
plt.show()

#hasil plot menunjukkan sub giant branch


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

data = 'Tiga Massa Matahari.txt'
L = np.loadtxt(data, usecols=(3))
Te = np.loadtxt(data, usecols=(4))

Lsun = 3.85*10**33
Ly = L/Lsun

plt.figure(1)
#plt.plot(np.log10(Te), np.log10(Ly))
plt.scatter(np.log10(Te), np.log10(Ly), s=1)
plt.gca().invert_xaxis()
plt.legend()
plt.title('Diagram HR Tiga Massa Matahari')
plt.xlabel('$log Teff (K)$')
plt.ylabel('$log (L/L\odot)$')
plt.savefig('Log Tiga Massa Matahari.png', dpi=800)
plt.show()


# In[64]:


import numpy as np
import matplotlib.pyplot as plt

data = 'Satu Massa Matahari.txt'
L = np.loadtxt(data, usecols=(3))
Te = np.loadtxt(data, usecols=(4))

Lsun = 3.85*10**33
Ly = L/Lsun

plt.figure(1)
plt.plot(np.log10(Te), np.log10(Ly))
plt.scatter(np.log10(Te), np.log10(Ly), s=5)
plt.gca().invert_xaxis()
plt.legend()
plt.title('Diagram HR Satu Massa Matahari')
plt.xlabel('$log Teff (K)$')
plt.ylabel('$log (L/L\odot)$')
plt.savefig('Log Satu Massa Matahari.png', dpi=800)
plt.show()


# In[39]:


import numpy as np
import matplotlib.pyplot as plt

data = 'Dua Massa Matahari.txt'
L = np.loadtxt(data, usecols=(3))
Te = np.loadtxt(data, usecols=(4))

Lsun = 3.85*10**33
Ly = L/Lsun

plt.figure(1)
#plt.plot(np.log10(Te), np.log10(Ly), 'grey')
plt.scatter(np.log10(Te), np.log10(Ly), s=5)
plt.gca().invert_xaxis()
plt.legend()
plt.title('Diagram HR Dua Massa Matahari')
plt.xlabel('$log Teff$')
plt.ylabel('$log (L/L\odot)$')
plt.savefig('Log Dua Massa Matahari.png', dpi=800)
plt.show()


# In[40]:


import numpy as np
import matplotlib.pyplot as plt

data = 'A.txt'
L = np.loadtxt(data, usecols=(3))
Te = np.loadtxt(data, usecols=(4))

Lsun = 3.85*10**33
Ly = L/Lsun

plt.figure(1)
#plt.plot(np.log10(Te), np.log10(Ly), 'grey')
plt.scatter(np.log10(Te), np.log10(Ly), s=5)
plt.gca().invert_xaxis()
plt.legend()
plt.title('Diagram HR')
plt.xlabel('$log Teff$')
plt.ylabel('$log (L/L\odot)$')
plt.savefig('A.png', dpi=800)
plt.show()


# In[11]:


import numpy as np
import matplotlib.pyplot as plt

data = 'polytr 1M.txt'
R = np.loadtxt(data, usecols=(0))
RHO = np.loadtxt(data, usecols=(1))

RHOc = 1.8117*10**(-9)
Rc = 4.41*10**11

x = R
y = RHO

plt.figure(1)
#plt.plot(np.log10(Te), np.log10(Ly))
plt.scatter(np.log10(x), np.log10(y), s=1)
#plt.gca().invert_xaxis()
plt.legend()
plt.title('Diagram HR Tiga Massa Matahari')
plt.xlabel('$log Teff (K)$')
plt.ylabel('$log (L/L\odot)$')
plt.savefig('Log Tiga Massa Matahari.png', dpi=800)
plt.show()

