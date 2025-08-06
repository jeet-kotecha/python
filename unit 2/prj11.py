# match mobile number start by 8 or 9 and total digit is 10
import re
mno="mobil numbber is 8976543210"
mn="9876543210 is mobil number"
a=re.match("^9",mn)
b=re.match("^8",mn)
c=re.search("[0-9]",mno)
d=re.search("[0-9]",mn)
print(a)
print(b)
print(c)
print(d)