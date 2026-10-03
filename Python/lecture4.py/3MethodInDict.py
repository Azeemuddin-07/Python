#method in dict.
# myDict.keys(),myDict.values()...etc

student = {
    "name" : "Ajju",
    "subject" : {
        "maths" : 90,
        "phy" : 85,
        "chem" : 88
    }
}
print(student.keys())
# typecast in list.
print(list(student.keys()))
print(len(list(student.keys())))

#myDict.values() --> return all values.
print(student.values())

#myDict.items() --> return all (keys,value) pair as tuple.
print(student.items())

#myDict.get("key") --> return the key acoording to value.
print(student.get("name"))

student.update({"city" : "delhi"})
#or
# new_dict = {"city" : "supaul"}
# student.update(new_dict)
print(student)