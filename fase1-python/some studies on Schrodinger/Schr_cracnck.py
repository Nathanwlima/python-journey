import numpy as np
import matplotlib
matplotlib.use('Agg')  # evita erro de interface (Tkinter)
import matplotlib.pyplot as plt

# parâmetros
nx = 101
nt = 500
DeltaX = 1.0
DeltaT = 0.1

alpha = 1j * DeltaT / (2 * DeltaX**2)

# espaço
x = np.arange(nx)
meio = nx // 2

# pacote gaussiano inicial
sigma = 5
u = np.exp(-(x - meio)**2 / (2 * sigma**2)).astype(complex)

# normalização
u = u / np.sqrt(np.sum(np.abs(u)**2))

# matrizes
A = np.zeros((nx, nx), dtype=complex)
B = np.zeros((nx, nx), dtype=complex)

for i in range(1, nx-1):
    A[i, i-1] = -alpha
    A[i, i]   = 1 + 2*alpha
    A[i, i+1] = -alpha

    B[i, i-1] = alpha
    B[i, i]   = 1 - 2*alpha
    B[i, i+1] = alpha

# condições de contorno
A[0,0] = A[-1,-1] = 1
B[0,0] = B[-1,-1] = 1

# armazenamento
u_t = np.zeros((nt, nx), dtype=complex)
u_t[0] = u

# evolução temporal
for n in range(1, nt):
    b = B @ u
    u = np.linalg.solve(A, b)
    u_t[n] = u

# densidade
p = np.abs(u_t)**2

# checar norma
print("Norma:")
for t in [0, 50, 100, 200, 400]:
    print(t, np.sum(p[t]))

# gráfico
plt.figure()
plt.plot(p[0], label="t=0")
plt.plot(p[50], label="t=50")
plt.plot(p[100], label="t=100")
plt.plot(p[200], label="t=200")
plt.plot(p[400], label="t=400")

plt.legend()
plt.xlabel("posição")
plt.ylabel("|ψ|²")
plt.title("Pacote Gaussiano - Crank Nicolson")

plt.savefig("evolucao.png", dpi=150)
plt.close()

print("Gráfico salvo como evolucao.png")