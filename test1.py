arr = [1,1,2,5,5,6]
dic = {}
for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

print(dic)