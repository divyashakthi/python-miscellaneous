cities={1:"ahmedabad",2:"Chennai",3:"New Delhi",4:"Amritsar",5:"Agra"}
def afind(cities):
    v=cities.values()
    for i in v:
        if i[0]=="a"or i[0]=="A":
            print(i)
        else:
            continue
afind(cities)

