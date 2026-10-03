light = input("enter the light color : ")

if(light == "red"):
    print("stop")
#elif always comes after the if.
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

#after the above all cond. are false then else condn. will be run.