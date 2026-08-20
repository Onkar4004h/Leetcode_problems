def sqrt(x):
    l=1
    while l*l<(x+1):
        if l*l==x:
            return l
        else:
            l+=1
    return (l-1)            