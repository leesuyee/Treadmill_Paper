import numpy as np 

def vel_based_swing_stance(combined_leg_velocity, nlegs):

    # create empty matrix
    swing_stance_mat=np.zeros([nlegs,len(combined_leg_velocity[0])])
    frames=np.arange(0,len(combined_leg_velocity[0]))

    # find stance periods: all frames where leg velocity <= 20mm/s 
    stance_period = []
    swing_period = [] 

    for leg in range(0, 6): 
        leg_stance_period = np.where(combined_leg_velocity[leg] < 5)
        stance_period.append(leg_stance_period)

        leg_swing_period = np.where(combined_leg_velocity[leg] >=5)
        swing_period.append(leg_swing_period) 

  # find stance and swing starts - nonconsecutive jumps between stance/swing positions 
    combined_stance_starts = [] 
    combined_swing_starts = [] 
    for leg in range(0, 6): 
        stance_starts_idx = np.where(np.diff(stance_period[leg][0])!=1)
        swing_starts_idx = np.where(np.diff(swing_period[leg][0])!=1)

        all_stance_starts = [] 
        stance_start = [] 

        all_swing_starts = [] 
        swing_start = [] 

        for idx in range(0, len(stance_starts_idx[0])): 
            stance_start = stance_period[leg][0][stance_starts_idx[0][idx]+1]
            all_stance_starts.append(stance_start)

        combined_stance_starts.append(all_stance_starts) 

        for idx in range(0, len(swing_starts_idx[0])): 
            swing_start = swing_period[leg][0][swing_starts_idx[0][idx]+1] 
            all_swing_starts.append(swing_start) 

        combined_swing_starts.append(all_swing_starts) 

    # match swing and stance periods 
    stance_end=[] # store the corresponding stance ends
    for leg in range(0,6): 
        leg_stances=combined_stance_starts[leg]

        # initialize the array for swing mathes
        swing_matches=np.zeros(len(leg_stances))

        # go through each stance and determine the follwoing swing time
        for j in range(0, len(leg_stances)): 
            curr_stance = leg_stances[j]

            #find the closest swing
            diff_swing_stance = combined_swing_starts[leg]-curr_stance

            # ignore negative values
            pos_idxs = np.where(diff_swing_stance>0)[0]

            # match the index to the swing
            #deal with the boundary condition of not finding a corresponding swing
            if len(pos_idxs)==0:
                # take out the stance that doesn't have a match
                combined_stance_starts[leg]=leg_stances[0:j-1]
                swing_matches=swing_matches[0:j-1]
                break
            else:
                # find the index of the closest swing
                pos_vals=diff_swing_stance[pos_idxs]
                min_idx = np.argmin(pos_vals)
                swing_match=combined_swing_starts[leg][np.where(pos_vals[min_idx]==diff_swing_stance)[0][0]]
                swing_matches[j]=swing_match

        # append the matched seing transitions to the stance ends
        stance_end.append(swing_matches.astype(int))
        

    return stance_period, swing_period, combined_stance_starts, combined_swing_starts, stance_end, swing_stance_mat

