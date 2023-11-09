import numpy as np 

def smooth(x_pos, y_pos, filled_tx, filled_ty):

    win_size=10
    win_edge=int(np.floor(win_size/2))
    smooth_x_pos=[]
    smooth_y_pos=[]
    for leg in range(len(x_pos)):
        filt_x_pos=np.zeros(len(x_pos[0]))
        filt_x_pos[0:win_size]=x_pos[leg][0:win_size]
        filt_x_pos[-win_size::]=x_pos[leg][-win_size::]

        filt_y_pos=np.zeros(len(y_pos[0]))
        filt_y_pos[0:win_size]=y_pos[leg][0:win_size]
        filt_y_pos[-win_size::]=y_pos[leg][-win_size::]
        for j in range(5, len(x_pos[0])-win_size):
            start_idx = j - win_edge
            end_idx= j + win_edge
            filt_x_pos[j]=np.mean(x_pos[leg][start_idx:end_idx])
            filt_y_pos[j]=np.mean(y_pos[leg][start_idx:end_idx])

        smooth_x_pos.append(filt_x_pos)
        smooth_y_pos.append(filt_y_pos)
    
    filt_tx_pos = np.zeros(len(filled_tx)) 
    filt_tx_pos[0:win_size]=filled_tx[0:win_size]
    filt_tx_pos[-win_size::]=filled_tx[-win_size::] 
    
    filt_ty_pos = np.zeros(len(filled_ty))
    filt_ty_pos[0:win_size]=filled_ty[-win_size::]
    filt_ty_pos[-win_size::]=filled_ty[-win_size::] 
        
    for a in range(0, len(filled_tx)-win_size):  
        start_idx = a - win_edge
        end_idx = a + win_edge 
        filt_tx_pos[a]=np.mean(filled_tx[start_idx:end_idx]) 
        filt_ty_pos[a]=np.mean(filled_ty[start_idx:end_idx])
                                            
        
    return smooth_x_pos, smooth_y_pos, filt_tx_pos, filt_ty_pos