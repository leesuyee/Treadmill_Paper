import numpy as np 

def compute_swing_distance(stance_start, stance_end, x_pos, y_pos, BL, nlegs, trial_samples):
    swing_distance =  np.empty((nlegs, trial_samples))
    swing_distance[:] = np.nan
    for leg in range(len(stance_start)):
        for j in range(len(stance_start[leg])-1):
            # compute step length
            dx = x_pos[leg][0][stance_end[leg][j]:stance_start[leg][j+1]] 
            dy = y_pos[leg][0][stance_end[leg][j]:stance_start[leg][j+1]]
            amplitude=np.sum(np.sqrt(np.diff(dx)**2 + np.diff(dy)**2))/BL 

            # filter out zero distance because it is attibuted to a tracking error
            if amplitude > 0:
                swing_distance[leg,stance_start[leg][j]] = amplitude # normalize by body length

    return swing_distance

