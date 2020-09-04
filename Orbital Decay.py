
# coding: utf-8

# In[1]:


TLE = "LAPAN-A2-peluncuran-2020.txt"

print(TLE)            


# In[2]:





# In[6]:


import csv

TLE_list = []

with open('peluncuranLAPANA2.txt', newline='') as TLE:
    TLE_reader = csv.DictReader(TLE, delimiter='\t')
    for TLE in TLE_reader:
        TLE_list.append(dict(TLE))
        
print(TLE_list)


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

read_file = pd.read_csv('peluncuranLAPANA2.txt', skiprows=lambda x: not x %2)
read_file.to_csv ('evenA2.csv', index=None)

df = pd.read_csv('evenA2.csv', header=None, delimiter='\s+', usecols=[4])
e = df*10**(-7)
#print(e)

df1 = pd.read_csv('evenA2.csv', header=None, delimiter='\s+', usecols=[7])
miu = 398600
a = (miu/(df1*0.0000727221)**2)**(1/3)
#print(a)

odd = pd.read_csv('peluncuranLAPANA2.txt', skiprows=lambda x: x %2)
odd.to_csv('oddA2.csv', index=None)

df2 = pd.read_csv('oddA2.csv', header=None, delimiter='\s+', usecols=[3])
#print(df2)

plt.figure()
plt.plot(df2, e, color="tan")
plt.legend()
plt.xlabel('JD')
plt.ylabel('Eksentrisitas')
plt.savefig('deA2.png', dpi=1000)
plt.show()

plt.figure()
plt.plot(df2, a, color="maroon")
plt.legend()
plt.xlabel('JD')
plt.ylabel('$Semi$-$major$ $axis$ (km)')
plt.savefig('daA2.png', dpi=1000)
plt.show()


# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

read_file = pd.read_csv('peluncuranLAPANA3.txt', skiprows=lambda x: not x %2)
read_file.to_csv ('evenA3.csv', index=None)

df = pd.read_csv('evenA3.csv', header=None, delimiter='\s+', usecols=[4])
e = df*10**(-7)
#print(e)

df1 = pd.read_csv('evenA3.csv', header=None, delimiter='\s+', usecols=[7])
miu = 398600
a = (miu/(df1*0.0000727221)**2)**(1/3)
#print(a)

odd = pd.read_csv('peluncuranLAPANA3.txt', skiprows=lambda x: x %2)
odd.to_csv('oddA3.csv', index=None)

df2 = pd.read_csv('oddA3.csv', header=None, delimiter='\s+', usecols=[3])
#print(df2)

plt.figure()
plt.plot(df2, e, color="tan")
plt.legend()
plt.xlabel('JD')
plt.ylabel('Eksentrisitas')
plt.savefig('deA3.png', dpi=1000)
plt.show()

plt.figure()
plt.plot(df2, a, color="maroon")
plt.legend()
plt.xlabel('JD')
plt.ylabel('$Semi$-$major$ $axis$ (km)')
plt.savefig('daA3.png', dpi=1000)
plt.show()


# In[6]:


import numpy as np
import pandas as pd

data = np.loadtxt('peluncuranLAPANA2.txt')
data = pd.DataFrame(data[::2])

print(data)


# In[23]:


import pandas as pd

read_file = pd.read_csv('peluncuranLAPANA2.txt', skiprows=lambda x: not x %2)
read_file.to_csv ('TLELAPANA2.csv', index=None)

df = pd.read_csv('TLELAPANA2.csv', header=None, delimiter='\s+')

print(df)


# In[37]:


import numpy as np
import matplotlib.pyplot as plt

storm1 = '2017A2.txt'
JD1 = np.loadtxt(storm1, usecols=(0))
a1 = np.loadtxt(storm1, usecols=(4))
e1 = np.loadtxt(storm1, usecols=(6))

storm2 = '2018A2.txt'
JD2 = np.loadtxt(storm2, usecols=(0))
a2 = np.loadtxt(storm2, usecols=(4))
e2 = np.loadtxt(storm2, usecols=(6))

storm3 = '2019A2.txt'
JD3 = np.loadtxt(storm3, usecols=(0))
a3 = np.loadtxt(storm3, usecols=(4))
e3 = np.loadtxt(storm3, usecols=(6))

fig,ax=plt.subplots()
ax.plot(JD1, a1, color="red", marker="o", label='da/dt')
ax.legend(loc="center left")
ax.set_xlabel("JD")
ax.set_ylabel("$Semi$-$Major$ $Axis$ (km)")
#ax.set_ylim(7018, 7018.5)
ax2=ax.twinx()
ax2.plot(JD1, e1, color="blue", marker="o", label='de/dt')
ax2.legend(loc="center right")
ax2.set_ylabel("Eksentrisitas")
#plt.legend((ax, ax2), ('da/dt', 'de/dt'))
plt.show()
fig.savefig('2017A2.jpg', format='jpeg', dpi=1000, bbox_inches='tight')

fig,ax3=plt.subplots()
ax3.plot(JD2, a2, color="red", marker="o", label='da/dt')
ax3.legend(loc="center left")
ax3.set_xlabel("JD")
ax3.set_ylabel("$Semi$-$Major$ $Axis$ (km)")
#ax.set_ylim(7018, 7018.5)
ax4=ax3.twinx()
ax4.plot(JD2, e2, color="blue", marker="o", label='de/dt')
ax4.legend(loc="center right")
ax4.set_ylabel("Eksentrisitas")
#plt.legend((ax, ax2), ('da/dt', 'de/dt'))
plt.show()
fig.savefig('2018A2.jpg', format='jpeg', dpi=1000, bbox_inches='tight')

