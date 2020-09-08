import numpy as np
def detect_anomalies(series):
    mean = np.mean(series)
    std = np.std(series)
    return np.abs(series - mean) > 3 * std
print('Time series anomaly detector ready.')
