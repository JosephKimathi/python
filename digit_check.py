import sys
def disp(arr):
    s= ""
    for i in arr:
        s += str(i) +" "
    print(s)
    
def is_valid_usnum(n):
    # for i < 8
    sum = 0
    #checksum = sum of all (characters*their indices) ~ index 1 = last digit ~k*digit(k)
    n = str(n)
    for i in range(8):
        c = int(n[i])
        sum+= (8-i)*c
    return (sum%11) == 0
    
def control_digit(n):
    sum = 0
    n = str(n)
    for i in range(7):
        c = int(n[i])
        sum+= c*(8-i)
    diff = sum % 11
    return (11 - diff)%11
    
if __name__ == '__main__':
    arr = sys.argv
    print(is_valid_usnum(arr[1]))
