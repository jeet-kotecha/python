# Match pattern (8999)-388-99877665
import re
no="number is (8999)-388-99877665"
a=re.search("\([0-9]{4}\)-[0-9]{3}-[0-9]{8}",no)
print(a)