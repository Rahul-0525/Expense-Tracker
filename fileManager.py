import json

with open('savedata.json','w') as file:
    content = {5:'a',2:'b',3:'c'}
    json.dump(content,file,indent=4)

with open('savedata.json','r') as file:
    d = json.load(file)

print(d)
print(type(d))

