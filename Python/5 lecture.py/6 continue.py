i = 0 
while i <= 5:
    if(i == 3): # 3 is skip by continue keyword.
        i += 1
        continue #skip
    print(i)
    i += 1

print("another part")
# odd and even

i = 1 
while i <= 10:
    if(i%2 == 0): # for even if(i%2 != 0).
        i += 1
        continue
    print(i)
    i += 1