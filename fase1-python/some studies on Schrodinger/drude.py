import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp

a=1
b=1


def drude(t, Y):
    x, v = Y
    return [v, -a*v + b]

t_span = (0, 10)
t_eval = np.linspace(0, 10, 200)

y0 = [0, 0]  # x(0)=0, v(0)=0

sol = solve_ivp(drude, t_span, y0, t_eval=t_eval)

#plt.plot(sol.t, sol.y[0], label='posição x(t)')
plt.plot(sol.t, sol.y[1], label='velocidade v(t)')
plt.legend()
plt.grid()
plt.show()