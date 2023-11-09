import numpy as np 

def time_align(frame_idx, smooth_x_pos, smooth_y_pos, rot_head, filt_tx_pos, filt_ty_pos, rot_abdomen): 
    
    time_r1_x = np.empty((1, 1500)) 
    time_r1_x[:] = np.NaN
    time_r1_y = np.empty((1, 1500)) 
    time_r1_y[:] = np.NaN

    time_r2_x = np.empty((1, 1500)) 
    time_r2_x[:] = np.NaN
    time_r2_y = np.empty((1, 1500)) 
    time_r2_y[:] = np.NaN

    time_r3_x = np.empty((1, 1500)) 
    time_r3_x[:] = np.NaN
    time_r3_y = np.empty((1, 1500)) 
    time_r3_y[:] = np.NaN

    time_l1_x = np.empty((1, 1500)) 
    time_l1_x[:] = np.NaN
    time_l1_y = np.empty((1, 1500)) 
    time_l1_y[:] = np.NaN

    time_l2_x = np.empty((1, 1500)) 
    time_l2_x[:] = np.NaN
    time_l2_y = np.empty((1, 1500)) 
    time_l2_y[:] = np.NaN

    time_l3_x = np.empty((1, 1500)) 
    time_l3_x[:] = np.NaN
    time_l3_y = np.empty((1, 1500)) 
    time_l3_y[:] = np.NaN

    time_hx = np.empty((1, 1500)) 
    time_hx[:] = np.NaN
    time_hy = np.empty((1, 1500)) 
    time_hy[:] = np.NaN

    time_tx = np.empty((1, 1500)) 
    time_tx[:] = np.NaN
    time_ty = np.empty((1, 1500)) 
    time_ty[:] = np.NaN

    time_ax = np.empty((1, 1500)) 
    time_ax[:] = np.NaN
    time_ay = np.empty((1, 1500)) 
    time_ay[:] = np.NaN

    for frames in range( 0, len(frame_idx) ): 

        time_r1_x[0, int(frame_idx[frames])] = smooth_x_pos[0][frames] 
        time_r2_x[0, int(frame_idx[frames])] = smooth_x_pos[1][frames] 
        time_r3_x[0, int(frame_idx[frames])] = smooth_x_pos[2][frames] 
        time_l1_x[0, int(frame_idx[frames])] = smooth_x_pos[3][frames] 
        time_l2_x[0, int(frame_idx[frames])] = smooth_x_pos[4][frames] 
        time_l3_x[0, int(frame_idx[frames])] = smooth_x_pos[5][frames] 

        time_r1_y[0, int(frame_idx[frames])] = smooth_y_pos[0][frames] 
        time_r2_y[0, int(frame_idx[frames])] = smooth_y_pos[1][frames] 
        time_r3_y[0, int(frame_idx[frames])] = smooth_y_pos[2][frames] 
        time_l1_y[0, int(frame_idx[frames])] = smooth_y_pos[3][frames] 
        time_l2_y[0, int(frame_idx[frames])] = smooth_y_pos[4][frames] 
        time_l3_y[0, int(frame_idx[frames])] = smooth_y_pos[5][frames] 

        time_hx[0, int(frame_idx[frames])] = rot_head[0][frames] 
        time_hy[0, int(frame_idx[frames])] = rot_head[1][frames] 
        time_tx[0, int(frame_idx[frames])] = filt_tx_pos[frames] 
        time_ty[0, int(frame_idx[frames])] = filt_ty_pos[frames] 
        time_ax[0, int(frame_idx[frames])] = rot_abdomen[0][frames] 
        time_ay[0, int(frame_idx[frames])] = rot_abdomen[1][frames] 
        
    time_align_x_pos = [time_r1_x, time_r2_x, time_r3_x,time_l1_x,
                        time_l2_x, time_l3_x ]
    
    time_align_y_pos = [time_r1_y, time_r2_y, time_r3_y,time_l1_y,
                        time_l2_y, time_l3_y ]
    
    time_align_body_pos = [time_hx, time_hy, time_tx, time_ty, time_ax, time_ay]
    
    return time_align_x_pos, time_align_y_pos, time_align_body_pos
