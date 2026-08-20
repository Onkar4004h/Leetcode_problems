strg = ["eat","tea","tan","ate","nat","bat"]
freq = {}
result = []
for str in range(len(strg)):
    str_split = list(strg[str])
    str_split.sort()
    str_joined = "".join(str_split)
    if str_joined not in freq:
        freq[str_joined] = []
    freq[str_joined].append(strg[str])

print(list(freq.values()))