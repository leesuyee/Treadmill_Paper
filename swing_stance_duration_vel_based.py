#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np 

def swing_stance_duration_vel_based(stance_start, stance_end, nlegs, trial_samples, FS):
    stance_duration =  np.empty((nlegs, trial_samples))
    stance_duration[:] = np.nan

    swing_duration =  np.empty((nlegs, trial_samples))
    swing_duration[:] = np.nan

    duty_factor =  np.empty((nlegs, trial_samples))
    duty_factor[:] = np.nan

    for leg in range(len(stance_start)):
        for j in range(len(stance_start[leg])-1):
            stance_delt=(stance_end[leg][j]-stance_start[leg][j])/FS
            if stance_delt > 0:
                stance_duration[leg, stance_start[leg][j]] = stance_delt

            swing_delt=(stance_start[leg][j+1] - stance_end[leg][j])/FS
            if swing_delt > 0:
                swing_duration[leg, stance_start[leg][j]] = swing_delt

            # compute the duty factor
            if (swing_delt > 0) and (stance_delt > 0):
                df=stance_delt/(stance_delt + swing_delt)
                duty_factor[leg, stance_start[leg][j]] = df
    
    return stance_duration, swing_duration, duty_factor

