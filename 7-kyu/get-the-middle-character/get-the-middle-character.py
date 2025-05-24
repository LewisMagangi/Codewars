def get_middle(s):
    x = len(s) % 2
    y = len(s)//2
    l = y-1
    m = y+1
    if x == 0:
        return s[l:m]
    else:
        return s[y]