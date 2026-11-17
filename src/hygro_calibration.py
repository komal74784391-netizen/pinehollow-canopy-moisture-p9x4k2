import numpy as np

def fit_offset(reference, candidate):
    """Robust affine correction between a reference and a consumer sensor."""
    a, b = np.polyfit(reference, candidate, 1)
    residual = candidate - (a * reference + b)
    return a, b, float(np.std(residual))

def apply_correction(candidate, a, b):
    return (candidate - b) / a
