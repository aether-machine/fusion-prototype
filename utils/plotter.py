import matplotlib.pyplot as plt
import os

def plot_field(X, Y, Z, field, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(field), rstride=1, cstride=1, antialiased=False)
    ax.set_title("Toroidal Harmonic Field")
    plt.savefig(filename)
    plt.close()
