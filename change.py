def get_change(due, tendered):
    change = abs(tendered - due)
    five = change//5
    two = (change - five*5)//2
    one =change - five*5 - two*2
    return "R5:"+str(five)+" R2:"+str(two)+ " R1: "+str(one)
