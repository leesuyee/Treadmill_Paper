import numpy as np 
def compute_tcs(stance_start, stance_end, FS):
    save_tcs = [] 

    # compute tripod coordination strength
    # use stance_start and stance_end times
    # leg ids of each tripod

    #right_tripod
    r1_stances = stance_start[0]
    r1_swings = stance_end[0]
    l2_stances = stance_start[4]
    l2_swings = stance_end[4]
    r3_stances = stance_start[2]
    r3_swings = stance_end[2]

    # tolerance of a tripods leg entering stance relative to the onset of swing of the reference leg
    tol = 3

    # storage lists
    right_tsc=[]
    right_tsc_time=[]

    # determine the closest stance start of l2 and r3 to that of r1
    if len(r1_stances) > 0 and len(l2_stances) > 0 and len(r3_stances) > 0: 
        for j in range(len(r1_stances)):

            # match stances of a step with reference of those of r1
            ref_stance = r1_stances[j]

            # find the closest indices
            diff_l2=l2_stances-ref_stance
            diff_r3=r3_stances-ref_stance

            # convert negative values into positive values because want jsut the magnitude
            l2_neg_idxs = np.where(diff_l2 <0)[0]
            diff_l2[l2_neg_idxs]=-diff_l2[l2_neg_idxs]
            r3_neg_idxs = np.where(diff_r3 <0)[0]
            diff_r3[r3_neg_idxs]=-diff_r3[r3_neg_idxs]

            # find the minimum idx
            l2_min_idx=np.argmin(diff_l2)
            l2_match_stance=l2_stances[l2_min_idx]
            r3_min_idx=np.argmin(diff_r3)
            r3_match_stance=r3_stances[r3_min_idx]

            # only continue calculate tcs if the stance onsets of l2 and r3 are less than the swing onset of r1 minus a tolerance
            ref_swing=r1_swings[j]
            if (l2_match_stance < (ref_swing-tol)) and (r3_match_stance < (ref_swing-tol)):
                # find the corresponding swing times
                 # find the closest indices
                diff_l2=l2_swings-ref_swing
                diff_r3=r3_swings-ref_swing

                # convert negative values into positive values because want jsut the magnitude
                l2_neg_idxs = np.where(diff_l2 <0)[0]
                diff_l2[l2_neg_idxs]=-diff_l2[l2_neg_idxs]
                r3_neg_idxs = np.where(diff_r3 <0)[0]
                diff_r3[r3_neg_idxs]=-diff_r3[r3_neg_idxs]

                # find the minimum idx
                l2_min_idx=np.argmin(diff_l2)
                l2_match_swing=l2_swings[l2_min_idx]
                r3_min_idx=np.argmin(diff_r3)
                r3_match_swing=r3_swings[r3_min_idx]

                # calculate t1: duration legs are in stance together
                # comute the max of those legs in stance
                last_stance=max(np.array([ref_stance, l2_match_stance, r3_match_stance]))
                first_swing=min(np.array([ref_swing, l2_match_swing, r3_match_swing]))
                t1=(first_swing-last_stance)/FS

                # calculate t2: total time that elapsed from the first leg entering stance and the last leg entering swing
                first_stance=min(np.array([ref_stance, l2_match_stance, r3_match_stance]))
                last_swing=max(np.array([ref_swing, l2_match_swing, r3_match_swing]))
                t2=(last_swing-first_stance)/FS

                # compute tcs, ratio of t1/t2
                if (t1>0) and (t2>0): # just in case of missed indices
                    tcs=t1/t2
                    right_tsc.append(tcs)
                    right_tsc_time.append(ref_stance)

        #         print(j)
        #         print('r1 stance: ', ref_stance)
        #         print('l2 stance: ', l2_match_stance)
        #         print('r3 stance: ', r3_match_stance)
        #         print('r1 swing: ', ref_swing)
        #         print('l2 swing: ', l2_match_swing)
        #         print('r3 swing: ', r3_match_swing)
        #         print('tcs: ', tcs)

            else: 
                pass
#                 tcs = np.nan
#                 ref_stance = np.nan
#                 right_tsc.append(tcs)
#                 right_tsc_time.append(ref_stance)
        else: 
            pass
