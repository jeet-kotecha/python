# match pattern string starts with uppercase and contain lowercase with only 1 digit 
import re

name="Jeet21kotecha"
a=re.match("[A-z][a-z]*[0-9]*[a-z]*",name)
print(a)