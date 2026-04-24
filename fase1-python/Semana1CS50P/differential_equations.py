import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp

# ============================================
# JEITO 1 — Analítico com SymPy
# ============================================
t = sp.Symbol('t')
y = sp.Function('y')

edo = sp.Eq(y(t).diff(t), -2 * y(t))
solucao = sp.dsolve(edo, y(t), ics={y(0): 1})
print("Solução analítica:", solucao)

# ============================================
# JEITO 2 — Numérico com SciPy
# ============================================
def edo_numerica(t, y):
    return -2 * y

t_span = (0, 5)
t_eval = np.linspace(0, 5, 100)
y0 = [1]

resultado = solve_ivp(edo_numerica, t_span, y0, t_eval=t_eval)

# ============================================
# PLOTAR OS DOIS JUNTOS
# ============================================
t_analitico = np.linspace(0, 5, 100)
y_analitico = np.exp(-2 * t_analitico)

plt.figure(figsize=(8, 5))
plt.plot(t_analitico, y_analitico, 'b-', linewidth=2, label='Analítico')
plt.plot(resultado.t, resultado.y[0], 'r--', linewidth=2, label='Numérico (SciPy)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('dy/dt = -2y  —  Solução analítica vs numérica')
plt.legend()
plt.grid(True)
plt.savefig('edo_resultado.png')
print("Gráfico salvo como edo_resultado.png!")