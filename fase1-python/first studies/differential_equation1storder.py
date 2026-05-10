import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp

def equation(t,y):
    return y-(t**2)-1

t_span = (0, 5)
t_eval = np.linspace(0, 5, 100)

y0= [0.5]

result = solve_ivp(equation, t_span, y0, t_eval=t_eval)
plt.plot(result.t, result.y[0])
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solução da EDO')
plt.grid()

plt.show()