import numpy as np 

def norm(x_pos, y_pos, body_pos): 

    norm_x_pos = x_pos - body_pos[2]
    norm_y_pos = y_pos - body_pos[3]
    norm_hx = body_pos[0] - body_pos[2] 
    norm_hy = body_pos[1] - body_pos[3] 
    norm_ax = body_pos[4] - body_pos[2] 
    norm_ay = body_pos[5] - body_pos[3] 
    
    norm_body_pos = norm_hx, norm_hy, body_pos[2], body_pos[3], norm_ax, norm_ay
    
    return norm_x_pos, norm_y_pos, norm_body_pos