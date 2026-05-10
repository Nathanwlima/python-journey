import numpy as np
import matplotlib.pyplot as plt

DeltaX = 1
DeltaT = 0.1
D =1
nt= 1001
nx = 101
meio =int((nx-1)/2)
u =np.zeros((nt,nx))

u[0, meio] = 1000
u[0, meio+1] = 1000
u[0, meio-1] = 1000
u[0, meio+2] = 1000
u[0, meio-2] = 1000
u[0, meio+3] = 1000
u[0, meio-3] = 1000
u[0, meio+4] = 1000
u[0, meio-4] = 1000




i=1
for i in range (1,nt):
    j=1
    for j in range (1,nx-1):
        u[i,j] = u[i-1,j] + ((D*DeltaT)/((DeltaX)**2))*(u[i-1,j+1]-2*u[i-1,j]+ u[i-1,j-1])
        j=j+1
    u[i,0] = u[i-1,0] + ((D*DeltaT)/((DeltaX)**2))*(u[i-1,1]- u[i-1,0])
    u[i,nx-1] = u[i-1,nx-1] + ((D*DeltaT)/((DeltaX)**2))*(-u[i-1,nx-1]+ u[i-1,nx-2])

    i = i+1



plt.plot(u[0], label="t=0")
plt.plot(u[10], label="t=10")
plt.plot(u[50], label="t=50")
plt.plot(u[100], label="t=100")
plt.plot(u[300], label="t=300")
plt.plot(u[500], label="t=500")
plt.plot(u[1000], label="t=1000")

plt.legend()

plt.xlabel("posição")
plt.ylabel("temperatura")
plt.title("Evolução da equação do calor")

plt.show()

plt.imshow(u, aspect='auto')
plt.colorbar()
plt.xlabel("posição")
plt.ylabel("tempo")
plt.title("Equação do calor")
plt.show()

for i in range(100):
    plt.clf()
    plt.plot(u[i])
    plt.ylim(0, 1000)  # mantém escala fixa
    plt.title(f"t = {i}")
    plt.pause(0.1)
    plt.xlabel("posição")
    plt.ylabel("temperatura")

plt.show()