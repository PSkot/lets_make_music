import numpy as np

def calcPressure(time, amp, freq):
    T = 1/freq
    return amp*np.sin(2*np.pi*freq*time)
