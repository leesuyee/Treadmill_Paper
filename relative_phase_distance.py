
# Compare the phase relationship between legs
import numpy as np 

def relative_phase_distance(stance_start, x_pos, y_pos, trial_samples):
    leg_comparasions = [[3,0], [3,1], [3,2], [3,4], [3,5], [4,0], [4,1], [4,2], [4,5], [5,0], [5,1], [5,2], [0,1], [1,2]]
    step_phase = -np.ones((len(leg_comparasions), trial_samples))
    relative_distance = -np.ones((len(leg_comparasions), trial_samples))
    for j in range(len(leg_comparasions)):
        leg1 = leg_comparasions[j][0]
        leg2 = leg_comparasions[j][1]

        for i in range(len(stance_start[leg1])-1):
            stance_index = stance_start[leg2][np.logical_and(stance_start[leg2] >= stance_start[leg1][i], stance_start[leg2] < stance_start[leg1][i+1])]

            if len(stance_index) > 0: # make sure there is a match - only consider the first index
                step_phase[j, stance_start[leg1][i]] = (stance_start[leg1][i+1]-stance_index[0])/(stance_start[leg1][i+1]-stance_start[leg1][i])

                # relative distance
                dx = x_pos[leg1][0] - x_pos[leg2][0]
                dy = y_pos[leg1][0] - y_pos[leg2][0]
                relative_distance[j, stance_start[leg1][i]] = np.sqrt(dx[stance_start[leg1][i]]**2 + dy[stance_start[leg1][i]]**2)      
    
    return step_phase, relative_distance

