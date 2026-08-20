def unique_element(s):

    freq = {}
    for x in s:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    answer = ""        
    for letter,count in freq.items():
        if count==1:
            answer=letter
            break
    for i in range(len(s)):
        if s[i]==answer:
            return i 
    return -1  