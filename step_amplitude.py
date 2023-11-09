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
from scipy import signal

def step_amplitude(stance_start, stance_end, x_pos, y_pos):
    step_amp_store=[]
    step_time_store=[] # frame number of when stance is entered
    for leg in range(0,len(stance_start)):
        # use each stance start as a point of reference and find the next stance end point
        step_amp=[]
        step_frame=[]
        for stance in range(0,len(stance_start[leg])):
            itr=0
            # go until the next stance is found
            end_idx=0
            while stance_end[leg][itr] < stance_start [leg][stance]:
                itr=itr+1 # iterate through to find next end
                if itr > len(stance_end[leg])-1: # deals with boundary condition
                    break
            if itr > len(stance_end[leg])-1:
                # if step (i.e. stance) is not completed then ignore the last stance initiation
                pass
            else:
                # compute step length
                dx=x_pos[leg][0][stance_start [leg][stance]] - x_pos[leg][0][stance_end[leg][itr]]
                dy=y_pos[leg][0][stance_start [leg][stance]] - y_pos[leg][0][stance_end[leg][itr]]
                amplitude=np.sqrt(math.pow(dx,2) + math.pow(dy,2))
                step_amp.append(amplitude)
                step_frame.append(stance_start [leg][stance])

        step_amp_store.append(np.array(step_amp))
        step_time_store.append(np.array(step_frame))
            
    return(step_amp_store, step_time_store)