from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt

# Estado |+> -- superposição igual de |0> e |1>
plot_bloch_vector([1, 1, 1], title="Estado |+>")
plt.show()