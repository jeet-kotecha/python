# use of regular Expression module
import re 
a="Hello world this is python lecture and this is practice code of regular expression"
b=re.match("Hello",a) # check that pattern ("Hello") is available in string a at starting  
print(b)
c=re.search("world",a) # check that pattern ("world") is available in string a
print(c)
d=re.findall("this",a) # check and return how many times pattern("this") repeat in string
print(d)