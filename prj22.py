# create json object 
import json
j1={"rno":1,"name":"jeet","sub":["py","j2ee","asp.net"]} 
j=json.dumps(j1)
f1=json.loads(j)
print(f1) 