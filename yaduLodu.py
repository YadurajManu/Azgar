d={"manu":[12,32,32], "rahul":[21,32,43], "yadu":[12,32,43]}
name = input("emter")
if name in d:
    L=d[name]
    avg=(L[0]+L[1]+L[2])/3
    print(avg)
else:
    print("no")
