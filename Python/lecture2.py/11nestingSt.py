# Nesting.

age = int(input("Enter age :"))

if(age>=18): #nested.
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

