l1=[1,2,3,4,5,6,7,8,9,10]

for i in l1:
    if i%2==0: 
        print(i,end='') 
print("\n")        
l1[2]=30
print(l1)

l1[6]=60
print(l1)

l1.remove(10)
print(l1)

l1.append(50)
print(l1)

l1.append(100)
print(l1)

l1.insert(9,10)
print(l1)

for i in l1:
    print(i,end=' ')