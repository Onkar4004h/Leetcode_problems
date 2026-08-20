def valid_anagram(s,t):
    freq1 ={}
    freq2 ={}
    for x in s:
        if x in freq1:
            freq1[x]+=1
        else:
            freq1[x]=1
    for y in t:
        if y in freq2:
                freq2[y]+=1
        else:
            freq2[y]=1
    if freq1==freq2:
         return True
    return False

print(valid_anagram("rat","car"))