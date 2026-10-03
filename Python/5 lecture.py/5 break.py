i = 1 
while i <= 5:
    print(i)
    if(i ==3 ):
        break
    i += 1


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36
i = 0 #initilization.
while i < len(nums):
    if(nums[i]==x):
        print("found idx :",i)
       # break  #it terminate the next loop operation when element is found.
    else:
        print("finding...")
    i += 1
