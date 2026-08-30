def minimun_window_substring(s,t):
    freq1={}
    freq2={}
    count=0
    for x in t:
        freq1[x]=freq1.get(x,0)+1
    l=0
    answer=""
    for r in range(len(s)):
        if s[r] in freq1:
            freq2[s[r]]=freq2.get(s[r],0)+1
            if freq2[s[r]]<=freq1[s[r]]:
                count+=1
        while count==len(t):
            if answer=="" or r-l+1<len(answer):
                answer=s[l:r+1]
            if s[l] in freq1:
                freq2[s[l]]-=1
                if freq1[s[l]]>freq2[s[l]]:
                    count-=1
            l+=1
    return answer
print(minimun_window_substring("ADOBECODEBANC","ABC"))

