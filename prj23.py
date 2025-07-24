# create dictionary and store in json file
import json

d1={
    "eid":1,
    "ename":"jeet",
    "esal":50000
}
f=open("emp.json",'w')
json.dump(d1,f)

