fruits = ["apple","banana","cherry"]

print("apple" in fruits)
print("mango" in fruits )


collection = {"name":"sid", "age":23} 
print("sid" in collection) #this returns false becasue sid is a value, not key
print("name" in collection)
print("age" in collection)

#to check for sid we write 

print("sid" in collection.values())
