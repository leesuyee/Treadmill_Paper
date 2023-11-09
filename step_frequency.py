import numpy as np 

def step_freq(stance_start, time):
    cur_time=time
    step_frequency=[]
#    fig_num=fig_num+1
    for leg in range(0,len(stance_start)):
        
        # get times of when stance starts
        stance_time=cur_time[stance_start[leg]]
        
        # calculate the difference in time
        stance_dt=np.diff(stance_time)
        
        # compute step frequency
        freq=1/stance_dt
        
        step_frequency.append(freq)
        
#     # plot step frequency across time
#     # r1
#     plt1=plt.figure(fig_num, figsize=[10,5])
#     plt.plot(cur_time[stance_start[0][1::]], step_frequency[0], color='black', linewidth=1.25)
#     plt.xlabel('time (seconds)', fontsize=18)
#     plt.ylabel('step frequency (1/s)', fontsize=18)
#     plt.title('r1 step frequency', fontsize=18)
#     fig_num=fig_num+1
# #     fig_name= save_dir+'r1 step frequency'+fig_type
# #     plt1.savefig(fig_name, dpi=dpi_value)
    
#     # r2
#     plt2=plt.figure(fig_num, figsize=[10,5])
#     plt.plot(cur_time[stance_start[1][1::]], step_frequency[1], color='black', linewidth=1.25)
#     plt.xlabel('time (seconds)', fontsize=18)
#     plt.ylabel('step frequency (1/s)', fontsize=18)
#     plt.title('r2 step frequency', fontsize=18)
#     fig_num=fig_num+1
# #     fig_name= save_dir+'r2 step frequency'+fig_type
# #     plt2.savefig(fig_name, dpi=dpi_value)
    
#     # r3
#     plt3=plt.figure(fig_num, figsize=[10,5])
#     plt.plot(cur_time[stance_start[2][1::]], step_frequency[2], color='black', linewidth=1.25)
#     plt.xlabel('time (seconds)', fontsize=18)
#     plt.ylabel('step frequency (1/s)', fontsize=18)
#     plt.title('r3 step frequency', fontsize=18)
#     fig_num=fig_num+1
# #     fig_name= save_dir+'r3 step frequency'+fig_type
# #     plt3.savefig(fig_name, dpi=dpi_value)

#     # plot step frequency across time
#     # l1
#     plt4=plt.figure(fig_num, figsize=[10,5])
#     plt.plot(cur_time[stance_start[3][1::]], step_frequency[3], color='black', linewidth=1.25)
#     plt.xlabel('time (seconds)', fontsize=18)
#     plt.ylabel('step frequency (1/s)', fontsize=18)
#     plt.title('l1 step frequency', fontsize=18)
#     fig_num=fig_num+1
# #     fig_name= save_dir+'r1 step frequency'+fig_type
# #     plt1.savefig(fig_name, dpi=dpi_value)
    
#     # l2
#     plt5=plt.figure(fig_num, figsize=[10,5])
#     plt.plot(cur_time[stance_start[4][1::]], step_frequency[4], color='black', linewidth=1.25)
#     plt.xlabel('time (seconds)', fontsize=18)
#     plt.ylabel('step frequency (1/s)', fontsize=18)
#     plt.title('l2 step frequency', fontsize=18)
#     fig_num=fig_num+1
# #     fig_name= save_dir+'r2 step frequency'+fig_type
# #     plt2.savefig(fig_name, dpi=dpi_value)
    
#     # l3
#     plt6=plt.figure(fig_num, figsize=[10,5])
#     plt.plot(cur_time[stance_start[5][1::]], step_frequency[5], color='black', linewidth=1.25)
#     plt.xlabel('time (seconds)', fontsize=18)
#     plt.ylabel('step frequency (1/s)', fontsize=18)
#     plt.title('l3 step frequency', fontsize=18)
#     fig_num=fig_num+1
# #     fig_name= save_dir+'r3 step frequency'+fig_type
# #     plt3.savefig(fig_name, dpi=dpi_value)

    
    return(step_frequency)