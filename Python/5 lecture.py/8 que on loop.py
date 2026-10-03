list =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#x = 64
x= int(input("enter the no."))

idx = 0
for el in list:
    if(el == x):
        print("number found at idx", idx )
    idx += 1