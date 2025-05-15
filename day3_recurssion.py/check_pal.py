def check(s,i):
    if i>=len(s)/2:
        return True
    if s[i]==s[len(s)-i-1]:
        return check(s,i+1)
    else:
        return False
print(check("uday",0))
