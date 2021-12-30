for _ in range(int(input())):
    a=input()
    d={}
    for i in a:
        d[i] = d.get(i)+1 if i in d else 1
    l = list(d.values())
    l.sort()
    if len(l)<3:
        print("Dynamic")
    elif l[-1]==l[-2]+l[-3]:
        print("Dynamic")
    else:
        print("Not")