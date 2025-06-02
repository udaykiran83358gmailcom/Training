s = "abaabba"
l, r = 0, 0
maxi = 0
t=0
while r < len(s):
    curr = s[l:r+1]  
    if curr == curr[::-1] and len(curr) > 1:
        
        if maxi < len(curr):
            maxi = len(curr)
    if r == len(s) - 1:
        l += 1
        r = l
    else:
        r += 1
print(len(s)+t)
print(maxi)
