
import numpy as np

def X_a(w, a, w0):

    return (a + 1j*w) / ((a + 1j*w)**2 + w0**2)

def X_c(w):

    return 2*np.sinc(w/np.pi) + np.sinc((w-np.pi)/np.pi) + np.sinc((w+np.pi)/np.pi)

def X_d(w, a, T):

    return 1 / (1 - a*np.exp(-1j*w*T))

def X_e(w):
    return 8*(2 + 1j*w) / ((2 + 1j*w)**2 + 16)**2

def X_g(w):

    if w == 0:
        return 0

    
    return -2j*(np.sin(w)/w**2 - np.cos(2*w)/w)

def X_i(w):
    
    if w == 0:
        return 0
    
    return ((1j*w)**2 - 2 + 2*(1+1j*w)*np.exp(-1j*w)) / (1j*w)**3

