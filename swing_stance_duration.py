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

def swing_stance_duration(stance_start, stance_end, FPS):
    stance_duration = []
    swing_duration = []
    stance_time_store=[]
    swing_time_store=[]
    duty_factor=[]
    
#   fig_num=fig_num+1

    for leg in range(0,len(stance_start)):
        stance_delt = [] 
        swing_delt = [] 
        stance_d=[]
        swing_d=[]
        df_store=[]
        stance_time=[]
        swing_time=[]
        for stance in range(0,len(stance_start[leg])):
            itr=0
            # go until the next stance is found
            end_idx=0
            while stance_end[leg][itr] < stance_start[leg][stance]:
                itr=itr+1 # iterate through to find next end
                if itr > len(stance_end[leg])-1: # deals with boundary condition
                    break
            if itr > len(stance_end[leg])-2: # end boundary condition
                # if step (i.e. stance) is not completed then ignore the last stance initiation
                pass
            elif itr-1 < 0: # starting boundry condition
                pass
            else:
                stance_delt=(stance_end[leg][itr]-stance_start[leg][stance])/FPS
                swing_delt=(stance_start[leg][stance + 1]-stance_end[leg][itr])/FPS
                stance_d.append(stance_delt)
                swing_d.append(swing_delt)
                stance_time.append(stance_start [leg][stance])
                swing_time.append(stance_end[leg][itr-1])
                
                # compute the duty factor
                df=stance_delt/(stance_delt + swing_delt)
                df_store.append(df)
                
        duty_factor.append(np.array(df_store))
        stance_duration.append(np.array(stance_d))
        swing_duration.append(np.array(swing_d))
        stance_time_store.append(np.array(stance_time))
        swing_time_store.append(np.array(swing_time))
        
    return stance_time_store, stance_duration, swing_time_store, swing_duration, duty_factor 
            
            
  