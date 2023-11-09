import numpy as np 

def filter(step_time_store, step_amp_store, frame_idx, h_vel):
    control_step_amp_store = [] 
    control_step_amp_bin_one_store = []
    control_step_amp_bin_two_store = []
    control_step_amp_bin_three_store = []
    control_step_amp_bin_four_store = []
    control_step_amp_bin_five_store = []


    stim_step_amp_store = [] 
    stim_step_amp_bin_one_store = []
    stim_step_amp_bin_two_store = []
    stim_step_amp_bin_three_store = []
    stim_step_amp_bin_four_store = []
    stim_step_amp_bin_five_store = []

    for leg in range(0, len(step_time_store)): 
        control_step_amp= []
        control_step_amp_bin_one = []
        control_step_amp_bin_two = []
        control_step_amp_bin_three = []
        control_step_amp_bin_four = []
        control_step_amp_bin_five = []

        stim_step_amp = [] 
        stim_step_amp_bin_one = []
        stim_step_amp_bin_two = []
        stim_step_amp_bin_three = []
        stim_step_amp_bin_four = []
        stim_step_amp_bin_five = []


        for step in range(0,len(step_time_store[leg])): 
            idx = step_time_store[leg][step]

            if frame_idx[idx]<=750: 
                control_step_amp.append(step_amp_store[leg][step])

                if h_vel[idx]<=3: 
                    control_step_amp_bin_one.append(step_amp_store[leg][step])

                elif h_vel[idx]>=4 and h_vel[idx]<=10: 
                    control_step_amp_bin_two.append(step_amp_store[leg][step])

                elif h_vel[idx]>=11 and h_vel[idx]<=20:
                    control_step_amp_bin_three.append(step_amp_store[leg][step])            

                elif h_vel[idx]>=21 and h_vel[idx]<=30: 
                    control_step_amp_bin_three.append(step_amp_store[leg][step])                

                elif h_vel[idx]>=31 and h_vel[idx]<=40: 
                    control_step_amp_bin_four.append(step_amp_store[leg][step])   

                elif h_vel[idx]>= 41:
                    control_step_amp_bin_five.append(step_amp_store[leg][step])    


            elif frame_idx[idx]>=751: 
                stim_step_amp.append(step_amp_store[leg][step])

                if h_vel[idx]<=3: 
                    stim_step_amp_bin_one.append(step_amp_store[leg][step]) 

                elif h_vel[idx]>=4 and h_vel[idx]<=10: 
                    stim_step_amp_bin_two.append(step_amp_store[leg][step])

                elif h_vel[idx]>=11 and h_vel[idx]<=20: 
                    stim_step_amp_bin_three.append(step_amp_store[leg][step])            

                elif h_vel[idx]>=21 and h_vel[idx]<=30: 
                    stim_step_amp_bin_three.append(step_amp_store[leg][step])                

                elif h_vel[idx]>=31 and h_vel[idx]<=40: 
                    stim_step_amp_bin_four.append(step_amp_store[leg][step])   

                elif h_vel[idx]>= 41:
                    stim_step_amp_bin_five.append(step_amp_store[leg][step])

        control_step_amp_store.append(np.array(control_step_amp))
        control_step_amp_bin_one_store.append(np.array(control_step_amp_bin_one))
        control_step_amp_bin_two_store.append(np.array(control_step_amp_bin_two))
        control_step_amp_bin_three_store.append(np.array(control_step_amp_bin_three)) 
        control_step_amp_bin_four_store.append(np.array(control_step_amp_bin_four))
        control_step_amp_bin_five_store.append(np.array(control_step_amp_bin_five)) 

        stim_step_amp_store.append(np.array(stim_step_amp)) 
        stim_step_amp_bin_one_store.append(np.array(stim_step_amp_bin_one))
        stim_step_amp_bin_two_store.append(np.array(stim_step_amp_bin_two))
        stim_step_amp_bin_three_store.append(np.array(stim_step_amp_bin_three)) 
        stim_step_amp_bin_four_store.append(np.array(stim_step_amp_bin_four))
        stim_step_amp_bin_five_store.append(np.array(stim_step_amp_bin_five))                   

    return control_step_amp_store, control_step_amp_bin_one_store, control_step_amp_bin_two_store,control_step_amp_bin_three_store,control_step_amp_bin_four_store, control_step_amp_bin_five_store, stim_step_amp_store, stim_step_amp_bin_one_store, stim_step_amp_bin_two_store, stim_step_amp_bin_three_store, stim_step_amp_bin_four_store, stim_step_amp_bin_five_store

    #return control_step_amp_store