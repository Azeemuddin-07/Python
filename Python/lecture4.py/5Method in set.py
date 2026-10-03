collection = {1, 2, 3, 8, 6}

collection.add((1,2,3))#tuple
collection.add("hello")
collection.add(9)
collection.add(2) # in this case same value are ignored by the set.
print(collection)

# if element is not presemt im the set then remove method give error.
collection.remove(2)
print(collection)

collection.clear()# all set are removed.
print(collection)