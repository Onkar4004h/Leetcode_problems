def ship_package(weights,days):
    l=max(weights)
    r=sum(weights)
    while l<r:
        mid=(l+r)//2
        days_needed=1
        total_weight=0
        for weight in weights:
            if total_weight+weight>mid:
                days_needed+=1
                total_weight=weight
            else:
                total_weight+=weight    
        if days_needed<=days:
            r=mid
        else:
            l=mid+1
    return r

print(ship_package([1,2,3,4,5,6,7,8,9,10],5))               