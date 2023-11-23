# KADIDIA KAREMBE Master1 janv_2023
import matplotlib.pyplot as plt
import numpy as np
def plot_curves(x_range=(-10, 10), num_points=100):
    # Générer les valeurs de x
    x = np.linspace(x_range[0], x_range[1], num_points)
    # Calculer les valeurs y pour x^2 et x^3
    y_squared = x ** 2
    y_cubed = x ** 3
    # Tracer les courbes
    plt.plot(x, y_squared, label='x^2')
    plt.plot(x, y_cubed, label='x^3')
    # Ajouter des étiquettes et un titre
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphs of x^2 and x^3')
    # Ajouter une légende
    plt.legend()
    # Activer la grille
    plt.grid(True)
    # Afficher le graphique
    plt.show()
# Appeler la fonction avec les valeurs par défaut
plot_curves()







