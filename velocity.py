import numpy as np 

def velocity(hx, hy, FPS, win_size, BL): 
    dt=1/FPS 
    dx=np.diff(hx)
    dy=np.diff(hy)

    # euclidean distance 
    dist = np.sqrt(dx**2+dy**2)
    vel = dist/dt 

#     filter the velocity with an average sliding window
#     win_size= 5 # five frame sliding window
    nframes=len(vel)
    filt_vel=np.zeros(nframes)
    for j in range(nframes-win_size):
        filt_vel[j] = np.mean(vel[j:j+win_size])

    # fill in end with the last filtered positon
    filt_vel[(nframes-win_size)::] = filt_vel[(nframes-win_size)-1]

    lin_vel=filt_vel

#     median filter
    linear_vel_filter=filt_vel/BL
#     linear_vel_filter = vel 
    
    return linear_vel_filter 



    
