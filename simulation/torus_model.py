import numpy as np

def create_grid(config):
    size = config["grid_size"]
    radius = config["radius"]
    theta = np.linspace(0, 2 * np.pi, size)
    phi = np.linspace(0, 2 * np.pi, size)
    Theta, Phi = np.meshgrid(theta, phi)

    R = radius + 0.3 * np.cos(Theta)
    X = R * np.cos(Phi)
    Y = R * np.sin(Phi)
    Z = 0.3 * np.sin(Theta)

    return Theta, Phi, X, Y, Z