#             tcs = np.nan
#             ref_stance = np.nan
#             right_tsc.append(tcs)
#             right_tsc_time.append(ref_stance)





    #left_tripod
    l1_stances = stance_start[3]
    l1_swings = stance_end[3]
    r2_stances = stance_start[1]
    r2_swings = stance_end[1]
    l3_stances = stance_start[5]
    l3_swings = stance_end[5]


    # storage lists
    left_tsc=[]
    left_tsc_time=[]

    # determine the closest stance start of l2 and r3 to that of r1
    if len(l1_stances) > 0 and len(r2_stances) > 0 and len(l3_stances) > 0: 
        for j in range(len(l1_stances)):

            # match stances of a step with reference of those of r1
            ref_stance = l1_stances[j]

            # find the closest indices
            diff_r2=r2_stances-ref_stance
            diff_l3=l3_stances-ref_stance

            # convert negative values into positive values because want jsut the magnitude
            r2_neg_idxs = np.where(diff_r2 <0)[0]
            diff_r2[r2_neg_idxs]=-diff_r2[r2_neg_idxs]
            l3_neg_idxs = np.where(diff_l3 <0)[0]
            diff_l3[l3_neg_idxs]=-diff_l3[l3_neg_idxs]

            # find the minimum idx
            r2_min_idx=np.argmin(diff_r2)
            r2_match_stance=r2_stances[r2_min_idx]
            l3_min_idx=np.argmin(diff_l3)
            l3_match_stance=l3_stances[l3_min_idx]

            # only continue calculate tcs if the stance onsets of l2 and r3 are less than the swing onset of r1 minus a tolerance
            ref_swing=l1_swings[j]
            if (r2_match_stance < (ref_swing-tol)) and (l3_match_stance < (ref_swing-tol)):
                # find the corresponding swing times
                 # find the closest indices
                diff_r2=r2_swings-ref_swing
                diff_l3=l3_swings-ref_swing

                # convert negative values into positive values because want jsut the magnitude
                r2_neg_idxs = np.where(diff_r2 <0)[0]
                diff_r2[r2_neg_idxs]=-diff_r2[r2_neg_idxs]
                l3_neg_idxs = np.where(diff_l3 <0)[0]
                diff_l3[l3_neg_idxs]=-diff_l3[l3_neg_idxs]

                # find the minimum idx
                r2_min_idx=np.argmin(diff_r2)
                r2_match_swing=r2_swings[r2_min_idx]
                l3_min_idx=np.argmin(diff_l3)
                l3_match_swing=l3_swings[l3_min_idx]

                # calculate t1: duration legs are in stance together
                # comute the max of those legs in stance
                last_stance=max(np.array([ref_stance, r2_match_stance, l3_match_stance]))
                first_swing=min(np.array([ref_swing, r2_match_swing, l3_match_swing]))
                t1=(first_swing-last_stance)/FS

                # calculate t2: total time that elapsed from the first leg entering stance and the last leg entering swing
                first_stance=min(np.array([ref_stance, r2_match_stance, l3_match_stance]))
                last_swing=max(np.array([ref_swing, r2_match_swing, l3_match_swing]))
                t2=(last_swing-first_stance)/FS

                # compute tcs, ratio of t1/t2
                if (t1 > 0) and (t2 > 0): # just in case of missed indices
                    tcs=t1/t2
                    left_tsc.append(tcs)
                    left_tsc_time.append(ref_stance)

        #         print(j)
        #         print('l1 stance: ', ref_stance)
        #         print('r2 stance: ', r2_match_stance)
        #         print('l3 stance: ', l3_match_stance)
        #         print('l1 swing: ', ref_swing)
        #         print('r2 swing: ', r2_match_swing)
        #         print('l3 swing: ', l3_match_swing)
        #         print('tcs: ', tcs)
        #         print('t1: ', t1)
        #         print('t2: ', t2)

            else: 
                pass
#                 tcs = np.nan
#                 ref_stance = np.nan
#                 left_tsc.append(tcs)
#                 left_tsc_time.append(ref_stance)
        else:
            pass
#             tcs = np.nan
#             ref_stance = np.nan
#             left_tsc.append(tcs)
#             left_tsc_time.append(ref_stance)

    # combine the tripod coordination results of the right and left legs
    combined_tcs=np.concatenate([np.array(right_tsc), np.array(left_tsc)])
    combined_tcs_frame=np.concatenate([np.array(right_tsc_time), np.array(left_tsc_time)])

    # sort indices
    sort_idxs=np.argsort(combined_tcs_frame)
    sorted_tcs_frames=combined_tcs_frame[sort_idxs]
    sorted_tcs=combined_tcs[sort_idxs]

    # filter tcs if not walking
    #     for j in range(0,len(sorted_tcs)-1):
    #             step=np.where(np.logical_and(non_walking_indices>=sorted_tcs_frames[j], non_walking_indices<=sorted_tcs_frames[j+1]))[0]
    #             if step.size > 0: # there is a non-step
    #                 sorted_tcs[j]=np.nan

    #     # plot tripod coordination strength
    #     plt.figure(1, figsize=[10,5])
    #     plt.plot(sorted_tcs_frames, sorted_tcs, color='black', linewidth=1.5)
    #     plt.xlabel('Frame (#)', fontsize=18)
    #     plt.ylabel('TCS', fontsize=18)


    # compute stats of tcs
    mean_tcs=np.nanmean(sorted_tcs)
    std_tcs=np.nanstd(sorted_tcs)
    tcs_stat=[mean_tcs, std_tcs]
    
    save_tcs.append(sorted_tcs_frames) 
    save_tcs.append(sorted_tcs) 
    #     #time
    #     sorted_tcs_time=sorted_tcs_frames
    return(save_tcs) 

