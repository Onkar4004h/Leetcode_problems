def max_no_of_vowels(s,k):
    l=0
    answer=0
    no_of_vowels=0
    seen = ("a","e","i","o","u")
    for r in range(len(s)):
        if s[r] in seen:
            no_of_vowels+=1
        if r-l+1>k:
            if s[l] in seen:
                no_of_vowels-=1
            l+=1
        if r-l+1==k:
            answer=max(answer,no_of_vowels)
    return answer        
print(max_no_of_vowels("abciiidef",3))            
               
