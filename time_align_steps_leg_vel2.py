#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import math 

def time_align_steps_leg_vel2(total_flies, data, trial_samples): 
    # # Time Align Step + Coordination Metrics 
    # """
    # Data Organization: 
    #     Output: 
    #     time_aligned =  { "video_names" : [video_names], 
    #                   "velocity" : [velocity], # velocity[0][num_flies]
    #                   "step_amplitudes" : [step_amplitudes], # step_amplitudes[0][0][legs][num_flies]
    #                   "stance_durations" : [stance_durations], 
    #                   "swing_durations" : [swing_durations], 
    #                   "heading" : [heading], # heading[0][num_flies]
    #                   "step_frequencies" : [step_frequencies],
    #                   "tripod_coord" : [tripod_coord][0][fly][frames]}   
    # """
    import math 
    import numpy as np
    import matplotlib.pyplot as plt
    import h5py
    import os
    import pandas as pd 
    #matplotlib inline
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    import pandas as pd
    import seaborn as sea
    import scipy.signal
    import fnmatch as fn 
    np.set_printoptions(threshold=np.inf)
    import time_align_steps_leg_vel2 as tas2


    # %cd /Users/leesuyee/Desktop/Ms # go into directory with data
    trial_samples = 1500 

#     data = np.load('wtberlinv5.npy', allow_pickle = True) # select data file 

    # # Find size of dataset (number of videos and flies)

    total_flies = 0 
    video_num = len( data ) 

    for video in range( 0, len( data ) ): 
        num_flies = int( len( data[ video ] ) / 17 ) # length of data = number flies x 17 stored variables (see above)  
        total_flies = total_flies + num_flies # count flies through iterations 

    velocity = np.empty(( total_flies, trial_samples)) # make empty num_flies x 1500 frame array 
    velocity[:] = np.NaN # fill with nans 

    heading = np.empty(( total_flies, trial_samples)) # make mpty num_flies x 1500 frame array 
    heading[:] = np.NaN # fill with nans 
 
    rotational_vel = np.empty(( total_flies, trial_samples)) # make mpty num_flies x 1500 frame array 
    rotational_vel[:] = np.NaN # fill with nans 
    

    R1_a = np.empty(( total_flies, 1500 ))
    R2_a = np.empty(( total_flies, 1500 ))
    R3_a = np.empty(( total_flies, 1500 ))
    L1_a = np.empty(( total_flies, 1500 ))
    L2_a = np.empty(( total_flies, 1500 ))
    L3_a = np.empty(( total_flies, 1500 )) # make empty num_flies x 1500 frame array

    R1_a[:] = np.NaN
    R2_a[:] = np.NaN
    R3_a[:] = np.NaN
    L1_a[:] = np.NaN
    L2_a[:] = np.NaN
    L3_a[:] = np.NaN # fill with nans 

    R1_b = np.empty(( total_flies, 1500 ))
    R2_b = np.empty(( total_flies, 1500 ))
    R3_b = np.empty(( total_flies, 1500 ))
    L1_b = np.empty(( total_flies, 1500 ))
    L2_b = np.empty(( total_flies, 1500 ))
    L3_b = np.empty(( total_flies, 1500 )) # make empty num_flies x 1500 frame array

    R1_b[:] = np.NaN
    R2_b[:] = np.NaN
    R3_b[:] = np.NaN
    L1_b[:] = np.NaN
    L2_b[:] = np.NaN
    L3_b[:] = np.NaN # fill with nans 

    R1_c = np.empty(( total_flies, 1500 ))
    R2_c = np.empty(( total_flies, 1500 ))
    R3_c = np.empty(( total_flies, 1500 ))
    L1_c = np.empty(( total_flies, 1500 ))
    L2_c = np.empty(( total_flies, 1500 ))
    L3_c = np.empty(( total_flies, 1500 )) # make empty num_flies x 1500 frame array

    R1_c[:] = np.NaN
    R2_c[:] = np.NaN
    R3_c[:] = np.NaN
    L1_c[:] = np.NaN
    L2_c[:] = np.NaN
    L3_c[:] = np.NaN # fill with nans 

    R1_d = np.empty(( total_flies, 1500 ))
    R2_d = np.empty(( total_flies, 1500 ))
    R3_d = np.empty(( total_flies, 1500 ))
    L1_d = np.empty(( total_flies, 1500 ))
    L2_d = np.empty(( total_flies, 1500 ))
    L3_d = np.empty(( total_flies, 1500 )) # make empty num_flies x 1500 frame array

    R1_d[:] = np.NaN
    R2_d[:] = np.NaN
    R3_d[:] = np.NaN
    L1_d[:] = np.NaN
    L2_d[:] = np.NaN
    L3_d[:] = np.NaN # fill with nans 
    
    R1_e = np.empty(( total_flies, 1500 ))
    R2_e = np.empty(( total_flies, 1500 ))
    R3_e = np.empty(( total_flies, 1500 ))
    L1_e = np.empty(( total_flies, 1500 ))
    L2_e = np.empty(( total_flies, 1500 ))
    L3_e = np.empty(( total_flies, 1500 )) # make empty num_flies x 1500 frame array

    R1_e[:] = np.NaN
    R2_e[:] = np.NaN
    R3_e[:] = np.NaN
    L1_e[:] = np.NaN
    L2_e[:] = np.NaN
    L3_e[:] = np.NaN # fill with nans 
    
    R1_f = np.empty(( total_flies, 1500 ))
    R2_f = np.empty(( total_flies, 1500 ))
    R3_f = np.empty(( total_flies, 1500 ))
    L1_f = np.empty(( total_flies, 1500 ))
    L2_f = np.empty(( total_flies, 1500 ))
    L3_f = np.empty(( total_flies, 1500 )) # make empty num_flies x 1500 frame array

    R1_f[:] = np.NaN
    R2_f[:] = np.NaN
    R3_f[:] = np.NaN
    L1_f[:] = np.NaN
    L2_f[:] = np.NaN
    L3_f[:] = np.NaN # fill with nans 

    tripod_coord = np.empty(( total_flies, 1500 )) 
    tripod_coord[:] = np.NaN 


    fly_counter = -1 # for ez indexing 
    video_names = [ ]

    for video in range( 0, len( data ) ): 
        num_flies = int( len( data[ video ] ) / 17 )
        fly_video = [ ]

    #     global_variables  = global_variables[file][fly][0:14]
    #                         filename [0]
    #                         frame idx [1]
    #                         time_align_x_pos [2][leg][0]
    #                         time_align_y_pos [3][leg][0]
    #                         smoothed velocity (head) [4]  
    #                         swing_stance_mat [6]
    #                         swing_distance (step length) [7]
    #                         stance_distance (step length) [8]
    #                         swing_duration [9]
    #                         stance duration [10]
    #                         duty factor [11]
    #                         h_angle (heading angle, radians) [12]
    #                         step frequency [13] 
    #                         tripod coordination strength [14]
    #                         AEP_PEP [15] 


        for fly in range(0, num_flies): # iterate through video/fly and load in stored variables for repackaging 
            fly_counter = fly_counter + 1 # for ez indexing 
            fly_num = fly * 17
            #x_pos = global_variables[video][2 + (fly_num * 14)]
            #global_variables = data[ video ][ ( 0 + ( 14 * fly ) ):( 13 + ( 14 * fly ) ) ] # start separating the variables within global_variables 
            global_variables = data[ video ]
            filename = global_variables[ 0 + fly_num ]
            int_frame_idx = global_variables[ 1 + fly_num ]
            x_pos = global_variables[ 2 + fly_num ]
            y_pos = global_variables[ 3 + fly_num ]
            h_vel = global_variables[ 4 + fly_num ] # thorax velocity 
            swing_stance_mat = global_variables[ 5 + fly_num ] 
            swing_distance = global_variables[ 6 + fly_num ]  
            step_distance = global_variables[ 7 + fly_num ]
            swing_duration = global_variables[ 8 + fly_num ]
            stance_duration = global_variables[ 9 + fly_num ]
            heading_angle = global_variables[ 10 + fly_num ]
            rot_vel = global_variables[ 11 + fly_num ]
            step_freq = global_variables[ 12 + fly_num ] 
            tcs = global_variables[ 13 + fly_num ] 
            AEP_PEP = global_variables[ 14 + fly_num ] 
            step_phase = global_variables[15 + fly_num ] 
            relative_distance = global_variables[16 + fly_num] 


            if np.isnan(np.sum(h_vel)) == False: 

                int_h_vel = h_vel.tolist() 
                int_h_angle = heading_angle.tolist()
                int_rot_vel = rot_vel.tolist()

                R1_a[fly_counter, :] = step_distance[0]
                R2_a[fly_counter, :] = step_distance[1]
                R3_a[fly_counter, :] = step_distance[2]            
                L1_a[fly_counter, :] = step_distance[3]
                L2_a[fly_counter, :] = step_distance[4]
                L3_a[fly_counter, :] = step_distance[5]     

                R1_b[fly_counter, :] = swing_duration[0]
                R2_b[fly_counter, :] = swing_duration[1]
                R3_b[fly_counter, :] = swing_duration[2]            
                L1_b[fly_counter, :] = swing_duration[3]
                L2_b[fly_counter, :] = swing_duration[4]
                L3_b[fly_counter, :] = swing_duration[5]  

                R1_c[fly_counter, :] = stance_duration[0]
                R2_c[fly_counter, :] = stance_duration[1]
                R3_c[fly_counter, :] = stance_duration[2]            
                L1_c[fly_counter, :] = stance_duration[3]
                L2_c[fly_counter, :] = stance_duration[4]
                L3_c[fly_counter, :] = stance_duration[5] 

                R1_d[fly_counter, :] = step_freq[0]
                R2_d[fly_counter, :] = step_freq[1]
                R3_d[fly_counter, :] = step_freq[2]            
                L1_d[fly_counter, :] = step_freq[3]
                L2_d[fly_counter, :] = step_freq[4]
                L3_d[fly_counter, :] = step_freq[5] 
                
                R1_e[fly_counter, :] = step_phase[0]
                R2_e[fly_counter, :] = step_phase[1]
                R3_e[fly_counter, :] = step_phase[2]            
                L1_e[fly_counter, :] = step_phase[3]
                L2_e[fly_counter, :] = step_phase[4]
                L3_e[fly_counter, :] = step_phase[5] 
                
                R1_f[fly_counter, :] = relative_distance[0]
                R2_f[fly_counter, :] = relative_distance[1]
                R3_f[fly_counter, :] = relative_distance[2]            
                L1_f[fly_counter, :] = relative_distance[3]
                L2_f[fly_counter, :] = relative_distance[4]
                L3_f[fly_counter, :] = relative_distance[5] 

    #                 int_h_angle = h_angle.astype(int) 

            for idx in range( 1, len( int_frame_idx) ): 
                velocity[ fly_counter, int(int_frame_idx[idx])] = int_h_vel[ idx - 1 ]
                heading[ fly_counter, int(int_frame_idx[idx])] = int_h_angle[idx-1]# convert radians  to degrees
                rotational_vel[ fly_counter, int(int_frame_idx[idx])] = int_rot_vel[idx - 1] 
                
                if np.isnan(np.sum(tcs)) == False:  
                    tcs_frames = tcs[0].astype(int) 

                    for frames in range( 0, len( tcs_frames )): 
                        tripod_coord[fly_counter, tcs_frames[frames]] = tcs[ 0 ][ frames ] 

            else: 
                pass


        video_names.append(filename)

        step_amplitudes = [ ]
        step_amplitudes.append(( R1_a, R2_a, R3_a, L1_a, L2_a, L3_a ))

        swing_durations = [ ]
        swing_durations.append(( R1_b, R2_b, R3_b, L1_b, L2_b, L3_b ))

        stance_durations = [ ]
        stance_durations.append(( R1_c, R2_c, R3_c, L1_c, L2_c, L3_c ))

        step_frequencies = [  ] 
        step_frequencies.append(( R1_d, R2_d, R3_d, L1_d, L2_d, L3_d ))
        
        step_phases = [ ] 
        step_phases.append(( R1_e, R2_e, R3_e, L1_e, L2_e, L3_e ))
        
        relative_distances = [ ] 
        relative_distances.append(( R1_f, R2_f, R3_f, L1_f, L2_f, L3_f ))

    time_aligned =  { "video_names" : [video_names], 
                  "velocity" : [velocity], # velocity[0][num_flies]
                  "step_amplitudes" : [step_amplitudes], # step_amplitudes[0][0][legs][num_flies]
                  "stance_durations" : [stance_durations], 
                  "swing_durations" : [swing_durations], 
                  "heading" : [heading], # heading[0][num_flies]
                  "step_frequencies" : [step_frequencies],
                  "tripod_coord" : [tripod_coord], 
                  "step_phases" : [step_phases], 
                  "relative_distances" : [relative_distances], 
                  "rotational_velocity": [rotational_vel]} 


    # time_align = tas2.time_align_steps_leg_vel2(total_flies, data, trial_samples)

    # output structure: 
    #     time_aligned =  { "video_names" : [video_names], 
    #                   "velocity" : [velocity], # velocity[0][num_flies]
    #                   "step_amplitudes" : [step_amplitudes], # step_amplitudes[0][0][legs][num_flies]
    #                   "stance_durations" : [stance_durations], 
    #                   "swing_durations" : [swing_durations], 
    #                   "heading" : [heading], # heading[0][num_flies]
    #                   "step_frequencies" : [step_frequencies],
    #                   "tripod_coord" : [tripod_coord], 
    #                    "step_phases" : [step_phases], 
    #                    "relative_distances" : [relative_distances]} 

    return time_aligned 


