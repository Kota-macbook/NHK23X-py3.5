import numpy as np

def phase(phase_X,border_phase,PID,L_I,R_I,L_D,R_D):

    if(abs(phase_X)>border_phase):
        L_move=PID[0]*phase_X+PID[1]*L_I-PID[2]*(L_D)
        R_move=PID[0]*phase_X+PID[1]*R_I-PID[2]*(R_D)
    elif(phase_X>0):
        L_move=PID[0]*phase_X+PID[1]*L_I-PID[2]*(L_D)
        R_move=0.0
    else:
        R_move=PID[0]*phase_X+PID[1]*R_I-PID[2]*(R_D)
        L_move=0.0

    return L_move,R_move


        