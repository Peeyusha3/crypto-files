import re
s = input("Ënter the secret message:\n")
rt=''
s=re.sub("[^a-zA-Z' ']+", "", s)
print(s) 
for i in range(len(s)):
    if s[i]==' ':
        rt=rt+' '
        continue
    diff=int(ord(s[i]))-7
    if 90<=diff<97:
        diff=122-(97-diff-1)
    elif diff<65:
        diff=90-(65-diff-1)
    rt=rt+chr(diff)
print("Decoded message is: ",rt)

