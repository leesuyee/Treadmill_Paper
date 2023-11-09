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


def find_stance(stance_start, stance_end, swing_stance_mat):
    for leg in range(0,len(stance_start)):
        # use each stance start as a point of reference and find the next stance end point
        for stance in range(0,len(stance_start[leg])):
            itr=0
            # go until the next stance is found
            end_idx=0
            while stance_end[leg][itr] < stance_start [leg][stance]:
                itr=itr+1 # iterate through to find next end
                if itr > len(stance_end[leg])-1: # deals with boundary condition
                    break
            if itr > len(stance_end[leg])-1:
                swing_stance_mat[leg][stance_start [leg][stance]::]=1
            else:
                swing_stance_mat[leg][stance_start [leg][stance]:stance_end[leg][itr]]=1
            
    return(swing_stance_mat)