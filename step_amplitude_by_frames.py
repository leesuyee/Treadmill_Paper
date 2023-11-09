#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

#update to sum movement over frames of step period 

# step_period = stance_start: stance_start-1 
# calculate dx and dy over each frame to the end of step 
# calculate amplitude for each frame to the end of step 
# sum total for step length (more accurate, incorporates more of curve) 
def step_amplitude_by_frames(stance_start, stance_end, time_align_x_pos, time_align_y_pos):
    step_amp_store=[]
    step_time_store=[] # frame number of when stance is entered
    for leg in range(0,len(stance_start)):
        # use each stance start as a point of reference and find the next stance end point
        step_amp=[]
        step_frame = []
        for stance in range(0,len(stance_start[leg])):
            sum_amp = []
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
                step_frame.append(stance_start [leg][stance])
                step_range = [i for i in range(stance_start[leg][stance],stance_end[leg][itr]+1)]
                dx = np.diff(time_align_x_pos[0][0][step_range])
                dy = np.diff(time_align_y_pos[0][0][step_range])
                for dx_idx in range(0, len(dx)): 
                    amplitude = np.sqrt(math.pow(dx[dx_idx],2) + math.pow(dy[dx_idx],2))
                    sum_amp.append(amplitude)

                single_step_amp = np.sum(sum_amp) 

            step_amp.append(single_step_amp) 

        step_amp_store.append(np.array(step_amp))
        step_time_store.append(np.array(step_frame))

    return(step_amp_store, step_time_store)

