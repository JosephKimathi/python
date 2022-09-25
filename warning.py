
def storm_warning(initial):
    warnings= ["No warning", "Light Air", "Light Breeze", "Gentle Breeze", "Moderate Breeze", "Fresh Breeze", "Strong wind", "Near Gale", "Gale-force wind", "Strong Gale", "Storm-force wind" , "Violent Storm", "Hurricane-force wind"]
    i =0
    if initial>=1 and initial<=5:
        i = 0
    elif initial>=6 and initial<=11:
        i = 0
    elif initial>=12 and initial<=19:
        i = 0
    elif initial>=20 and initial<=28:
        i = 0
    elif initial>=29 and initial<=38:
        i = 0
    elif initial>=39 and initial<=49:
        i = 6
    elif initial>=50 and initial<=61:
        i = 6
    elif initial>=62 and initial<=74:
        i = 8
    elif initial>=75 and initial<=88:
        i = 8
    elif initial>=89 and initial<=102:
        i = 10
    elif initial>=103 and initial<=117:
        i = 10
    elif initial>=118:
        i = 12   
    else:
        i =0    
    return (warnings[i])
    
