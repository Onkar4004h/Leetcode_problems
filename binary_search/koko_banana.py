def koko_banana(piles,h):
    l=1
    r =  max(piles)
    while l<r:
        mid=(l+r)//2
        hour=0
        for pile in piles:
            hour+=(pile+mid-1)//mid
        if hour<=h:
            r=mid
        else:
            l=mid+1
    return r         
    
print(koko_banana([30,11,23,4,20],5))            

  
