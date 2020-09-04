import math
import matplotlib.pyplot as plt
import numpy 
pi = numpy.pi
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(nu, temp) :
    x = 8.0*pi*h*nu**3
    y = (h*nu)/(k*temp)
    intensity = x/((c**3)*(math.e**y-1.0))
    return intensity

def rayjeans(nu, temp) :
    intensity = (8.0*pi*nu**2*k*temp)/(c**3)
    return intensity

def wien(nu, temp) :
    x = 8.0*pi*h*nu**3
    y = (h*nu)/(k*temp)
    intensity = x/((c**3)*(math.e**y))
    return intensity
   
nuplanck = numpy.arange (0, 15e+15, 1e+12)
nurj = numpy.arange (0, 15e+15, 1e+12)
nuwien = numpy.arange (0, 15e+15, 1e+12)

p5500 = planck(nuplanck, 5500)
p7500 = planck(nuplanck, 7500)
p9000 = planck(nuplanck, 9000)
r5500 = rayjeans(nurj, 5500)
r7500 = rayjeans(nurj, 7500)
r9000 = rayjeans(nurj, 9000)
w5500 = wien(nuwien, 5500)
w7500 = wien(nuwien, 7500)
w9000 = wien(nuwien, 9000)

plt.plot()
plt.plot(nuplanck, p5500, 'b-', label = 'Planck 5500 K')
plt.plot(nuplanck, p7500, 'r-', label = 'Planck 7500 K')
plt.plot(nuplanck, p9000, 'g-', label = 'Planck 9000 K')
plt.plot(nurj, r5500, 'y-', label = 'Rayleigh-Jeans 5500 K')
plt.plot(nurj, r7500, 'b-', label = 'Rayleigh-Jeans 7500 K')
plt.plot(nurj, r9000, 'c-', label = 'Rayleigh-Jeans 9000 K')
plt.plot(nuwien, w5500, 'k--', label = 'Wien 5500 K')
plt.plot(nuwien, w7500, 'm--', label = 'Wien 7500 K')
plt.plot(nuwien, w9000, 'c--', label = 'Wien 9000 K')
plt.legend()
plt.xlabel('ν (THz)')
plt.title('Distribusi Radiasi dalam Frekuensi')
plt.ylabel('Intensistas Radiasi u(ν)')
plt.xlim(0, 20e+14)
plt.ylim(0, 1e-14)
plt.savefig('grafik ν.jpg')
plt.show()