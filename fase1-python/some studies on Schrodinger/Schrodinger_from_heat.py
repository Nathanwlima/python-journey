import numpy as np
import matplotlib.pyplot as plt

DeltaX = 1
DeltaT = 0.1
D =0.001+ 0.5j
nt= 1001
nx = 501
meio =int((nx-1)/2)
u =np.zeros((nt,nx), dtype=complex)
p=np.zeros((nt,nx))
meio = int((nx-1)/2)
x = np.arange(nx)          
sigma = 3
u[0] = np.exp(-0.5*((x - meio)/sigma)**2)   

i=1
for i in range (1,nt):
    j=1
    for j in range (1,nx-1):
        u[i,j] = u[i-1,j] + ((D*DeltaT)/((DeltaX)**2))*(u[i-1,j+1]-2*u[i-1,j]+ u[i-1,j-1])
        j=j+1   
    i = i+1

p=(u*u.conjugate()).real
tempos = [0, 10, 100, 1000]

cores = ['blue', 'green', 'orange', 'red']
for t, cor in zip(tempos, cores):
    curva = p[t]
    area = np.trapezoid(curva, x)   # ou np.trapz(curva, x) se numpy < 2.0
    curva_norm = curva / area
    plt.plot(x, curva_norm, color=cor, label=f"t={t}")

plt.legend()
plt.xlabel("posição")
plt.ylabel("|ψ|² normalizado")
plt.title("Alargamento do pacote gaussiano")
plt.show()
