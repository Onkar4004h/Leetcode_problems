def longest_substring(s):
    l=0
    freq={}
    answer=0
    for r in range(len(s)):
        if s[r] in freq:
            while s[r] in freq:
                del freq[s[l]]
                l+=1
        freq[s[r]]=1
        answer=max(answer,r-l+1)
    return answer             


# print(longest_substring("abcabcbb")) 

def longest_substring_byset(s):
    l=0
    existing_string=set()
    answer=0
    for r in range(len(s)):
        while s[r] in existing_string:
            existing_string.remove(s[l])
            l+=1
        existing_string.add(s[r])
        answer=max(answer,len(existing_string))
    return answer

print(longest_substring_byset("abcabcbb"))       