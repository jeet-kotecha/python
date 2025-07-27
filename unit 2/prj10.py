# use of regular expression using synbols
import re
a="kitkat is chocolate"
b="pkm.coll+ege@gma-il.com"
c="hello"
d="xyz,xy,xyzz,xyzzy,zxz"

m=re.search(r"\.",b)
print(m)
m1=re.search("@",b)
print(m1)
m2=re.search("^kit",a)
print(m2)
m3=re.search("ate$",a)
print(m3)
m5=re.search("cho*co",a)
m6=re.search("cho?co",a)
m7=re.search("cho+co",a)
print(m5)
print(m6)
print(m7)