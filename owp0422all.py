
import numpy as np


def x_a(t):
  
    return np.exp(2j*np.pi*t) * (np.abs(t) < 3)

def x_d(t):
  
    return (2j/np.pi)*np.sin(t) + (3/np.pi)*np.cos(2*np.pi*t)
