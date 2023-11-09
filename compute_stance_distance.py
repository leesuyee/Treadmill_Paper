import numpy as np 

def compute_stance_distance(stance_start, stance_end, x_pos, y_pos, BL, nlegs, trial_samples):
    stance_distance =  np.empty((nlegs, trial_samples))
    stance_distance[:] = np.nan
    for leg in range(len(stance_start)):
        for j in range(len(stance_start[leg])):
            # compute step length
            dx = x_pos[leg][stance_start[leg][j]:stance_end[leg][j]]
            dy = y_pos[leg][stance_start[leg][j]:stance_end[leg][j]]
            amplitude=np.sum(np.sqrt(np.diff(dx)**2 + np.diff(dy)**2))/BL

            # filter out zero distance because it is attibuted to a tracking error
            if amplitude > 0:
                stance_distance[leg,stance_start[leg][j]] = amplitude # normalize by body length
            
    return stance_distance

