# practice example for match pattern too string
import re 
a="pkm.college@gmail.com"
b="bca_pkmcollege@gmail.com"
c="Tybca1234@gmail.com"

d=re.search("[a-z]*.[a-z]*@[a-z]*.[a-z]",a)
e=re.search("[a-z]*_[a-z]*@[a-z]*.[a-z]",b)
f=re.search("[A-Z][a-z]*[0-9]*@[a-z]*.[a-z]",c)
print(d)
print(e)
print(f)