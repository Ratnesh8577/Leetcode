def island(n, mapping_str, encrypted_str):
    d = {}
    for i in range(n):
        d[chr(97 + i)] = mapping_str[i]           # lowercase
        d[chr(65 + i)] = mapping_str[i].upper()   # uppercase

    ans = ""
    for ch in encrypted_str:
        if ch == "_":
            ans += " "
        elif ch.isalpha():
            ans += d[ch]
        else:
            ans += ch
    return ans

# Input
s = input().split()
n = int(s[0])
mapping_str = s[1]

for _ in range(n):
    encrypted_str = input()
    print(island(n, mapping_str, encrypted_str))
