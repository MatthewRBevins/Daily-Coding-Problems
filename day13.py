s = "abcba"
k = 2
longest = 0
longestStr = ""
for i in range(len(s)):
    used = []
    current = 0
    for j in range(i,len(s)):
        if not s[j] in used:
            used.append(s[j])
        if len(used) > k:
            if current > longest:
                longest = current
                longestStr = s[i:j]
            break
        current += 1
print(longestStr)
