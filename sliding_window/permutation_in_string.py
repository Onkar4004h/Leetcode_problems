def permutation_in_string(s1,s2):
    freq1={}
    freq2={}
    for x in s1:
        freq1[x]=freq1.get(x,0)+1
    l=0
    for r in range(len(s2)):
        freq2[s2[r]]=freq2.get(s2[r],0)+1
        if r-l+1>len(s1):
            freq2[s2[l]]-=1
            if freq2[s2[l]]==0:
                del freq2[s2[l]]
            l+=1
        if freq2==freq1:
            return True    
    return False

print(permutation_in_string("ab","eidbaooo"))        
