#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# compute the AEP and PEP 
import numpy as np 

def compute_AEP_PEP(x_pos, y_pos, stance_start, stance_end, BL, nlegs, trial_samples):
    AEPx =  np.empty((nlegs, trial_samples))
    AEPx[:] = np.nan
    AEPy =  np.empty((nlegs, trial_samples))
    AEPy[:] = np.nan
    PEPx =  np.empty((nlegs, trial_samples))
    PEPx[:] = np.nan
    PEPy =  np.empty((nlegs, trial_samples))
    PEPy[:] = np.nan
    
    for leg in range(len(stance_start)):
        for j in range(len(stance_start[leg])- 1):
            # determine x and y position of AEP at the onset of stance normalized by body length
            AEPx[leg, stance_start[leg][j]] = x_pos[leg][0][stance_start[leg][j]]/BL
            AEPy[leg, stance_start[leg][j]] = y_pos[leg][0][stance_start[leg][j]]/BL

            # determine x and y position of PEP at swing start/ end of stance phase normalized by body length
            PEPx[leg, stance_start[leg][j]] = x_pos[leg][0][stance_end[leg][j]]/BL
            PEPy[leg, stance_start[leg][j]] = y_pos[leg][0][stance_end[leg][j]]/BL

    return AEPx, AEPy, PEPx, PEPy

