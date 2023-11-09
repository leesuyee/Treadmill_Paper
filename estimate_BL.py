#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np 
def estimate_BL(body_pos):

    # head coordinates
    hx = body_pos[0]
    hy = body_pos[1]

    # abdomen coordinates
    ax = body_pos[4]
    ay = body_pos[5]

    # compute the difference
    dx = hx - ax
    dy = hy - ay

    # Calculate the body lengths for the trial
    BL = np.sqrt(dx**2 + dy**2)

    # filter the body length for when the fly is walking
    #filtered_BL = BL[walking_indices]

    # calculate the median BL
    return np.median(BL)

