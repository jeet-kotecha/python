# open and read data from data.txt using for loop
f=open("unit 2/data.txt",'r')
line=f.readlines()
for i in line:
    print(i,end='')