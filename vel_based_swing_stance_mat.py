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
import read_data as rd
import organize_data as od
import fill_nans as fill
import velocity as vel 
import swing_stance as s_s 

from scipy import signal


def vel_based_swing_stance_mat(stance_period, swing_period, swing_stance_mat):
    for leg in range(0,len(stance_period)):
        swing_stance_mat[leg][stance_period[leg][0]] = 1 
        swing_stance_mat[leg][swing_period[leg][0]] = 0 
      
    return(swing_stance_mat)

