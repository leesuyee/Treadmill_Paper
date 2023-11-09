import numpy as np 

def compute_step_distance(x_pos, y_pos, stance_start, stance_end, BL, FS, nlegs, trial_samples):
    step_distance =  np.empty((nlegs, trial_samples))
    step_distance[:] = np.nan
    # compute stance and swing speed and sum both from step speed
    for leg in range(len(stance_start)):
        # calculate the stance and swing speed for each step
        for j in range(len(stance_start[leg])-1):
            # compute distance traveled during the step
            # stance distance
            st_dx = x_pos[leg][0][stance_start[leg][j]:stance_end[leg][j]]
            st_dy = y_pos[leg][0][stance_start[leg][j]:stance_end[leg][j]]
#             st_dz = z_pos_raw[leg][stance_start[leg][j]:stance_end[leg][j]]
            st_distance = np.nansum(np.sqrt(np.diff(st_dx)**2 + np.diff(st_dy)**2))/BL
            # swing distance
            sw_dx = x_pos[leg][0][stance_end[leg][j]:stance_start[leg][j+1]]
            sw_dy = y_pos[leg][0][stance_end[leg][j]:stance_start[leg][j+1]]
#             sw_dz = z_pos_raw[leg][stance_end[leg][j]:stance_start[leg][j+1]]
            sw_distance = np.nansum(np.sqrt(np.diff(sw_dx)**2 + np.diff(sw_dy)**2))/BL
            # step distance
            step_dist = st_distance + sw_distance
            if (st_distance > 0) and (sw_distance > 0):
                step_distance[leg, stance_start[leg][j]] = step_dist
    return step_distance

