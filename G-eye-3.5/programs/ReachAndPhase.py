import numpy as np        
from defs import phase
import math

def RAP_def(pole_top,Y,h,w):
    theta_Y=phase.HighToTheta(pole_top[1].astype(int),int(h/2),0.674)
    theta_X=phase.HighToTheta(pole_top[0].astype(int),int(w/2),0.674*(w/h))

    Reach=Y/(math.cos(theta_X)*math.tan(theta_Y))

    return theta_X,Reach