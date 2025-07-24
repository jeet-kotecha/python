# write data in json file
import json
f=open("emp.json","a")
j1={"city":"junagadh"}
json.dumps(j1)
s=json.dump(j1,f)