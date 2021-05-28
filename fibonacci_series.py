for _ in range(int(input())):
    a=input()
    d={}
    for i in a:
        if i in d:
            d.update({i:d.get(i)+1})
        else:
            d.update({i:1})
    l=[]
    for i in d.values():
        l.append(i)
    l.sort()
    if len(l)<3:
        print("Dynamic")
    else:
        if l[-1]==l[-2]+l[-3]:
            print("Dynamic")
        else:
            print("Not")