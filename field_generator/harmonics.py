from utils.math_utils import angular_toroidal_modes, normalize_field

def generate_field(theta, phi, modes, param=0.0, use_radius=True):
    field = angular_toroidal_modes(theta, phi, modes, param=param, use_radius=use_radius)
    return normalize_field(field)
