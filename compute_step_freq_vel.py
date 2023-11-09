import numpy as np

def compute_step_freq_vel(stance_start, nlegs, trial_samples, FS):
    step_frequency =  np.empty((nlegs, trial_samples))
    step_frequency[:] = np.nan
    for leg in range(len(stance_start)):
        for j in range(len(stance_start[leg])-1):
            step_duration=(stance_start[leg][j+1] - stance_start[leg][j])/FS
            if step_duration>0:
                step_frequency[leg, stance_start[leg][j]] = 1/step_duration
    
    return step_frequency

