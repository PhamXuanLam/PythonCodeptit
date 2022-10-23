with open('DATA.in', 'r') as file:
    data = [s.strip() for s in file.readlines()]
    b=[]
    c = []
    for line in data:
        b.extend(line.split())
    for i in b:
        try:
            if(len(i)<10):
                i = int(i)
        except:
            c.append(i)
        if type(i) is str and len(i)>9:
            c.append(i)
    c.sort()
    for i in c:
        print(i,end=" ")
    file.close()