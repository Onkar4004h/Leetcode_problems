def replace_character(s,k):
    l=0
    answer=0
    freq={}
    for r in range(len(s)):
        freq[s[r]]=freq.get(s[r],0)+1
        max_freq=max(freq.values())
        replace=(r-l+1)-max_freq
        if replace>k:
            freq[s[l]]-=1
            l+=1
        answer=max(r-l+1,answer)
    return answer        