fig,ax5=plt.subplots()
ax5.plot(JD3, a3, color="red", marker="o", label='da/dt')
ax5.legend(loc="center left")
ax5.set_xlabel("JD")
ax5.set_ylabel("$Semi$-$Major$ $Axis$ (km)")
#ax.set_ylim(7018, 7018.5)
ax6=ax5.twinx()
ax6.plot(JD3, e3, color="blue", marker="o", label='de/dt')
ax6.legend(loc="center right")
ax6.set_ylabel("Eksentrisitas")
#plt.legend((ax, ax2), ('da/dt', 'de/dt'))
#plt.show()
#fig.savefig('2019A2.jpg', format='jpeg', dpi=1000, bbox_inches='tight')


# In[14]:





# In[48]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

storm1 = '2017A2.txt'
JD1 = np.loadtxt(storm1, usecols=(0))
a1 = np.loadtxt(storm1, usecols=(4))
e1 = np.loadtxt(storm1, usecols=(6))

fig,ax=plt.subplots()
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.plot(JD1, a1, color="maroon", label='$Semi$-$Major$ $Axis$')
ax.ticklabel_format(useOffset=False)
ax.legend()
ax.set_xlabel("JD")
ax.set_ylabel("$Semi$-$Major$ $Axis$ (km)")
#ax.set_ylim(7018, 7018.5)
ax2=ax.twinx()
ax2.plot(JD1, e1, color="coral", label='Eksentrisitas')
ax2.legend()
ax2.set_ylabel("Eksentrisitas")
#plt.legend((ax, ax2), ('da/dt', 'de/dt'))
plt.show()
fig.savefig('Perubahan Elemen Orbit A2 September 2017.png', dpi=800, bbox_inches='tight')


# In[49]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

storm2 = '2018A2.txt'
JD2 = np.loadtxt(storm2, usecols=(0))
a2 = np.loadtxt(storm2, usecols=(4))
e2 = np.loadtxt(storm2, usecols=(6))

fig,ax3=plt.subplots()
ax3.yaxis.set_major_formatter(ScalarFormatter())
ax3.plot(JD2, a2, color="maroon", label='$Semi$-$Major$ $Axis$')
ax3.ticklabel_format(useOffset=False)
ax3.legend(loc="upper left")
ax3.set_xlabel("JD")
ax3.set_ylabel("$Semi$-$Major$ $Axis$ (km)")
#ax3.set_ylim(18237.0, 18240.0, range(0.5))
ax4=ax3.twinx()
ax4.plot(JD2, e2, color="coral", label='Eksentrisitas')
ax4.legend(loc="upper right")
ax4.set_ylabel("Eksentrisitas")
#plt.legend((ax, ax2), ('da/dt', 'de/dt'))
plt.show()
fig.savefig('Perubahan Elemen Orbit A2 Agustus 2018.png', dpi=800, bbox_inches='tight')


# In[50]:


import numpy as np
import matplotlib.pyplot as plt

storm1 = '2017A3.txt'
JD1 = np.loadtxt(storm1, usecols=(0))
a1 = np.loadtxt(storm1, usecols=(4))
e1 = np.loadtxt(storm1, usecols=(6))

fig,ax=plt.subplots()
ax.plot(JD1, a1, color="maroon", label='$Semi$-$Major$ $Axis$')
ax.ticklabel_format(useOffset=False)
ax.legend(loc="upper left")
ax.set_xlabel("JD")
ax.set_ylabel("$Semi$-$Major$ $Axis$ (km)")
#ax.set_ylim(7018, 7018.5)
ax2=ax.twinx()
ax2.plot(JD1, e1, color="coral", label='Eksentrisitas')
ax2.legend(loc="upper right")
ax2.set_ylabel("Eksentrisitas")
#plt.legend((ax, ax2), ('da/dt', 'de/dt'))
plt.show()
fig.savefig('Perubahan Elemen Orbit A3 September 2017.png', dpi=800, bbox_inches='tight')


# In[51]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

storm2 = '2018A3.txt'
JD2 = np.loadtxt(storm2, usecols=(0))
a2 = np.loadtxt(storm2, usecols=(4))
e2 = np.loadtxt(storm2, usecols=(6))

fig,ax3=plt.subplots()
ax3.yaxis.set_major_formatter(ScalarFormatter())
ax3.plot(JD2, a2, color="maroon", label='$Semi$-$Major$ $Axis$')
ax3.ticklabel_format(useOffset=False)
ax3.legend(loc="upper left")
ax3.set_xlabel("JD")
ax3.set_ylabel("$Semi$-$Major$ $Axis$ (km)")
#ax3.set_ylim(18237.0, 18240.0, range(0.5))
ax4=ax3.twinx()
ax4.plot(JD2, e2, color="coral", label='Eksentrisitas')
ax4.legend(loc="upper right")
ax4.set_ylabel("Eksentrisitas")
#plt.legend((ax, ax2), ('da/dt', 'de/dt'))
plt.show()
fig.savefig('Perubahan Elemen Orbit A3 Agustus 2018.png', dpi=800, bbox_inches='tight')

