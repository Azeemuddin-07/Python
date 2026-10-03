str = "apnacollege"
for char in str:
    print(char)

else:
    print("end")


str = "apnacollege"
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
#else: #after break, no else statement will run.
#    print(end)
print("end")