import numpy as np
  
def compute_step_freq(step_time_store):
    step_frequency=[]
    
    for leg in range(len(step_time_store)):
        # get times of when stance starts
        step_duration = np.diff(np.array(step_time_store[leg]))/150
        step_freq = 1/step_duration
       
        step_frequency.append(step_freq)

    return step_frequency 
