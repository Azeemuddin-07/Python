#WAP to enter marks of 3 subject from the user and store them in a dictionary.
#start with an empty dictionary & add one by one. 
#use subject name as key & marks as values.
# part 2 
#figure out way to store 9 & 9.0 as seprate value in the set .
#(you can take help of built in data type)

marks = {}
x = int(input("enter phy : "))
marks.update({"phy" : x })
x = int(input("enter maths : "))
marks.update({"maths" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)

#part 2

values = {9, 9.0} # give only 9 in a set
print(values)
# but
val = {9, "9.0"}
print(val)

# other solution in tuple form because tuples are immutable
vall = {
    ("float", 9.0), # tuples are immutable hence dictionary is mutable.
    ("int", 9)      # thats why tuple stored in set, since the element of set is also immutable.
}
print(vall)