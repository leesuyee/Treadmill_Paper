import h5py
import os
import math

#matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import seaborn as sea
import scipy.signal
import read_data as rd
import organize_data as od
import fill_nans as fill
import velocity as vel 
import swing_stance as s_s 

from scipy import signal

def fill_nans(points):
    A = points
    if np.isnan(points).all()==True:
        A = np.zeros([len(points)])

    
    elif np.isnan(points).all()==False:
        ok = ~np.isnan(A)
        xp = ok.ravel().nonzero()[0]
        fp = A[~np.isnan(A)]
        x  = np.isnan(A).ravel().nonzero()[0]

        A[np.isnan(A)] = np.interp(x, xp, fp)

    return A 

