

word = ["h","e","l","l","o"]
l = 0
r = len(word)-1
while l<r:
    word[l],word[r]= word[r] , word[l]
    l+=1
    r-=1
print(word)    