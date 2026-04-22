import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
import sympy as sp

print("NumPy:", np.__version__)
print("SymPy:", sp.__version__)
print("Todas as bibliotecas funcionando!")

# Teste rápido com número complexo
psi = np.array([1+2j, 3+4j])
print("Função de onda:", psi)
print("Módulo ao quadrado:", np.abs(psi)**2)