# create file data.txt and add info using file handling function
f=open("unit 2/data.txt",'w')

f.write("Roll no : 25 \n")
f.write("Name : jeet kotecha\n")
f.close()
f=open("unit 2/data.txt",'a')
f.write("std : BCA tyc")
f.close()
