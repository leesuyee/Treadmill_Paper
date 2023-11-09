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

from scipy import signal

def swing_stance(new_x_pos, nlegs):
    
    # create empty matrix
    swing_stance_mat=np.zeros([nlegs,len(new_x_pos[0][0])])
    frames=np.arange(0,len(new_x_pos[0][0]))
    
    # find peaks parameters
    prom=0.1
    w=0
    dist=1
    
    # find the indices of local maximums (stance start)
    r1_max_pks, r1_max_properties = scipy.signal.find_peaks(new_x_pos[0][0], prominence=prom, width=w, distance=dist)
    r2_max_pks, r2_max_properties = scipy.signal.find_peaks(new_x_pos[1][0], prominence=prom, width=w, distance=dist)
    r3_max_pks, r3_max_properties = scipy.signal.find_peaks(new_x_pos[2][0], prominence=prom, width=w, distance=dist)
    l1_max_pks, l1_max_properties = scipy.signal.find_peaks(new_x_pos[3][0], prominence=prom, width=w, distance=dist)
    l2_max_pks, l2_max_properties = scipy.signal.find_peaks(new_x_pos[4][0], prominence=prom, width=w, distance=dist)
    l3_max_pks, l3_max_properties = scipy.signal.find_peaks(new_x_pos[5][0], prominence=prom, width=w, distance=dist)

    # collect the all of the stance starts starting from the second one to the second to last one
    stance_start=[r1_max_pks[1:-1], r2_max_pks[1:-1], r3_max_pks[1:-1], l1_max_pks[1:-1], l2_max_pks[1:-1], l3_max_pks[1:-1]]
    
    max_pks = [r1_max_pks, r2_max_pks, r3_max_pks, l1_max_pks, l2_max_pks, l3_max_pks] 

    # find the indices of local maximums (swing start)
    r1_min_pks, r1_min_properties = scipy.signal.find_peaks(-new_x_pos[0][0], prominence=prom, width=w, distance=dist)
    r2_min_pks, r2_min_properties = scipy.signal.find_peaks(-new_x_pos[1][0], prominence=prom, width=w, distance=dist)
    r3_min_pks, r3_min_properties = scipy.signal.find_peaks(-new_x_pos[2][0], prominence=prom, width=w, distance=dist)
    l1_min_pks, l1_min_properties = scipy.signal.find_peaks(-new_x_pos[3][0], prominence=prom, width=w, distance=dist)
    l2_min_pks, l2_min_properties = scipy.signal.find_peaks(-new_x_pos[4][0], prominence=prom, width=w, distance=dist)
    l3_min_pks, l3_min_properties = scipy.signal.find_peaks(-new_x_pos[5][0], prominence=prom, width=w, distance=dist)
    
    swing_transitions=[r1_min_pks, r2_min_pks, r3_min_pks, l1_min_pks, l2_min_pks, l3_min_pks]
    
    min_pks = [r1_min_pks, r2_min_pks, r3_min_pks, l1_min_pks, l2_min_pks, l3_min_pks] 
    
       # captured swing transitions...need to match them to the stance_transitions
    swing_transitions=[r1_min_pks, r2_min_pks, r3_min_pks, l1_min_pks, l2_min_pks, l3_min_pks]

    # determine match pairs
    stance_end=[] # store the corresponding stance ends
    for leg in range(len(stance_start)):
        leg_stances=stance_start[leg]

        # initialize the array for swing mathes
        swing_matches=np.zeros(len(leg_stances))

        # go through each stance and determine the follwoing swing time
        for j in range(len(leg_stances)):
            curr_stance = leg_stances[j]

            #find the closest swing
            diff_swing_stance = swing_transitions[leg]-curr_stance

            # ignore negative values
            pos_idxs = np.where(diff_swing_stance>0)[0]

            # match the index to the swing
            #deal with the boundary condition of not finding a corresponding swing
            if len(pos_idxs)==0:
                # take out the stance that doesn't have a match
                stance_start[leg]=leg_stances[0:j-1]
                swing_matches=swing_matches[0:j-1]
                break
            else:
                # find the index of the closest swing
                pos_vals=diff_swing_stance[pos_idxs]
                min_idx = np.argmin(pos_vals)
                swing_match=swing_transitions[leg][np.where(pos_vals[min_idx]==diff_swing_stance)[0]]
                swing_matches[j]=swing_match

        # append the matched seing transitions to the stance ends
        stance_end.append(swing_matches.astype(int))
        
    return stance_start, stance_end, swing_stance_mat, max_pks, min_pks 
            
    
    
