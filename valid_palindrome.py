def valid_palindrome(s):

    s = s.lower()
    x = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i in s:
        if i in letters:
            x = x+i
    l = 0
    r = len(x)-1
    print(x)
    while l<r:
        if x[l]!=x[r]:
         return False
                    
        l+=1
        r-=1
    return True

print(valid_palindrome("Marge, let's \"[went].\" I await {news} telegra"))

# j = []
# for i in range(97, 123):
#    j.append(chr(i))
# print(j)