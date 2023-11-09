import numpy as np 
from scipy.ndimage import gaussian_filter1d

def swing_stance_classification(time_align_x_pos, time_align_y_pos, FS, nlegs, trial_samples):
    trial_samples = 1500 
    FS = 150 
    nlegs = 6 

    all_frames = np.arange(0, trial_samples)

    dt = 1/FS
    r1_vel = np.sqrt(np.diff(time_align_x_pos[0][0])**2 + np.diff(time_align_y_pos[0][0])**2)/dt
    r2_vel = np.sqrt(np.diff(time_align_x_pos[1][0])**2 + np.diff(time_align_y_pos[1][0])**2)/dt
    r3_vel = np.sqrt(np.diff(time_align_x_pos[2][0])**2 + np.diff(time_align_y_pos[2][0])**2)/dt
    l1_vel = np.sqrt(np.diff(time_align_x_pos[3][0])**2 + np.diff(time_align_y_pos[3][0])**2)/dt
    l2_vel = np.sqrt(np.diff(time_align_x_pos[4][0])**2 + np.diff(time_align_y_pos[4][0])**2)/dt
    l3_vel = np.sqrt(np.diff(time_align_x_pos[5][0])**2 + np.diff(time_align_y_pos[5][0])**2)/dt

    #     # add sign
    r1_vel[np.diff(time_align_x_pos[0][0])<0] = -1*r1_vel[np.diff(time_align_x_pos[0][0])<0]
    r2_vel[np.diff(time_align_x_pos[1][0])<0] = -1*r2_vel[np.diff(time_align_x_pos[1][0])<0]
    r3_vel[np.diff(time_align_x_pos[2][0])<0] = -1*r3_vel[np.diff(time_align_x_pos[2][0])<0]
    l1_vel[np.diff(time_align_x_pos[3][0])<0] = -1*l1_vel[np.diff(time_align_x_pos[3][0])<0]
    l2_vel[np.diff(time_align_x_pos[4][0])<0] = -1*l2_vel[np.diff(time_align_x_pos[4][0])<0]
    l3_vel[np.diff(time_align_x_pos[5][0])<0] = -1*l3_vel[np.diff(time_align_x_pos[5][0])<0]

    # smooth velocities using a gaussian filter
    s =1 # sigma parameter
    r1_smoothed_vel = gaussian_filter1d(r1_vel, s)
    r2_smoothed_vel = gaussian_filter1d(r2_vel, s)
    r3_smoothed_vel = gaussian_filter1d(r3_vel, s)
    l1_smoothed_vel = gaussian_filter1d(l1_vel, s)
    l2_smoothed_vel = gaussian_filter1d(l2_vel, s)
    l3_smoothed_vel = gaussian_filter1d(l3_vel, s)

        # swing stance classification - forward steps
    swing_stance_mat=np.zeros([nlegs, trial_samples])
    # velocity_threshold = 25 # velocities above 20 mm/s classified as swing, from Deangelis paper 
    # swing_stance_mat[0, np.concatenate((np.array([[r1_smoothed_vel > velocity_threshold][0][0]]), r1_smoothed_vel > velocity_threshold))] = 1
    # swing_stance_mat[1, np.concatenate((np.array([[r2_smoothed_vel > velocity_threshold][0][0]]), r2_smoothed_vel > velocity_threshold))] = 1
    # swing_stance_mat[2, np.concatenate((np.array([[r3_smoothed_vel > velocity_threshold][0][0]]), r3_smoothed_vel > velocity_threshold))] = 1
    # swing_stance_mat[3, np.concatenate((np.array([[l1_smoothed_vel > velocity_threshold][0][0]]), l1_smoothed_vel > velocity_threshold))] = 1
    # swing_stance_mat[4, np.concatenate((np.array([[l2_smoothed_vel > velocity_threshold][0][0]]), l2_smoothed_vel > velocity_threshold))] = 1
    # swing_stance_mat[5, np.concatenate((np.array([[l3_smoothed_vel > velocity_threshold][0][0]]), l3_smoothed_vel > velocity_threshold))] = 1
    #     # swing stance classification - forward steps
    # swing_stance_mat=np.zeros([nlegs, trial_samples])
    velocity_threshold = 0 # positive velocities classified as swing
    swing_stance_mat[0, np.concatenate((np.array([[r1_smoothed_vel < velocity_threshold][0][0]]), r1_smoothed_vel < velocity_threshold))] = 1
    swing_stance_mat[1, np.concatenate((np.array([[r2_smoothed_vel < velocity_threshold][0][0]]), r2_smoothed_vel < velocity_threshold))] = 1
    swing_stance_mat[2, np.concatenate((np.array([[r3_smoothed_vel < velocity_threshold][0][0]]), r3_smoothed_vel < velocity_threshold))] = 1
    swing_stance_mat[3, np.concatenate((np.array([[l1_smoothed_vel < velocity_threshold][0][0]]), l1_smoothed_vel < velocity_threshold))] = 1
    swing_stance_mat[4, np.concatenate((np.array([[l2_smoothed_vel < velocity_threshold][0][0]]), l2_smoothed_vel < velocity_threshold))] = 1
    swing_stance_mat[5, np.concatenate((np.array([[l3_smoothed_vel < velocity_threshold][0][0]]), l3_smoothed_vel < velocity_threshold))] = 1

    # #     # swing stance classification - backward steps
    # velocity_threshold = -25 # velocities below 25 mm/s are also considered swing
    # swing_stance_mat[0, np.concatenate((np.array([[r1_smoothed_vel < velocity_threshold][0][0]]), r1_smoothed_vel < velocity_threshold))] = 0
    # swing_stance_mat[1, np.concatenate((np.array([[r2_smoothed_vel < velocity_threshold][0][0]]), r2_smoothed_vel < velocity_threshold))] = 0
    # swing_stance_mat[2, np.concatenate((np.array([[r3_smoothed_vel < velocity_threshold][0][0]]), r3_smoothed_vel < velocity_threshold))] = 0
    # swing_stance_mat[3, np.concatenate((np.array([[l1_smoothed_vel < velocity_threshold][0][0]]), l1_smoothed_vel < velocity_threshold))] = 0
    # swing_stance_mat[4, np.concatenate((np.array([[l2_smoothed_vel < velocity_threshold][0][0]]), l2_smoothed_vel < velocity_threshold))] = 0
    # swing_stance_mat[5, np.concatenate((np.array([[l3_smoothed_vel < velocity_threshold][0][0]]), l3_smoothed_vel < velocity_threshold))] = 0


    # swing and stance transitions
    stance_start = []
    stance_end = []
    for leg in range(nlegs):
        swing_stance_diff = np.diff(swing_stance_mat[leg,:])
        leg_stance_starts = all_frames[np.concatenate((np.array([False]),swing_stance_diff == 1))][1:-1] # ignore first and last stance onset - trial edge effects
        leg_swing_starts = all_frames[np.concatenate((np.array([False]),swing_stance_diff == -1))][1:-1]

        # find stance and swing onset matching pairs
        leg_stance_end = []
        for stance in range(len(leg_stance_starts)):
            stance_idx = leg_stance_starts[stance]
            try: # just in case there is an edge effect (end of trial)
                leg_stance_end.append(leg_swing_starts[[leg_swing_starts - stance_idx][0] > 0][0])
            except: # remove stance start index
                leg_stance_starts = leg_stance_starts[leg_stance_starts != stance_idx] 

        # convert stance end into a numpy array
        leg_stance_end = np.array(leg_stance_end)

        # append stance start and end data across legs
        stance_start.append(leg_stance_starts)
        stance_end.append(leg_stance_end)


    return swing_stance_mat, stance_start, stance_end

