import numpy as np

def angular_toroidal_modes(theta, phi, modes, param=0.0, use_radius=True):
    field = np.zeros_like(theta, dtype=np.float64)
    for n_theta, n_phi, omega in modes:
        phase = n_theta * theta + n_phi * phi - omega * (param if use_radius else 0.0)
        field += np.cos(phase)
    return field

def normalize_field(field):
    min_val = np.min(field)
    max_val = np.max(field)
    return (field - min_val) / (max_val - min_val)
