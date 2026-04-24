import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# ============================================
# PARÂMETROS DO POÇO
# ============================================
L = 1.0          # largura do poço (unidades arbitrárias)
N = 1000         # número de pontos
x = np.linspace(0, L, N)
niveis = 4       # quantos níveis plotar

# ============================================
# SOLUÇÃO ANALÍTICA
# energia e função de onda para cada nível n
# ============================================
# Em unidades onde hbar=1, 2m=1:
# E_n = n² * pi² / L²
# psi_n = sqrt(2/L) * sin(n*pi*x/L)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
cores = ['blue', 'red', 'green', 'purple']

for n in range(1, niveis + 1):
    # Energia
    E_n = (n**2 * np.pi**2) / (L**2)

    # Função de onda
    psi_n = np.sqrt(2/L) * np.sin(n * np.pi * x / L)

    # Densidade de probabilidade
    prob_n = psi_n**2

    # Plot das funções de onda (deslocadas pelo nível de energia)
    axes[0].plot(x, psi_n + E_n, color=cores[n-1], linewidth=2, label=f'n={n}, E={E_n:.1f}')
    axes[0].axhline(y=E_n, color=cores[n-1], linestyle='--', alpha=0.4)

    # Plot das densidades de probabilidade
    axes[1].plot(x, prob_n, color=cores[n-1], linewidth=2, label=f'n={n}')

# Poço infinito — paredes
for ax in axes:
    ax.axvline(x=0, color='black', linewidth=3)
    ax.axvline(x=L, color='black', linewidth=3)
    ax.legend()
    ax.grid(True, alpha=0.3)

axes[0].set_title('Funções de onda ψₙ(x)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('ψₙ(x) + Eₙ')

axes[1].set_title('Densidade de probabilidade |ψₙ(x)|²')
axes[1].set_xlabel('x')
axes[1].set_ylabel('|ψₙ(x)|²')

plt.suptitle('Poço Infinito — Primeiros 4 níveis de energia', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('poco_infinito.png', dpi=150)
print("Gráfico salvo como poco_infinito.png!")

# Imprime os níveis de energia
print("\nNíveis de energia:")
for n in range(1, niveis + 1):
    E_n = (n**2 * np.pi**2) / (L**2)
    print(f"  E_{n} = {E_n:.4f}  (proporção: {n**2})")