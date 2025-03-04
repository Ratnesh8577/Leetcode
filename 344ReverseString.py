#Reverse String
def reverseString(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s
#Driver code
s=['h','e','l','l','o']
x=reverseString(s)
print(x)