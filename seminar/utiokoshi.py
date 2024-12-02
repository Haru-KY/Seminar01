#left wrist = 15
#right wrist = 16
#left hip = 23
#right hip = 24


def utiokoshi( x_15, y_15, x_16, y_16, x_23, y_23, x_24, y_24 ):

    hip_center = ( x_24 + x_23 ) / 2
    wrist_center = ( x_16 + x_15 ) / 2

    hip_slope = ( y_23 - y_24 ) / ( x_23 - x_24 )
    wrist_slope = ( y_15 - y_16 ) / ( x_15 - x_16 )

    if( ( hip_center - wrist_center ) < 0.02 and 
        ( hip_center - wrist_center ) > -0.02 and 
        ( hip_slope - wrist_slope ) < 5 and 
        ( hip_slope - wrist_slope ) > -5 and 
        x_15 - x_23 < 0.02 and 
        x_15 - x_23 > -0.02 and
        x_16 - x_24 < 0.02 and 
        x_16 - x_24 > -0.02 ):
        return True
    else:
        return False