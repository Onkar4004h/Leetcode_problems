def fruit_basket(fruits):
    l=0
    freq={}
    answer=0
    for r in range(len(fruits)):
        freq[fruits[r]]=freq.get(fruits[r],0)+1
        while len(freq)>2:
            freq[fruits[l]]-=1
            if freq[fruits[l]]==0:
                del freq[fruits[l]]
            l+=1
        answer=max(answer,r-l+1)        
    return answer

print(fruit_basket([3,3,3,1,2,1,1,2,3,3,4]))            