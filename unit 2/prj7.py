# create empty list std and input elements from the user anf print elements using for loop
std=[]

for i in range(5):
    val=input(f"Enter element {i+1}:")
    std.append(val)
for j in std:
    print(j)