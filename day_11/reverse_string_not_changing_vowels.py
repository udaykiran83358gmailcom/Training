s="hippopotamus"
s=list(s)
l,r=0,len(s)-1
vow="aeiou"
while l<=r:
    if (s[l] not in vow) and (s[r] not in vow):
        s[r],s[l]=s[l],s[r]
        l+=1
        r-=1
    if s[l] in vow:
        l+=1
    if s[r]  in vow:
        r-=1
print("".join(s))
