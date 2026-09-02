def isomorphic_string(s,t):
#   seen1=set(s)
#   seen2=set(t)
#   if len(seen1)==len(seen2):
#     return True
#   else:
#     return False
    # freq1={}
    # freq2={}
    # for x in s:
    #     freq1[x]=freq1.get(x,0)+1
    # for y in t:
    #     freq2[y]=freq2.get(y,0)+1
    # if freq1==freq2:
    #     return True
    # else:
    #     return False
    freq1={}
    freq2={}
    for x in range(len(s)):
        a=s[x]
        b=t[x]
        if a in freq1:
            if freq1[a]!=b:
                return False
        else:
            freq1[a]=b
        if b in freq2:
            if freq1[b]!=a:
                return False
        else:
            freq2[b]=a 
    return True           


print(isomorphic_string("f11","b23"))  
