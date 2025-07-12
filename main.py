import yaml
from field_generator.harmonics import generate_field
from simulation.torus_model import create_grid
from utils.plotter import plot_field

# === Load config ===
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)["simulation"]

# === Set up grid ===
theta, phi, X, Y, Z = create_grid(config)

# === Generate field ===
field = generate_field(theta, phi, config["modes"])

# === Plot ===
plot_field(X, Y, Z, field, config["output_image"])
print(f"✅ Simulation complete. Image saved to {config['output_image']}")
