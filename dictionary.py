import json
t={}
for k in range(3):
    t['pdf']=['python','page120']
    t['doc']={"Physics":["contents80","exercises10","solution15"]}
    t['ppt']=['chemistry','noteslides50','EXslides10']
print(t['doc']["Physics"][2])
print(t['ppt'][0])
print(t['pdf'][1])
print(json.dumps(t,indent=3))
