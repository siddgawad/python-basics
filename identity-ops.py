

x=[14,15,16]
y=[14,15,16]

print(y is x)
print(y==x)


x=y.copy() #this creates new list in memory location whereas x=y points to same list location in memory


print(x)


print("New program: \n")
print("\n")
x=[4,7,10]
y=[2,6,9]
x=y.copy()
x=[1,2,3]

print(x)


print("New program : \n")
print("\n")
x=[4,7,10]
y=[2,6,9]
x=y
print(x)