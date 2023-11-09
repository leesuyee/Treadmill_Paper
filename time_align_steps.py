import numpy as np 
import math 

def time_align_steps(total_flies, data): 
    velocity = np.empty(( total_flies, 1500)) # make empty num_flies x 1500 frame array 
    velocity[:] = np.NaN # fill with nans 

    heading = np.empty(( total_flies, 1500)) # make mpty num_flies x 1500 frame array 
    heading[:] = np.NaN # fill with nans 

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

    tripod_coord = np.empty(( total_flies, 1500 )) 
    tripod_coord[:] = np.NaN 


    fly_counter = -1 # for ez indexing 
    video_names = [ ]

    for video in range( 0, len( data ) ): 
        num_flies = int( len( data[ video ] ) / 17 )
        fly_video = [ ]

        for fly in range(0, num_flies): # iterate through video/fly and load in stored variables for repackaging 
            fly_counter = fly_counter + 1 # for ez indexing 
            fly_num = fly * 17
            #x_pos = global_variables[video][2 + (fly_num * 17)]
            #global_variables = data[ video ][ ( 0 + ( 17 * fly ) ):( 13 + ( 17 * fly ) ) ] # start separating the variables within global_variables 
            global_variables = data[ video ]
            filename = global_variables[ 0 + fly_num ]
            frame_idx = global_variables[ 1 + fly_num ]
            x_pos = global_variables[ 2 + fly_num ]
            max_pks = global_variables[ 3 + fly_num ]
            min_pks = global_variables[ 4 + fly_num ] 
            h_vel = global_variables[ 5 + fly_num ] # head velocity 
            swing_stance_mat = global_variables[ 6 + fly_num ] 
            step_amp_store = global_variables[ 7 + fly_num ]  
            step_time_store = global_variables[ 8 + fly_num ]
            stance_time_store = global_variables[ 9 + fly_num ]
            stance_duration = global_variables[ 10 + fly_num ]
            swing_time_store = global_variables[ 11 + fly_num ]
            swing_duration = global_variables[ 12 + fly_num ]
            duty_factor = global_variables[ 13 + fly_num ] 
            h_angle = global_variables[ 14 + fly_num ] 
            step_freq = global_variables[ 15 + fly_num ] 
            tcs = global_variables[ 16 + fly_num ] 
            int_frame_idx = frame_idx.astype(int)

            if np.isnan(np.sum(h_vel)) == True: 

                pass 

            else: 
                int_h_vel = h_vel.astype(int)
    #                 int_h_angle = h_angle.astype(int) 

                for idx in range( 1, len( int_frame_idx) ): 
                    velocity[ fly_counter, int(int_frame_idx[idx])] = int_h_vel[ idx - 1  ]
                    heading[ fly_counter, int(int_frame_idx[idx])] = math.degrees(h_angle[idx-1]) # convert radians  to degrees

                if np.isnan(np.sum(tcs[0])) == False:  
                    tcs_frames = tcs[0].astype(int) 

                    for frames in range( 0, len( tcs_frames )): 
                        tripod_coord[fly_counter, tcs_frames[frames]] = tcs[ 1 ][ frames ] 

                else: 
                    pass 


                for leg in range (0, 6): 
                    for steps in range (0, len(step_time_store [ leg] ) ): 

                        if leg == 0: 
                            R1_a[fly_counter, int((step_time_store[0][steps]))] = step_amp_store[ 0 ][ steps ] # 0 = R1
                        if leg == 1: 
                            R2_a[fly_counter, int((step_time_store[1][steps]))] = step_amp_store[ 1 ][ steps ] # 1 = R2
                        if leg == 2: 
                            R3_a[fly_counter, int((step_time_store[2][steps]))] = step_amp_store[ 2 ][ steps ] # 2 = R3

                        if leg == 3: 
                            L1_a[fly_counter, int((step_time_store[3][steps]))] = step_amp_store[ 3 ][ steps ] # 3 = L1

                        if leg == 4: 
                            L2_a[fly_counter, int((step_time_store[4][steps]))] = step_amp_store[ 4 ][ steps ] # 4 = L2

                        if leg == 5: 
                            L3_a[fly_counter, int((step_time_store[5][steps]))] = step_amp_store[ 5 ][ steps ] # 5 = L3



                    for steps in range( 0, len( stance_time_store [ leg ] ) ): 

                        if leg == 0: 
                            R1_b[fly_counter, int((stance_time_store[leg][steps]))] = stance_duration[ 0 ][ steps ] # 0 = R1
                            R1_d[fly_counter, int((stance_time_store[leg][steps]))] = step_freq[ 0 ][ steps ] # 0 = R1
                        if leg == 1: 
                            R2_b[fly_counter, int((stance_time_store[leg][steps]))] = stance_duration[ 1 ][ steps ] # 1 = R2
                            R2_d[fly_counter, int((stance_time_store[leg][steps]))] = step_freq[ 1 ][ steps ] # 0 = R1
                        if leg == 2: 
                            R3_b[fly_counter, int((stance_time_store[leg][steps]))] = stance_duration[ 2 ][ steps ] # 2 = R3
                            R3_d[fly_counter, int((stance_time_store[leg][steps]))] = step_freq[ 2 ][ steps ] # 0 = R1
                        if leg == 3: 
                            L1_b[fly_counter, int((stance_time_store[leg][steps]))] = stance_duration[ 3 ][ steps ] # 3 = L1
                            L1_d[fly_counter, int((stance_time_store[leg][steps]))] = step_freq[ 3 ][ steps ] # 0 = R1
                        if leg == 4: 
                            L2_b[fly_counter, int((stance_time_store[leg][steps]))] = stance_duration[ 4 ][ steps ] # 4 = L2
                            L2_d[fly_counter, int((stance_time_store[leg][steps]))] = step_freq[ 4 ][ steps ] # 0 = R1
                        if leg == 5: 
                            L3_b[fly_counter, int((stance_time_store[leg][steps]))] = stance_duration[ 5 ][ steps ] # 5 = L3
                            L3_d[fly_counter, int((stance_time_store[leg][steps]))] = step_freq[ 5 ][ steps ] # 0 = R1

                    for steps in range( 0, len( swing_time_store [ leg ] ) ): 

                        if leg == 0: 
                            R1_c[fly_counter, int((swing_time_store[leg][steps]))] = swing_duration[ 0 ][ steps ] # 0 = R1
                        if leg == 1: 
                            R2_c[fly_counter, int((swing_time_store[leg][steps]))] = swing_duration[ 1 ][ steps ] # 1 = R2
                        if leg == 2: 
                             R3_c[fly_counter, int((swing_time_store[leg][steps]))] = swing_duration[ 2 ][ steps ] # 2 = R3
                        if leg == 3: 
                             L1_c[fly_counter, int((swing_time_store[leg][steps]))] = swing_duration[ 3 ][ steps ] # 3 = L1
                        if leg == 4: 
                            L2_c[fly_counter, int((swing_time_store[leg][steps]))] = swing_duration[ 4 ][ steps ] # 4 = L2
                        if leg == 5: 
                            L3_c[fly_counter, int((swing_time_store[leg][steps]))] = swing_duration[ 5 ][ steps ] # 5 = L3


        video_names.append(filename)

        step_amplitudes = [ ]
        step_amplitudes.append(( R1_a, R2_a, R3_a, L1_a, L2_a, L3_a ))

        stance_durations = [ ]
        stance_durations.append(( R1_b, R2_b, R3_b, L1_b, L2_b, L3_b ))

        swing_durations = [ ]
        swing_durations.append(( R1_c, R2_c, R3_c, L1_c, L2_c, L3_c ))

        step_frequencies = [  ] 
        step_frequencies.append(( R1_d, R2_d, R3_d, L1_d, L2_d, L3_d ))

    time_aligned =  { "video_names" : [video_names], 
                  "velocity" : [velocity], # velocity[0][num_flies]
                  "step_amplitudes" : [step_amplitudes], # step_amplitudes[0][0][legs][num_flies]
                  "stance_durations" : [stance_durations], 
                  "swing_durations" : [swing_durations], 
                  "heading" : [heading], # heading[0][num_flies]
                  "step_frequencies" : [step_frequencies],
                  "tripod_coord" : [tripod_coord]} 

    return time_aligned, step_time_store, step_amp_store, stance_time_store, stance_duration, swing_time_store, swing_duration

